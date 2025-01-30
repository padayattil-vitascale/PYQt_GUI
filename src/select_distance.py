import numpy as np
import pandas as pd

def distance_file(file):

    df = pd.read_csv(file)

    # Create finer time intervals (110 steps)
    finer_time = np.arange(df["Timestamp|ms"].iloc[0], df["Timestamp|ms"].iloc[-1] + 90, 90)

    # Create a new DataFrame with finer intervals
    finer_df = pd.DataFrame({"Finer_Time": finer_time})

    # Use the pandas merge_asof function to fill values for finer intervals
    finer_df["Distance"] = pd.merge_asof(
        finer_df, df, left_on="Finer_Time", right_on="Timestamp|ms", direction="backward"
    )["HeadPositionDistance|m"]
    finer_df["Distance"] = (finer_df["Distance"] - 0.096)*1000            #Deviation of 96mm between mouth and Joyson camera distance contact convert in mm
    #finer_df["shifted_Distance"] = finer_df["Distance"].shift(-54)
    finer_df["shifted_Distance"] = finer_df["Distance"].shift(54).interpolate()

    print("Distance added")

    return finer_df