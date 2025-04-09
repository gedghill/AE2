#Define function to get BTC forecast using FB Prophet model
import pandas as pd
from pycaret.time_series import *
import matplotlib.pyplot as plt
from fetch_data import fetch_data
data = fetch_data()
def get_btc_prophet(data):
    try:
      #create series with just BTC close price
      btc = data.loc[:,'BTC-USD']
      # Set up PyCaret environment
      s = setup(data=btc, 
            target = 'BTC-USD',
            #transform_target='log',
            fh=30,  # Forecast horizon
            session_id=123,
            fold_strategy='expanding',
            seasonal_period='D',
            #fold_spans="adaptive",
            numeric_imputation_target = 'drift')
      prophet = create_model('prophet')
      tuned_prophet = tune_model(prophet)
      # Predictions
      final_prophet = finalize_model(tuned_prophet)
      prophet_predictions = predict_model(final_prophet)
      #Plot prophet model forecast
      plot_model(final_prophet, plot='forecast')
      return prophet, plt.gcf()
    except Exception as e:
       print(f"An error occurred: {e}")
       return None, None

if __name__ == "__main__":
    data = fetch_data()
    trained_model, plot = get_btc_prophet(data)
    plt.show()
    if trained_model is not None and plot is not None:
        save_model(trained_model, 'trained_model')
        plt.show()
    else:
        print("Model training or plotting failed")
        