#installed full pycaret version on COM731 environment. always switch to COM731 lower right corner
from pycaret.time_series import *
import pandas as pd
import matplotlib.pyplot as plt
#from fetch_data import fetch_data
# Load your data
data = pd.read_csv('Close_Data.csv', sep=',', encoding='utf-8', index_col=0, parse_dates=True)

# Select BTC-USD column and convert to time series
btc_series = data['BTC-USD'].to_frame()

# Initialize PyCaret time series experiment
setup = TSForecastingExperiment()
setup.setup(data=btc_series, target='BTC-USD', fh=30, fold=3, session_id=123)

# Define the specific models we want to compare
models_to_compare = {
    'arima': {'order': (1,1,1)},  # ARIMA with specified parameters
    'prophet': {},                # Facebook Prophet
    'xgboost': {},                # XGBoost
    'lstm': {'n_hidden': 50}      # LSTM with 50 hidden units
}

# Create and compare our selected models
model_results = []
for model_name, params in models_to_compare.items():
    try:
        model = setup.create_model(model_name, **params)
        model_results.append(model)
    except Exception as e:
        print(f"Failed to create {model_name}: {str(e)}")

# Compare model performance
best_model = setup.compare_models(include=[m for m in model_results if m is not None])

# Create final model (using the best one from our selection)
final_model = setup.create_model(best_model)

# Generate forecasts
forecast = setup.predict_model(final_model)

# Plot results
setup.plot_model(final_model, plot='forecast')

# Display error metrics for all compared models
print("\nModel Comparison Metrics:")
metrics = setup.pull()
print(metrics)

# Additional diagnostics
setup.plot_model(best_model, plot='diagnostics')
setup.plot_model(best_model, plot='insample')

plt.show()
