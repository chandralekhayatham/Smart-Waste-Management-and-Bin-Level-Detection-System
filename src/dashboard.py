import pandas as pd
from datetime import datetime

def save_data(distance, fill_percentage, status):

    data = {
        "Timestamp": [datetime.now()],
        "Distance": [distance],
        "FillPercentage": [fill_percentage],
        "Status": [status]
    }

    df = pd.DataFrame(data)

    df.to_csv(
        "data/bin_data.csv",
        mode="a",
        index=False,
        header=False
    )