import sys
sys.path.append("C:\\Users\\jeric\\Desktop\\Joyson_decrypted\\Python script\\GUI_APP\\src")

#import Correction_Factor_Calculation
#import File handling
from Correction_Factor_Calculation import *
from File_handling import *
from Calc_PPM import *
from Plot_Graphs import *

from datetime import datetime

import joblib


import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout,QHBoxLayout, QWidget, QLineEdit,QPushButton, QListWidget, QFileDialog, QComboBox, QLabel, QMessageBox
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtCore import Qt

from io import BytesIO


import matplotlib.pyplot as plt

class Joyson_prediction(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Joyson Analysis")
        self.setGeometry(200, 200, 600, 600)
        #self.setStyleSheet("border: 4px solid black")
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        #self.setStyleSheet("border: 4px solid black")

        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout2a = QHBoxLayout()
        layout3 = QHBoxLayout()
        #layout4 = QHBoxLayout()

        #Load folder
        self.load_button = QPushButton('Select File',self)
        self.load_button.clicked.connect(self.load_file)
        self.load_button.setFixedSize(100, 30)
        self.load_button.setStyleSheet("border: 3px solid black")
        layout2.addWidget(self.load_button)

        self.Load_status = QLabel()
        self.Load_status.setText('Select File')
        #self.Load_status.setAlignment(Qt.AlignCenter)
        self.Load_status.setFixedSize(100,20)
        layout2.addWidget(self.Load_status)

        layout1.addLayout(layout2)

        #display data
        self.CSV_button = QPushButton('Convert to CSV Raw',self)
        self.CSV_button.clicked.connect(self.convert_data)
        self.CSV_button.setFixedSize(200,30)
        self.CSV_button.setStyleSheet("border: 3px solid black")
        layout2a.addWidget(self.CSV_button, alignment=Qt.AlignCenter)

        self.preprocess_status = QLabel()
        self.preprocess_status.setAlignment(Qt.AlignCenter)
        self.preprocess_status.setFixedSize(200,20)
        layout2a.addWidget(self.preprocess_status, alignment=Qt.AlignCenter)

        layout1.addLayout(layout2a)

        #Display Distance text
        self.distance_text = QLabel()
        self.distance_text.setText('Select distance from the steering board:')
        layout3.addWidget(self.distance_text)

        #select distance from options
        self.distance_options = QComboBox(self)
        self.distance_options.addItems(["200", "250", "300", "350", "400", "450", "500"])
        #self.distance_options.setFixedSize(200,30)
        self.distance_options.setStyleSheet("border: 3px solid black")
        layout3.addWidget(self.distance_options)
        
        layout1.addLayout(layout3, stretch=2)

        #Add distance to the dataframe
        self.distance_button = QPushButton('Add_distance', self)
        self.distance_button.clicked.connect(self.show_distance)
        self.distance_button.setFixedSize(150,30)
        self.distance_button.setStyleSheet("border: 3px solid black")
        layout1.addWidget(self.distance_button, alignment=Qt.AlignCenter)
        
        #Apply correction, predict PPM & Save
        self.correction_button = QPushButton('Apply Ref_2.3 Correction, Predict PPM & Save', self)
        self.correction_button.clicked.connect(self.correction_factor)
        self.correction_button.setFixedSize(250,30)
        self.correction_button.setStyleSheet("border: 3px solid black")
        layout1.addWidget(self.correction_button, alignment=Qt.AlignCenter)


        #display PPM_graph
        self.PPM_button = QPushButton('PPM_graph', self)
        self.PPM_button.clicked.connect(self.show_PPM_graph)
        self.PPM_button.setFixedSize(150,30)
        self.PPM_button.setStyleSheet("border: 3px solid black")
        layout1.addWidget(self.PPM_button, alignment=Qt.AlignCenter)

        #display PPM_graph
        self.Graphs_button = QPushButton('Other_graphs', self)
        self.Graphs_button.clicked.connect(self.save_graphs)
        self.Graphs_button.setFixedSize(150,30)
        self.Graphs_button.setStyleSheet("border: 3px solid black")
        layout1.addWidget(self.Graphs_button, alignment=Qt.AlignCenter)


        #Display predited PPM
        self.ppm_graph = QLabel(self)
        self.ppm_graph.setAlignment(Qt.AlignCenter)
        layout1.addWidget(self.ppm_graph)
        
        """
        #Field to enter a User defined New tweet
        self.prompt = QLineEdit(self)
        self.prompt.setPlaceholderText("Enter a Tweet")
        self.prompt.setStyleSheet("border: 3px solid black")
        layout1.addWidget(self.prompt)
        """

        #central_widget.setStyleSheet()
        central_widget.setLayout(layout1)
        

    def load_file(self):
        options = QFileDialog.Options()
        self.folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if not self.folder_path:
            QMessageBox.critical(self, "Error", "Please select a folder first.")
        elif self.folder_path:
            self.data = load_data(self.folder_path)
            self.Load_status.setText('File Selected')
        
    def convert_data(self):
        self.preprocess_status.setText('Conversion in Progress....')
        convert_and_save(self, self.data)
        self.preprocess_status.setText('Conversion Done')
        #print(self.data)

    def show_distance(self):
        self.selected_dist =self.distance_options.currentText()
        self.df = add_distance(self.data, self.selected_dist)
        print('Distance Added')

    def correction_factor(self):
        self.df = correction_calculation(self, self.df)
        print('applied correction')

    #Display wordcloud
    def show_PPM_graph(self):
            df = self.df
            # Ensure necessary columns are present
            if 'Calculated_PPM' not in df.columns or 'windspeed' not in df.columns:
                print("Required columns ('PPM' and 'windspeed') are missing from the DataFrame.")
                return

            fig, ax = plt.subplots(figsize=(8,6))
            #markerstyles = ['v','o','+','*','.']
            ax.plot(df['Calculated_PPM'], linewidth=0.5, label='PPM', color='b')    
            ax.title.set_text('PPM & Windspeed')
            ax.set_ylabel('PPM predicted')
            ax.set_xlabel('Samples')
            ax.set_xticks(df.index)

            ax2 = ax.twinx()
            ax2.plot(df['windspeed'], color='r', linewidth=0.5, label='Windspeed')
            ax2.set_ylabel('Windspeed(m/s)')
            lines_1, labels_1 = ax.get_legend_handles_labels()
            lines_2, labels_2 = ax2.get_legend_handles_labels()

            lines = lines_1 + lines_2
            labels = labels_1 + labels_2

            ax.legend(lines, labels, loc='upper center')
            #ax.show()

            """
            # Plotting
            plt.figure(figsize=(8, 5))
            plt.plot(df['Windspeed_Max'], df['PPM'], marker='o', linestyle='-', color='b', label='PPM vs Windspeed_Max')
            plt.title('PPM vs Windspeed_Max')
            plt.xlabel('Windspeed_Max')
            plt.ylabel('PPM')
            plt.grid(True)
            plt.legend()
            plt.tight_layout()
            """
            # Convert plot to image for display in PyQt widget
            buf = BytesIO()
            plt.savefig(buf, format='png')

            plt.savefig(self.folder_path + 'PPM.png')

            plt.close()
            buf.seek(0)

            pixmap = QPixmap()
            pixmap.loadFromData(buf.getvalue())
            self.ppm_graph.setPixmap(pixmap)
    
    def save_graphs(self):
        df = self.df
        folder_path =self.folder_path
        plot_other_graphs(df, folder_path)

    def save_model(self):
        model = self.model
        date = datetime.now()
        model_name = re.sub(r'[(){}<>]', '', str(model))
        file_name = f'C://Users//Vivupadi//Desktop//Sentiment Analysis//models//{(model_name)}_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.pkl'
        #with open(file_name, 'wb') as f:
        joblib.dump(model, file_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Joyson_prediction()
    window.show()
    sys.exit(app.exec_())