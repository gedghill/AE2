import pandas as pd
from pycaret.time_series import *
import matplotlib.pyplot as plt
from fetch_data import fetch_data

df = fetch_data()
# Load your data
# Assume your dataframe is already loaded as 'df' with a 'Close' column
# Example: df = pd.read_csv('BTC-USD.csv', index_col='Date', parse_dates=True)

# Data Preparation
# Ensure the index is DatetimeIndex and the data is sorted
df.index = pd.to_datetime(df.index)
df = df.sort_index()

# Handle missing values if any
#df = df.fillna(df.mean())

# Set up PyCaret environment
s = setup(data=df['Close'], 
          fh=30,  # Forecast horizon
          session_id=123,
          fold_strategy='expanding',
          fold_spans="adaptive",
          numeric_imputation_target = 'drift')

# Model Training and Comparison
# Create models
prophet = create_model('prophet')
arima = create_model('arima')

# Tune models (optional, but recommended)
tuned_prophet = tune_model(prophet)
tuned_arima = tune_model(arima)

# Compare models
compare_models(include=['prophet', 'arima'])

# Predictions
future_dates = pd.date_range(df.index[-1], periods=30, freq='D')

prophet_predictions = predict_model(tuned_prophet, fh=30)
arima_predictions = predict_model(tuned_arima, fh=30)

# Plotting
# Prophet Plot
plt.figure(figsize=(12, 6))
plot_model(tuned_prophet, plot='forecast')
plt.title('Prophet Forecast')
plt.show()

# ARIMA Plot
plt.figure(figsize=(12, 6))
plot_model(tuned_arima, plot='forecast')
plt.title('ARIMA Forecast')
plt.show()