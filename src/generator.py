import pandas as pd
import numpy as np

def generate_biryani_data():
    # 5 years of daily dates
    dates = pd.date_range(start='2021-01-01', end='2026-05-12', freq='D')
    n = len(dates)
    
    # base price for a plate of kacchi
    base_price = 450 
    
    # factor 1: rice inflation (slow trend)
    trend = np.linspace(0, 150, n) 
    
    # factor 2: weekly seasonality (shonibar/robibar vs shukrobar)
    # prices spike slightly on Fridays (Shukrobar effect)
    seasonality = 20 * np.sin(2 * np.pi * dates.dayofweek / 7)
    
    # factor 3: the "Eid Spike" (exogenous variable)
    # we'll add a massive spike around religious festivals
    eid_effect = np.zeros(n)
    for i, date in enumerate(dates):
        if date.month in [3, 4, 5, 6]: # approximate eid windows
            eid_effect[i] = 50 * np.random.rand()

    # noise (random bazar fluctuations)
    noise = np.random.normal(0, 10, n)
    
    prices = base_price + trend + seasonality + eid_effect + noise
    
    df = pd.DataFrame({'date': dates, 'price': prices})
    df['is_festival'] = (eid_effect > 0).astype(int) # exogenous feature
    return df

# generate and save
df = generate_biryani_data()
df.to_csv('data/biryani_prices.csv', index=False)
print("biryani data generated!")