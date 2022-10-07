import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error


@staticmethod
def ARIMA(data, p, d, q):
    # Load data
    df = pd.read_csv(data, header=0, index_col=0, parse_dates=True, squeeze=True)
    # Create ARIMA model
    model = ARIMA(data, order=(p,q,d))
    model_fit = model.fit(disp=0)
    print(model_fit.summary())
    # Plot residual errors
    residuals = pd.DataFrame(model_fit.resid)
    residuals.plot()
    plt.show()
    residuals.plot(kind='kde')
    plt.show()
    print(residuals.describe())

def SARIMA(data, p, d, q, P, D, Q, s):
    # Load data
    df = pd.read_csv(data, header=0, index_col=0, parse_dates=True, squeeze=True)
    # Create SARIMA model
    model = SARIMA(data, order=(p,d,q), seasonal_order=(P,D,Q,s))
    model_fit = model.fit(disp=0)
    print(model_fit.summary())
    # Plot residual errors
    residuals = pd.DataFrame(model_fit.resid)
    residuals.plot()
    plt.show()
    residuals.plot(kind='kde')
    plt.show()
    print(residuals.describe())

