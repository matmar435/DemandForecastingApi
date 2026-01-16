# Demand Forecasting API

## 📌 Opis projektu

Demand Forecasting API to backendowa aplikacja napisana w **Python (FastAPI)**, której celem jest **prognozowanie zapotrzebowania (popytu) na produkty** na podstawie danych historycznych zamówień.

Projekt symuluje **realny scenariusz biznesowy**:
- dane transakcyjne zapisywane są w bazie danych,
- następnie są agregowane i przetwarzane,
- a wynik (forecast) udostępniany jest przez REST API.

---

## 🛠️ Stack technologiczny

- **Python 3.9**
- **FastAPI** – REST API
- **PostgreSQL** – baza danych
- **SQLAlchemy** – ORM
- **pandas / numpy** – przetwarzanie danych
- **Uvicorn** – serwer ASGI
- **Git / GitHub** – kontrola wersji

---

## 🗂️ Struktura projektu

```
app/
 ├── main.py              # punkt startowy aplikacji
 ├── database.py          # konfiguracja bazy danych
 ├── models/              # modele SQLAlchemy
 ├── schemas/             # schematy Pydantic (request / response)
 ├── crud/                # logika dostępu do danych
 ├── routers/             # endpointy FastAPI
 ├── services/            # logika serwisów
 │    └── forecast.py     # rolling mean forecast
 
```

---

## 📊 Model danych (uproszczony)

### Product
- `id`
- `name`
- `category`
- `created at`

### Order
- `id`
- `product_id`
- `order_date`
- `quantity`
- `price`

---

## 🔍 Funkcjonalności

### ✅ Produkty
- tworzenie produktu
- pobieranie listy produktów

### ✅ Zamówienia
- dodawanie zamówień
- walidacja danych (np. quantity > 0)

### ✅ Analityka
- agregacja zamówień dziennych
- sumowanie ilości per produkt

### ✅ Forecasting
- **baseline demand forecast** oparty o **rolling mean**
- forecast generowany na podstawie danych historycznych
- forecast udostępniony jako endpoint API

---

## 📈 Forecast – jak to działa?

1. Dane zamówień są **agregowane w SQL** (GROUP BY date).
2. Dane trafiają do **pandas DataFrame**.
3. Liczona jest **średnia ruchoma (rolling mean)** z ostatnich N dni.
4. Ostatnia wartość średniej używana jest jako prognoza na **kolejny dzień**.

Jest to **baseline forecast**, który stanowi punkt odniesienia do dalszego rozwoju modeli.

---

## 🌐 Przykładowe endpointy

### Produkty
```
GET    /products
POST   /products
```

### Zamówienia
```
GET    /orders
POST   /orders
```

### Forecast
```
GET /forecast/{product_id}
```

---

## ▶️ Uruchomienie projektu lokalnie

1. Klonowanie repozytorium:
```bash
git clone https://github.com/matmar435/DemandForecastingApi.git
cd demand-forecasting-api
```

2. Utworzenie i aktywacja virtualenv:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Instalacja zależności:
```bash
pip install -r requirements.txt
```

4. Uruchomienie serwera:
```bash
uvicorn app.main:app --reload
```

5. Dokumentacja API (Swagger):
```
http://127.0.0.1:8000/docs
```

---

## 🚀 Możliwe kierunki rozwoju

- weighted moving average
- wykrywanie trendu
- sezonowość (day-of-week)
- forecast na wiele dni
- metryki błędu (MAE, RMSE)
- testy jednostkowe

---

## 👤 Autor