import pandas as pd
from datetime import timedelta


def prepare_dataframe(data: list|[dict]):
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    return df