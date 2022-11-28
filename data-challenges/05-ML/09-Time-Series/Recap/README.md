# Recap
Let's correct the flashcards of the day below together with your teacher!


#### Q): List some advantages of using autoregressive models like ARIMA over conventional ML models for Time Series
<details>
    <summary>Answer</summary>

- Only one single ARIMA model is required to forecast _any_ time horizon ahead.
- Indeed, they model the **recursive** behavior of the data, forecasting one data point after the other
- You can compute a 95% confidence interval on your forecasts

</details>

&nbsp;
&nbsp;

#### Q): Describe what does a stationary time series look like, in one sentence? (plain English)
<details>
    <summary>Answer</summary>

"Wherever you look at it, your conclusions about its properties should be roughly the same."

</details>
&nbsp;
&nbsp;

#### Q): Give 3 statistical properties of stationary time series that remain constant over time ?
<details>
    <summary>Answer</summary>

Constant mean, constant variance, and constant autocorrelation

</details>
&nbsp;
&nbsp;

#### Q): What is the name of the statistical test used to check for stationarity?
<details>
    <summary>Answer</summary>

- Augmented Dickey Fuller - ADF Tests
- Consider the time series stationary when its `p-value` is below 0.05

</details>
&nbsp;
&nbsp;

#### Q): What are the 3 fundamental steps to model a time series?
<details>
    <summary>Answer</summary>

- First, stationarize your time series
- Then, forecast the stationary TS by prolongating its constant statistical properties over time. (AR/MA modeling is one way of doing so)
- Finally, transform back to the initial time series

</details>

&nbsp;
&nbsp;

#### Q): What is the fundamental reason we need to stationarize a time series before modeling it?
<details>
    <summary>Answer</summary>

- As its statistical properties are by definition **constant over time**, we can safely prolongate them in the future!
- We are never safe from unexpected changes (black swans), but we can quantify probabilities that they will stay constant (uncertainty intervals)
- AR/MA modeling is one way to do so. Many other methods exists. 

</details>
&nbsp;
&nbsp;

#### Q): Quote 4 methods to stationarize a time series?
<details>
    <summary>Answer</summary>

- Detrending (ex: taking the log, removing linear increase, etc...)
- Deseasonalizing (ex: using statsmodels `seasonal_decompose`)
- Differencing (ex: $y(t) - y(t-1)$)
- Seasonal differencing (ex: $y(t) - y(t-12)$)

</details>
&nbsp;
&nbsp;

#### Q): Name two methods of seasonal decomposition?
<details>
    <summary>Answer</summary>

- Additive Decomposition (y = Trend + Seasonal + Residuals)
- Multiplicative Decomposition (y = Trend * Seasonal * Residuals)

</details>
&nbsp;
&nbsp;

#### Q): What does ARIMA stand for?
<details>
    <summary>Answer</summary>

ARIMA stands for Auto-Regressive Integrated Moving-Average
- Step 1: **stationarize** the TS using differencing
- Step 2: **model** the stationary TS as the combination of an AR + MA processes
- Step 3: **extend** the stationary TS in the future
- Step 4: integrate back the differenced time-series to get the final forecast

</details>
&nbsp;
&nbsp;

#### Q): What is an AR process? How could you characterize its behavior? Give one example.
<details>
    <summary>Answer</summary>

- AR stands for "Auto-Regressive"
- A process whose values are a direct linear combinations of its past values
- In such processes, a one time "shock" will propagate far in the future
- e.g. the atmospheric CO2 concentration (when an giant forest-fire suddenly increases it, CO2 concentration is raised for decades)

</details>
&nbsp;
&nbsp;

#### Q): What is a MA process? How could you characterize its behavior? Give one example.
<details>
    <summary>Answer</summary>

- MA stands for "Moving-Average"
- A process whose values are a direct linear combinations of its past changes
- In such processes, any "shock" will have a limited time effect (rebound/elastic behavior)
- e.g. a country's GDP growth in % (when a pandemic shock lowers it to -10%, it may bounce back to +5% the following year)

</details>
&nbsp;
&nbsp;

#### Q): How many hyper-parameters do you have to set for ARIMA? For SARIMA?
<details>
    <summary>Answer</summary>

- 3 for ARIMA(p,d,q)
- 7 for SARIMA(p,d,q, P,D,Q, S)

</details>
&nbsp;
&nbsp;

#### Q): How do you choose for ARIMA hyperparameters?
<details>
    <summary>Answer</summary>

- Diff (d): minimum number of differences before you achieve stationarity
- AR term numbers (p): number of non-null terms in PACF plots of stationary TS
- MA term numbers (p): number of non-null terms in ACF plots of stationary TS

</details>
&nbsp;
&nbsp;

#### Q): What do ACF and PACF measure?
<details>
    <summary>Answer</summary>

- ACF: Measure of the **simple correlation coefs** between $Y(t)$ and each lagged features $Y(t-i)$
- PACF: Measure of the **partial correlation coefs** between $Y(t)$ and each lagged features $Y(t-i)$

</details>
&nbsp;
&nbsp;
