from skforecast.ForecasterAutoreg import ForecasterAutoreg
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

# load our simulated kacchi data
df = pd.read_csv('data/biryani_prices.csv', parse_dates=['date'])
df = df.set_index('date')

# the "sleeper" skill: using exogenous variables (is_festival)
forecaster = ForecasterAutoreg(
    regressor = RandomForestRegressor(random_state=123),
    lags      = 7 # look at the last week to predict tomorrow
)

# fit the model
forecaster.fit(y=df['price'], last_window=df['price'].iloc[-7:])
print("model is ready to predict kacchi prices!")