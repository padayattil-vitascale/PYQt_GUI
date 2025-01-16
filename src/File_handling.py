import pandas as pd
import os
import sys


sys.path.append("C:\\Users\\jeric\\Desktop\\Joyson_decrypted\\Python script\\GUI_APP\\src")

import Correction_Factor_Calculation
import Calc_PPM
import Low_pass_filter

from PyQt5.QtWidgets import QFileDialog, QMessageBox


def load_data(folder_path):
    if folder_path:
        DF = pd.DataFrame()  # Empty dataframe to merge all the files
        for file_name in sorted(os.listdir(folder_path)):
            if file_name.endswith(".csv"):
                file = os.path.join(folder_path, file_name)
                # Load the data from the selected Excel file
                df = pd.read_csv(file, sep = '\t')
                df = df.iloc[:,0:11]

                DF = DF.append(df, ignore_index=True)
    return DF
    #file_label.config(text="Selected Folder: " + folder_path)


def convert_and_save(parent, DF):
    try:
        # Save the results to an Excel file
        options = QFileDialog.Options()
        result_file_path, _ = QFileDialog.getSaveFileName(parent, "Save File", "", "Excel files (*.xlsx);;All Files (*)", options=options)
        
        if result_file_path:
            DF.to_excel(result_file_path, index= False)
            QMessageBox.information(parent, "Success", "Results saved to " + result_file_path)
    except:
        print('File maynot be selected')

def add_distance(df, dist):
    try:
        df['Distance'] = dist
        df['Distance'] = df['Distance'].astype(int)
        return df
    except:
        print('File probably not selected')


def correction_calculation(parent, DF):
    # Apply function across all rows and store result in a new column 'Max'
    DF['Max'] = [Correction_Factor_Calculation.compute_max_rolling(DF['filtered_ethanol'], i, window_size = 75) for i in range(len(DF))]     #Set the rolling window to selec the MAx out of last 70 samples
    
    DF['Windspeed_max_filtered'] = [Correction_Factor_Calculation.compute_max_rolling(DF['filtered_windspeed'], i, window_size = 42) for i in range(len(DF))]     #Set the rolling window to selec the MAx out of last 35 samples
    
    DF['Min'] = DF['filtered_ethanol']
    DF['Old_delta'] = DF['Max'] - DF['Min']

    DF['Max_Deviation_Ref_2.3'] = DF['Max'] - 2.3
    DF['Max_Deviation_Ref_3'] = DF['Max'] - 3
    DF = Correction_Factor_Calculation.Calc_coeff_2_3(DF)
    DF = Correction_Factor_Calculation.Calc_coeff_3(DF)
    DF = Calc_PPM.predict_ppm_on_distance(DF)               #PPM calculation for both references
    DF['PPM_Peak_Ref_2.3'] = [Correction_Factor_Calculation.compute_peak(DF['Calculated_PPM_Ref_2.3'], DF['New_Delta_Ref_2.3'], DF['Windspeed_max_filtered'], i, window_size = 25) for i in range(len(DF))]
    DF['PPM_Peak_Ref_3'] = [Correction_Factor_Calculation.compute_peak(DF['Calculated_PPM_Ref_3'], DF['New_Delta_Ref_3'], DF['Windspeed_max_filtered'], i, window_size = 25) for i in range(len(DF))]
    #breakpoint()

    # Save the results to an Excel file
    options = QFileDialog.Options()
    result_file_path, _ = QFileDialog.getSaveFileName(parent, "Save File", "", "Excel files (*.xlsx);;All Files (*)", options=options)
    
    if result_file_path:
        DF.to_excel(result_file_path, index= False)
        QMessageBox.information(parent, "Success", "Results saved to " + result_file_path)

    return DF


def apply_low_pass_filter(df):
    df['filtered_Acethone'] = Low_pass_filter.low_pass_filtered(df['Acethone'])
    df['filtered_windspeed'] = Low_pass_filter.low_pass_filtered(df['windspeed'])
    df['filtered_ethanol'] = Low_pass_filter.low_pass_filtered(df['Ethanol'])
    return df