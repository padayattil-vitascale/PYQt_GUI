import pandas as pd
import os


def load_data(file_path):
    if file_path:
        DF = pd.DataFrame()  # Empty dataframe to merge all the files
        for file_name in sorted(os.listdir(file_path)):
            if file_name.endswith(".csv"):
                file = os.path.join(file_path, file_name)
                # Load the data from the selected Excel file
                df = pd.read_csv(file, sep = '\t')
                df = df.iloc[:,0:11]

                DF = DF.append(df, ignore_index=True)
    return DF
    #file_label.config(text="Selected Folder: " + folder_path)



def convert_file():
    if not folder_path:
        messagebox.showerror("Error", "Please select a folder first.")
        return

    global DF
    DF = pd.DataFrame()  # Empty dataframe to merge all the files
    for file_name in sorted(os.listdir(folder_path)):
        if file_name.endswith(".csv"):
            file = os.path.join(folder_path, file_name)
            # Load the data from the selected Excel file
            df = pd.read_csv(file, sep = '\t')
            df = df.iloc[:,0:11]

            DF = DF.append(df, ignore_index=True)

    # Save the results to an Excel file
    result_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    
    if result_file_path:
        DF.to_excel(result_file_path, index= False)
        messagebox.showinfo("Success", "Results saved to " + result_file_path)