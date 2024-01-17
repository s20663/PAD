import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np
from scipy import stats
import statsmodels.api as sm


# Wczytanie danych
data = pd.read_csv('messy_data.csv')

# Czyszczenie danych
data.replace('', np.nan, inplace=True)
data.columns = data.columns.str.strip()
kolumny_kategoryczne = ['clarity', 'color', 'cut']
for col in kolumny_kategoryczne:
    data[col] = data[col].astype('category')
data.dropna(inplace=True)

enkodery_labeli = {}
for col in kolumny_kategoryczne:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    enkodery_labeli[col] = le

kolumny_numeryczne = ['carat', 'x dimension', 'y dimension', 'z dimension', 'depth', 'table']
for col in kolumny_numeryczne:
    data[col] = pd.to_numeric(data[col], errors='coerce')



data = data.apply(pd.to_numeric, errors='coerce')
data.dropna(subset=kolumny_numeryczne, inplace=True)

# 1. Usunięcie duplikatów
data.drop_duplicates(inplace=True)

# 2. Analiza wartości odstających (przykład z wynikami Z)
z_scores = np.abs(stats.zscore(data[kolumny_numeryczne]))
outliers = (z_scores > 3).any(axis=1)
data = data[~outliers]

# 3. Analiza spójności i inne etapy czyszczenia danych

# Analiza zakresu wartości w kolumnach numerycznych
for col in kolumny_numeryczne:
    print(f"Zakres wartości w kolumnie {col}: {data[col].min()} - {data[col].max()}")

# Usunięcie dokładnych duplikatów (poza indeksem)
data.drop_duplicates(subset=data.columns.difference(['id']), keep='first', inplace=True)

# # Dodatkowe etapy analizy spójności
# korelacja = data[kolumny_numeryczne].corr()
# sns.heatmap(korelacja, annot=True, cmap='coolwarm', linewidths=0.5)
# plt.title('Macierz korelacji między zmiennymi numerycznymi')
# plt.show()
#
# # Analiza występowania outlierów
# for col in kolumny_numeryczne:
#     sns.boxplot(x=data[col])
#     plt.title(f'Boxplot kolumny {col}')
#     plt.show()

# 4. Model regresji (Eliminacja wsteczna)

X = data.drop('price', axis=1)
y = data['price']


def eliminacja_wsteczna(X, y, p_value_limit=0.05):
    cols = list(X.columns)
    while True:
        model = sm.OLS(y, X).fit()
        p_values = model.pvalues
        max_p_value = p_values.max()
        if max_p_value > p_value_limit:
            excluded_feature = p_values.idxmax()
            cols.remove(excluded_feature)
            X = X[cols]
        else:
            break
    return cols


wybrane_zmienne = eliminacja_wsteczna(X, y)
X = X[wybrane_zmienne]

# 5. Dashboard
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard do prognozowania ceny diamentów"),

    html.Label("Wybierz zmienną:"),
    dcc.Dropdown(
        id='zmienna-wyboru',
        options=[
            {'label': col, 'value': col} for col in set(kolumny_numeryczne + kolumny_kategoryczne + wybrane_zmienne)
        ],
        value=kolumny_numeryczne[0]  # Możesz dostosować wartość początkową
    ),

    dcc.Graph(id='wykres-histogramu'),
    dcc.Graph(id='wykres-skrzynkowy'),
    dcc.Graph(id='wykres-regresji')
])

# Funkcja pomocnicza do rysowania wykresu regresji
def rysuj_wykres_regresji(wybrana_zmienna):
    model = LinearRegression()
    model.fit(X[[wybrana_zmienna]], y)
    y_pred = model.predict(X[[wybrana_zmienna]])

    wykres = px.scatter(x=X[wybrana_zmienna], y=y, title=f'Wykres regresji: Cena vs {wybrana_zmienna}')
    wykres.add_trace(px.line(x=X[wybrana_zmienna], y=y_pred).data[0])

    return wykres

# Funkcje zwrotne do aktualizacji wszystkich wykresów na podstawie jednego pola wyboru
@app.callback(
    Output('wykres-histogramu', 'figure'),
    Output('wykres-skrzynkowy', 'figure'),
    Output('wykres-regresji', 'figure'),
    Input('zmienna-wyboru', 'value')
)
def aktualizuj_wykresy(wybrana_zmienna):
    if wybrana_zmienna in kolumny_numeryczne:
        wykres_histogramu = px.histogram(data, x=wybrana_zmienna, marginal="box", title=f'Wykres histogramu: {wybrana_zmienna}')
        wykres_skrzynkowy = px.box(data, x=wybrana_zmienna, y='price', title=f'Wykres skrzynkowy: Cena vs {wybrana_zmienna}')
        wykres_regresji = rysuj_wykres_regresji(wybrana_zmienna)
    elif wybrana_zmienna in kolumny_kategoryczne:
        wykres_histogramu = px.histogram(data, x=wybrana_zmienna, title=f'Wykres histogramu: {wybrana_zmienna}')
        wykres_skrzynkowy = px.box(data, x=wybrana_zmienna, y='price', title=f'Wykres skrzynkowy: Cena vs {wybrana_zmienna}')
        wykres_regresji = px.scatter()
    elif wybrana_zmienna in wybrane_zmienne:
        wykres_histogramu = px.histogram(data, x=wybrana_zmienna, marginal="box", title=f'Wykres histogramu: {wybrana_zmienna}')
        wykres_skrzynkowy = px.scatter(data, x=wybrana_zmienna, y='price', title=f'Wykres skrzynkowy: Cena vs {wybrana_zmienna}')
        wykres_regresji = rysuj_wykres_regresji(wybrana_zmienna)
    else:
        wykres_histogramu = px.histogram()
        wykres_skrzynkowy = px.scatter()
        wykres_regresji = px.scatter()

    return wykres_histogramu, wykres_skrzynkowy, wykres_regresji

# Uruchomienie aplikacji
if __name__ == '__main__':
    app.run_server(debug=True)
