import pandas as pd
import numpy as np

#Function to calculate

def Cal_New_delta_2_3(row, coeff_2_3):
    new_delta = row['Old_delta'] - (row['Max_Deviation_Ref_2.3'] * coeff_2_3)
    return new_delta, coeff_2_3

def Calc_coeff_2_3(df):
    def apply_cal(row):
        if (row['Distance'] == 200) and (row['Max_Deviation_Ref_2.3'] > 0.05 and (row['Max_Deviation_Ref_2.3'] < 0.3)):
            return Cal_New_delta_2_3(row, 0.85)
        elif (row['Distance'] == 200) and (row['Max_Deviation_Ref_2.3'] > 0.05 and (row['Max_Deviation_Ref_2.3'] > 0.3)):
            return Cal_New_delta_2_3(row, 0.75)
        elif (row['Distance'] == 200) and ((row['Max_Deviation_Ref_2.3'] < -0.05) and (row['Max_Deviation_Ref_2.3'] > -0.3)):
            return Cal_New_delta_2_3(row, 0.65)
        elif (row['Distance'] == 200) and ((row['Max_Deviation_Ref_2.3'] < -0.05) and (row['Max_Deviation_Ref_2.3'] < -0.3)):
            return Cal_New_delta_2_3(row, 0.75)
        elif (row['Distance'] == 250) and (row['Max_Deviation_Ref_2.3'] > 0.05 and (row['Max_Deviation_Ref_2.3'] < 0.3)):
            return Cal_New_delta_2_3(row, 0.85)
        elif (row['Distance'] == 250) and (row['Max_Deviation_Ref_2.3'] > 0.05 and (row['Max_Deviation_Ref_2.3'] > 0.3)):
            return Cal_New_delta_2_3(row, 0.75)
        elif (row['Distance'] == 250) and ((row['Max_Deviation_Ref_2.3'] < -0.05) and (row['Max_Deviation_Ref_2.3'] > -0.3)):
            return Cal_New_delta_2_3(row, 0.65)
        elif (row['Distance'] == 250) and ((row['Max_Deviation_Ref_2.3'] < -0.05) and (row['Max_Deviation_Ref_2.3'] < -0.3)):
            return Cal_New_delta_2_3(row, 0.75)
        elif (row['Distance'] == 300) and (row['Max_Deviation_Ref_2.3'] > 0.05 and (row['Max_Deviation_Ref_2.3'] < 0.3)):
            return Cal_New_delta_2_3(row, 0.85)
        elif (row['Distance'] == 300) and (row['Max_Deviation_Ref_2.3'] > 0.05 and (row['Max_Deviation_Ref_2.3'] > 0.3)):
            return Cal_New_delta_2_3(row, 0.7)
        elif (row['Distance'] == 300) and ((row['Max_Deviation_Ref_2.3'] < -0.05) and (row['Max_Deviation_Ref_2.3'] > -0.3)):
            return Cal_New_delta_2_3(row, 0.65)
        elif (row['Distance'] == 300) and ((row['Max_Deviation_Ref_2.3'] < -0.05) and (row['Max_Deviation_Ref_2.3'] < -0.3)):
            return Cal_New_delta_2_3(row, 0.7)
        elif (row['Distance'] == 350) and (row['Max_Deviation_Ref_2.3'] > 0.05 and (row['Max_Deviation_Ref_2.3'] < 0.3)):
            return Cal_New_delta_2_3(row, 0.85)
        elif (row['Distance'] == 350) and (row['Max_Deviation_Ref_2.3'] > 0.05 and (row['Max_Deviation_Ref_2.3'] > 0.3)):
            return Cal_New_delta_2_3(row, 0.7)
        elif (row['Distance'] == 350) and ((row['Max_Deviation_Ref_2.3'] < -0.05) and (row['Max_Deviation_Ref_2.3'] > -0.3)):
            return Cal_New_delta_2_3(row, 0.65)
        elif (row['Distance'] == 350) and ((row['Max_Deviation_Ref_2.3'] < -0.05) and (row['Max_Deviation_Ref_2.3'] < -0.3)):
            return Cal_New_delta_2_3(row, 0.7)
        elif (row['Distance'] == 400) and (row['Max_Deviation_Ref_2.3'] > 0.05 and (row['Max_Deviation_Ref_2.3'] < 0.3)):
            return Cal_New_delta_2_3(row, 0.75)
        elif (row['Distance'] == 400) and (row['Max_Deviation_Ref_2.3'] > 0.05 and (row['Max_Deviation_Ref_2.3'] > 0.3)):
            return Cal_New_delta_2_3(row, 0.6)
        elif (row['Distance'] == 400) and ((row['Max_Deviation_Ref_2.3'] < -0.05) and (row['Max_Deviation_Ref_2.3'] > -0.3)):
            return Cal_New_delta_2_3(row, 0.5)
        elif (row['Distance'] == 400) and ((row['Max_Deviation_Ref_2.3'] < -0.05) and (row['Max_Deviation_Ref_2.3'] < -0.3)):
            return Cal_New_delta_2_3(row, 0.6)
        elif (row['Distance'] == 450) and (row['Max_Deviation_Ref_2.3'] > 0.05 and (row['Max_Deviation_Ref_2.3'] < 0.3)):
            return Cal_New_delta_2_3(row, 0.75)
        elif (row['Distance'] == 450) and (row['Max_Deviation_Ref_2.3'] > 0.05 and (row['Max_Deviation_Ref_2.3'] > 0.3)):
            return Cal_New_delta_2_3(row, 0.6)
        elif (row['Distance'] == 450) and ((row['Max_Deviation_Ref_2.3'] < -0.05) and (row['Max_Deviation_Ref_2.3'] > -0.3)):
            return Cal_New_delta_2_3(row, 0.5)
        elif (row['Distance'] == 450) and ((row['Max_Deviation_Ref_2.3'] < -0.05) and (row['Max_Deviation_Ref_2.3'] < -0.3)):
            return Cal_New_delta_2_3(row, 0.6)
        elif (row['Distance'] == 500) and (row['Max_Deviation_Ref_2.3'] > 0.05 and (row['Max_Deviation_Ref_2.3'] < 0.3)):
            return Cal_New_delta_2_3(row, 0.65)
        elif (row['Distance'] == 500) and (row['Max_Deviation_Ref_2.3'] > 0.05 and (row['Max_Deviation_Ref_2.3'] > 0.3)):
            return Cal_New_delta_2_3(row, 0.5)
        elif (row['Distance'] == 500) and ((row['Max_Deviation_Ref_2.3'] < -0.05) and (row['Max_Deviation_Ref_2.3'] > -0.3)):
            return Cal_New_delta_2_3(row, 0.5)
        elif (row['Distance'] == 500) and ((row['Max_Deviation_Ref_2.3'] < -0.05) and (row['Max_Deviation_Ref_2.3'] < -0.3)):
            return Cal_New_delta_2_3(row, 0.5)
        else:
            return Cal_New_delta_2_3(row, 1)

    df['New_Delta_Ref_2.3'], df['Coeff_2.3'] = zip(*df.apply(apply_cal, axis=1))
    return df

#Function to calculate New_Delta based on reference of Ethanol_Max of 3 V

def Cal_New_delta_3(row, coeff_3):
    new_delta = row['Old_delta'] - (row['Max_Deviation_Ref_3'] * coeff_3)
    return new_delta, coeff_3

def Calc_coeff_3(df):
    def apply_cal(row):
        if (row['Distance'] == 200) and (row['Max_Deviation_Ref_3'] > 0.1 and (row['Max_Deviation_Ref_3'] < 0.3)):
            return Cal_New_delta_3(row, 0.85)
        elif (row['Distance'] == 200) and (row['Max_Deviation_Ref_3'] > 0.1 and (row['Max_Deviation_Ref_3'] > 0.3)):
            return Cal_New_delta_3(row, 0.75)
        elif (row['Distance'] == 200) and ((row['Max_Deviation_Ref_3'] < -0.1) and (row['Max_Deviation_Ref_3'] > -0.3)):
            return Cal_New_delta_3(row, 0.65)
        elif (row['Distance'] == 200) and ((row['Max_Deviation_Ref_3'] < -0.1) and (row['Max_Deviation_Ref_3'] < -0.3)):
            return Cal_New_delta_3(row, 0.75)
        elif (row['Distance'] == 250) and (row['Max_Deviation_Ref_3'] > 0.1 and (row['Max_Deviation_Ref_3'] < 0.3)):
            return Cal_New_delta_3(row, 0.85)
        elif (row['Distance'] == 250) and (row['Max_Deviation_Ref_3'] > 0.1 and (row['Max_Deviation_Ref_3'] > 0.3)):
            return Cal_New_delta_3(row, 0.75)
        elif (row['Distance'] == 250) and ((row['Max_Deviation_Ref_3'] < -0.1) and (row['Max_Deviation_Ref_3'] > -0.3)):
            return Cal_New_delta_3(row, 0.65)
        elif (row['Distance'] == 250) and ((row['Max_Deviation_Ref_3'] < -0.1) and (row['Max_Deviation_Ref_3'] < -0.3)):
            return Cal_New_delta_3(row, 0.75)
        elif (row['Distance'] == 300) and (row['Max_Deviation_Ref_3'] > 0.1 and (row['Max_Deviation_Ref_3'] < 0.3)):
            return Cal_New_delta_3(row, 0.85)
        elif (row['Distance'] == 300) and (row['Max_Deviation_Ref_3'] > 0.1 and (row['Max_Deviation_Ref_3'] > 0.3)):
            return Cal_New_delta_3(row, 0.7)
        elif (row['Distance'] == 300) and ((row['Max_Deviation_Ref_3'] < -0.1) and (row['Max_Deviation_Ref_3'] > -0.3)):
            return Cal_New_delta_3(row, 0.65)
        elif (row['Distance'] == 300) and ((row['Max_Deviation_Ref_3'] < -0.1) and (row['Max_Deviation_Ref_3'] < -0.3)):
            return Cal_New_delta_3(row, 0.7)
        elif (row['Distance'] == 350) and (row['Max_Deviation_Ref_3'] > 0.1 and (row['Max_Deviation_Ref_3'] < 0.3)):
            return Cal_New_delta_3(row, 0.85)
        elif (row['Distance'] == 350) and (row['Max_Deviation_Ref_3'] > 0.1 and (row['Max_Deviation_Ref_3'] > 0.3)):
            return Cal_New_delta_3(row, 0.7)
        elif (row['Distance'] == 350) and ((row['Max_Deviation_Ref_3'] < -0.1) and (row['Max_Deviation_Ref_3'] > -0.3)):
            return Cal_New_delta_3(row, 0.65)
        elif (row['Distance'] == 350) and ((row['Max_Deviation_Ref_3'] < -0.1) and (row['Max_Deviation_Ref_3'] < -0.3)):
            return Cal_New_delta_3(row, 0.7)
        elif (row['Distance'] == 400) and (row['Max_Deviation_Ref_3'] > 0.1 and (row['Max_Deviation_Ref_3'] < 0.3)):
            return Cal_New_delta_3(row, 0.75)
        elif (row['Distance'] == 400) and (row['Max_Deviation_Ref_3'] > 0.1 and (row['Max_Deviation_Ref_3'] > 0.3)):
            return Cal_New_delta_3(row, 0.6)
        elif (row['Distance'] == 400) and ((row['Max_Deviation_Ref_3'] < -0.1) and (row['Max_Deviation_Ref_3'] > -0.3)):
            return Cal_New_delta_3(row, 0.5)
        elif (row['Distance'] == 400) and ((row['Max_Deviation_Ref_3'] < -0.1) and (row['Max_Deviation_Ref_3'] < -0.3)):
            return Cal_New_delta_3(row, 0.6)
        elif (row['Distance'] == 450) and (row['Max_Deviation_Ref_3'] > 0.1 and (row['Max_Deviation_Ref_3'] < 0.3)):
            return Cal_New_delta_3(row, 0.75)
        elif (row['Distance'] == 450) and (row['Max_Deviation_Ref_3'] > 0.1 and (row['Max_Deviation_Ref_3'] > 0.3)):
            return Cal_New_delta_3(row, 0.6)
        elif (row['Distance'] == 450) and ((row['Max_Deviation_Ref_3'] < -0.1) and (row['Max_Deviation_Ref_3'] > -0.3)):
            return Cal_New_delta_3(row, 0.5)
        elif (row['Distance'] == 450) and ((row['Max_Deviation_Ref_3'] < -0.1) and (row['Max_Deviation_Ref_3'] < -0.3)):
            return Cal_New_delta_3(row, 0.6)
        elif (row['Distance'] == 500) and (row['Max_Deviation_Ref_3'] > 0.1 and (row['Max_Deviation_Ref_3'] < 0.3)):
            return Cal_New_delta_3(row, 0.65)
        elif (row['Distance'] == 500) and (row['Max_Deviation_Ref_3'] > 0.1 and (row['Max_Deviation_Ref_3'] > 0.3)):
            return Cal_New_delta_3(row, 0.5)
        elif (row['Distance'] == 500) and ((row['Max_Deviation_Ref_3'] < -0.1) and (row['Max_Deviation_Ref_3'] > -0.3)):
            return Cal_New_delta_3(row, 0.5)
        elif (row['Distance'] == 500) and ((row['Max_Deviation_Ref_3'] < -0.1) and (row['Max_Deviation_Ref_3'] < -0.3)):
            return Cal_New_delta_3(row, 0.5)
        else:
            return Cal_New_delta_3(row, 1)

    df['New_Delta_Ref_3'], df['Coeff_3'] = zip(*df.apply(apply_cal, axis=1))
    return df

# Function to compute max within a window of 100 previous rows
def compute_max_rolling(series, current_index, window_size):
    start_index = max(0, current_index - window_size)  # Ensure index doesn't go negative
    return series[start_index:current_index].max()

def compute_peak(series, delta_series, windspeed_series, current_index, window_size):
    start_index = max(0, current_index - window_size)
    # Define the end index of the window
    end_index = min(len(series), current_index + window_size)
    # Compute the maximum value within the window
    max_temp = series[start_index:end_index].max()
    # Get the current value
    current_value = series[current_index]
    delta_condition_value = delta_series[current_index]
    windspeed_condition_value = windspeed_series[current_index]
    # Check if the current value is equal to the maximum in the window
    return current_value if (current_value == max_temp) and (delta_condition_value >= 0) and (windspeed_condition_value >= 0.01) else np.nan