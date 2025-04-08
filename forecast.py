#installed full pycaret version on COM731 environment. always switch to COM731 lower right corner
from pycaret.time_series import TSForecastingExperiment
import pandas as pd
import matplotlib.pyplot as plt
#import os
#os.environ["PYCARET_CUSTOM_OBJECTIVE"] = "False"  # Disable Dask usage



# Load data - ensure your CSV has 'Date' and 'BTC-USD' columns
try:
    data = pd.read_csv('Close_Data.csv', sep=',', encoding='utf-8', index_col=0, parse_dates=True)
    btc_series = data[['BTC-USD']]  # Double brackets to keep as DataFrame
    
    # Initialize experiment
    exp = TSForecastingExperiment()
    exp.setup(data=btc_series, target='BTC-USD', fh=30, session_id=42)
    
    # Model dictionary with tuned parameters
    models = {
        'arima': {'order': (1,1,1)},
        'prophet': {'seasonality_mode': 'multiplicative'},
        #'xgboost': {'max_depth': 6, 'n_estimators': 100},
        #'lstm_cds': {'n_hidden': 20}  # Using LSTM from NeuralForecast
    }
    
    # Train and compare models
    trained_models = []
    for name, params in models.items():
        try:
            model = exp.create_model(name, **params)
            trained_models.append(model)
            print(f"Successfully trained {name}")
        except Exception as e:
            print(f"Failed to train {name}: {str(e)}")
    
    # Compare model performance
    if trained_models:
        best_model = exp.compare_models(include=trained_models)
        
        # Generate and plot forecast
        forecast = exp.predict_model(best_model)
        exp.plot_model(best_model, plot='forecast')
        
        # Show metrics
        metrics = exp.pull()
        print("\nModel Comparison Metrics:")
        print(metrics)
        
        plt.show()
    else:
        print("No models were successfully trained")

except Exception as e:
    print(f"Error occurred: {str(e)}")