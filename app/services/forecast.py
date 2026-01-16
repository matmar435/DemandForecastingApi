from typing import Union

import pandas as pd
from datetime import timedelta


def prepare_dataframe(data: Union[list, dict]):
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    return df


def rolling_mean_forecast(df: pd.DataFrame, days: int = 7):
    df["forecast"] = (
        df["quantity"]
        .rolling(window=days)
        .mean()
    )

    last_date = df["date"].max()
    forecast_value = df["forecast"].iloc[-1]

    return {
        "forecast_date": last_date + timedelta(days=1),
        "predicted_quantity": round(float(forecast_value), 2)
    }
