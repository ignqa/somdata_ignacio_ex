# SomData - Ignacio Gazquez Exercise
## Exercise goal
Implement a Django app doing the next tasks:
1. It must obtain every minute the information coming from https://api.bittrex.com/v3/markets/BTC-USDT/summary.
2. Displays in a graph the values for "low" and "high" fields (abscissa axis must represent the "updatedAt" values).
## Setup
1. Run `pip install -r requirements.txt`
2. Run `python manage.py runserver 8000`. If you preferred to install the requirements into a virtual environment, then
execute `{venv_name_path}/bin/python manage.py runserver 8000`
## URLs
1. Index: `http://localhost:8000`
2. Administration: `http://localhost:8000/admin`.
    - User: `admin`
    - Password: `admin`