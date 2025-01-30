import sys
sys.path.append("C:\\Users\\jeric\\Desktop\\Joyson_decrypted\\Python script\\GUI_APP\\src")

#import Correction_Factor_Calculation
#import File handling
from Correction_Factor_Calculation import *
from File_handling import *
from Calc_PPM import *
from Plot_Graphs import *
from Low_pass_filter import *
from windspeed_correction import *
from Plot_Draeger import *
from select_distance import *

from datetime import datetime


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
        layout3a = QHBoxLayout()
        layout3b = QHBoxLayout()
        layout3c = QHBoxLayout()
        layout4 = QHBoxLayout()

        #Load folder
        self.load_button = QPushButton('Select File',self)
        self.load_button.clicked.connect(self.load_file)
        self.load_button.setFixedSize(100, 30)
        #self.load_button.setStyleSheet("border: 3px solid black")
        layout2.addWidget(self.load_button)

        self.Load_status = QLabel()
        self.Load_status.setText('Select File')
        #self.Load_status.setAlignment(Qt.AlignCenter)
        self.Load_status.setFixedSize(700,20)
        layout2.addWidget(self.Load_status)

        layout1.addLayout(layout2)

        #display data
        self.CSV_button = QPushButton('Convert to CSV Raw',self)
        self.CSV_button.clicked.connect(self.convert_data)
        self.CSV_button.setFixedSize(200,30)
        #self.CSV_button.setStyleSheet("border: 3px solid black")
        layout2a.addWidget(self.CSV_button, alignment= Qt.AlignCenter)

        self.preprocess_status = QLabel()
        #self.preprocess_status.setAlignment(Qt.AlignCenter)
        self.preprocess_status.setFixedSize(200,20)
        layout2a.addWidget(self.preprocess_status, alignment=Qt.AlignCenter)

        layout1.addLayout(layout2a)

        #Display Distance text
        self.distance_text = QLabel()
        self.distance_text.setText('Select distance from the steering board:')
        layout3.addWidget(self.distance_text)

        #display data
        self.distance_button = QPushButton('select Distance file',self)
        self.distance_button.clicked.connect(self.select_distance_file)
        self.distance_button.setFixedSize(200,30)
        #self.CSV_button.setStyleSheet("border: 3px solid black")
        layout3.addWidget(self.distance_button, alignment= Qt.AlignCenter)
        """
        #select distance from options
        self.distance_options = QComboBox(self)
        self.distance_options.addItems(["200", "250", "300", "350", "400", "450", "500"])
        #self.distance_options.setFixedSize(200,30)
        #self.distance_options.setStyleSheet("border: 3px solid black")
        layout3.addWidget(self.distance_options)
        """       
        layout1.addLayout(layout3, stretch=2)
        """
        #Add distance to the dataframe
        self.distance_button = QPushButton('Add_distance', self)
        self.distance_button.clicked.connect(self.show_distance)
        self.distance_button.setFixedSize(150,30)
        #self.distance_button.setStyleSheet("border: 3px solid black")
        layout1.addWidget(self.distance_button, alignment= Qt.AlignCenter)
"""
        #display PPM_graph button
        self.filter_button = QPushButton('Filter_acetone,ethanol & windspeed', self)
        self.filter_button.clicked.connect(self.filter_acetone_ethanol_windspeed)
        self.filter_button.setFixedSize(150,30)
        #self.Graphs_button.setStyleSheet("border: 3px solid black")
        layout1.addWidget(self.filter_button, alignment= Qt.AlignCenter)

        #Button to correct Windspeed
        self.filter_button = QPushButton('Correct_Windspeed', self)
        self.filter_button.clicked.connect(self.corrected_windspeed)
        self.filter_button.setFixedSize(150,30)
        #self.Graphs_button.setStyleSheet("border: 3px solid black")
        layout1.addWidget(self.filter_button, alignment= Qt.AlignCenter)
        
        #Apply correction, predict PPM & Save
        self.correction_button = QPushButton('Apply Delta_Correction, Predict PPM and Save', self)
        self.correction_button.clicked.connect(self.correction_factor)
        self.correction_button.setFixedSize(250,30)
        #self.correction_button.setStyleSheet("border: 3px solid black")
        layout1.addWidget(self.correction_button, alignment= Qt.AlignCenter)

        #Enter starting Dräger values
        self.draeger_start_text = QLabel()
        self.draeger_start_text.setText('Enter Starting Dräger values:')
        layout3a.addWidget(self.draeger_start_text)

        self.input2 = QLineEdit(self)
        self.input2.setPlaceholderText("Enter value in mg/L")
        self.input2.setFixedSize(150,20)
        layout3a.addWidget(self.input2)

        layout1.addLayout(layout3a)

        #Enter mid Dräger values
        self.draeger_mid_text = QLabel()
        self.draeger_mid_text.setText('Enter Dräger values with time:')
        layout3b.addWidget(self.draeger_mid_text)

        self.input3 = QLineEdit(self)
        self.input3.setPlaceholderText("Enter time in minutes ")
        self.input3.setFixedSize(150,20)
        layout3b.addWidget(self.input3)

        self.input5 = QLineEdit(self)
        self.input5.setPlaceholderText("Enter value in mg/L")
        self.input5.setFixedSize(150,20)
        layout3b.addWidget(self.input5)

        layout1.addLayout(layout3b)

        #Enter end Dräger values
        self.draeger_end_text = QLabel()
        self.draeger_end_text.setText('Enter End Dräger values:')
        layout3c.addWidget(self.draeger_end_text)

        self.input4 = QLineEdit(self)
        self.input4.setPlaceholderText("Enter value in mg/L")
        self.input4.setFixedSize(150,20)
        layout3c.addWidget(self.input4)

        self.draeger_button = QPushButton('Dräger Values', self)
        self.draeger_button.clicked.connect(self.draeger_plot)
        self.draeger_button.setFixedSize(150,30)
        #self.PPM_button.setStyleSheet("border: 3px solid black")
        layout3c.addWidget(self.draeger_button)

        layout1.addLayout(layout3c)

        #display PPM_graph
        self.PPM_button = QPushButton('PPM_graph', self)
        self.PPM_button.clicked.connect(self.show_PPM_graph)
        self.PPM_button.setFixedSize(150,30)
        #self.PPM_button.setStyleSheet("border: 3px solid black")
        layout1.addWidget(self.PPM_button, alignment= Qt.AlignCenter)

        #Display predited PPM
        self.ppm_graph = QLabel(self)
        self.ppm_graph.setAlignment(Qt.AlignCenter)
        layout1.addWidget(self.ppm_graph)

        #display PPM_graph button
        self.Graphs_button = QPushButton('Other_graphs', self)
        self.Graphs_button.clicked.connect(self.save_graphs)
        self.Graphs_button.setFixedSize(150,30)
        #self.Graphs_button.setStyleSheet("border: 3px solid black")
        layout1.addWidget(self.Graphs_button, alignment= Qt.AlignCenter)

        #Display ethanol vs windspeed
        self.ws_graph = QLabel(self)
        #self.ws_graph.setAlignment(Qt.AlignCenter)
        layout4.addWidget(self.ws_graph)

        #Display ethanol vs acetone
        self.ace_graph = QLabel(self)
        #self.ace_graph.setAlignment(Qt.AlignCenter)
        layout4.addWidget(self.ace_graph)

        #Display ethanol vs acetone
        self.co2_graph = QLabel(self)
        #self.co2_graph.setAlignment(Qt.AlignCenter)
        layout4.addWidget(self.co2_graph)

        layout1.addLayout(layout4, stretch=2)

        """        
        #Display predited PPM
        self.ppm_graph = QLabel(self)
        self.ppm_graph.setAlignment(Qt.AlignCenter)
        layout1.addWidget(self.ppm_graph)        
        
        #Display predited PPM
        self.ppm_graph = QLabel(self)
        self.ppm_graph.setAlignment(Qt.AlignCenter)
        layout1.addWidget(self.ppm_graph)
        """
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
            self.Load_status.setText(f'file:{self.folder_path}')
        
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
        try:
            if 'windspeed_corr' in self.df.columns:
                self.df = correction_calculation(self, self.df)
                print('applied correction')
        except:
            print('Do windspeed correction first')

    def select_distance_file(self):
        options = QFileDialog.Options()
        file_filter = "All Files (*)"
        self.distance_file, _ = QFileDialog.getOpenFileName(self, "Select Folder")
        if not self.distance_file:
            QMessageBox.critical(self, "Error", "Please select a distance file first.")
        elif self.distance_file:
            self.df_distance_actual = distance_file(self.distance_file)
            
            self.df = pd.concat([self.data, self.df_distance_actual], axis = 1)

            self.Load_status.setText(f'file:{self.folder_path}')

    def filter_acetone_ethanol_windspeed(self):
      self.df = apply_low_pass_filter(self.df)
      print('Acetone, ethanol windspeed filtered')

    def corrected_windspeed(self):
      self.df = windspeed_corr(self.df)
      print('Windspeed_corrected')

    def draeger_plot(self):
        time1 = 0
        value1 = self.input2.text()
        time2 = self.df.shape[0]
        value2 = self.input4.text()
        time3 = float(self.input3.text()) * 600
        value3 = self.input5.text()

        self.rect_start = draeger_values(time1, value1)
        self.rect_mid = draeger_values(time3, value3)
        self.rect_end = draeger_values(time2, value2)
        #return self.rect_start
        #breakpoint()
        #self.rect_mid = draeger_values(time, value)
        #self.rect_end = draeger_values(time, value)

    #Display PPM graph
    def show_PPM_graph(self):
            df = self.df
            # Ensure necessary columns are present
            if 'Calculated_PPM_Ref_2.3' not in df.columns or 'windspeed' not in df.columns:
                print("Required columns ('PPM' and 'windspeed') are missing from the DataFrame.")
                return
            plt.rcParams.update({'font.size': 10})
            fig, ax = plt.subplots(figsize=(6,3.5))

            # using rc function
            #ax.rcParams.update({'font.size': 10})
            ax.plot(df['PPM_Peak_Ref_2.3'], linewidth=1, label='PPM_Ref_2.3', color='b', marker = '*', markersize = 9)
            ax.plot(df['PPM_Peak_Ref_3'], linewidth=1, label='PPM_Ref_3', color='g', marker = '+', markersize = 9)

            #breakpoint()
            ax.add_patch(self.rect_start)  #rectangular path of dräger
            ax.add_patch(self.rect_mid)
            ax.add_patch(self.rect_end)

            ax.set_ylim(bottom = 0)    
            ax.title.set_text('PPM_2.3, PPM_3 & Windspeed')
            ax.set_ylabel('PPM Calculated', fontsize=9)
            ax.set_xlabel('Samples', fontsize=9)
            xtick_labels = df.index
            step = max(1, len(xtick_labels) // 30)  # Adjusting step size
            ax.set_xticks(xtick_labels[::step])
            ax.set_xticklabels(xtick_labels[::step], rotation=90, fontsize=7)

            #ax2.rcParams.update({'font.size': 10})
            ax2 = ax.twinx()
            ax2.plot(df['windspeed'], color='r', linewidth=1, label='Windspeed')
            ax2.set_ylim(bottom = 0)
            ax2.set_ylabel('Windspeed(m/s)', fontsize=9)
            lines_1, labels_1 = ax.get_legend_handles_labels()
            lines_2, labels_2 = ax2.get_legend_handles_labels()

            lines = lines_1 + lines_2
            labels = labels_1 + labels_2

            ax.legend(lines, labels, fontsize = 6, loc='upper right', bbox_to_anchor=(1.1, 1.1))
            #ax.show()

            # Convert plot to image for display in PyQt widget
            buf = BytesIO()
            plt.savefig(buf, format='png', bbox_inches='tight')

            plt.savefig(self.folder_path + 'PPM.png')
            plt.tight_layout()
            plt.close()
            buf.seek(0)

            pixmap = QPixmap()
            pixmap.loadFromData(buf.getvalue())
            self.ppm_graph.setPixmap(pixmap)
    
    def save_graphs(self):
        df = self.df
        folder_path =self.folder_path
        fig_ws, fig_ace, fig_co2 = plot_other_graphs(df, folder_path)

        # Convert plot to image for display in PyQt widget
        def plt_to_img(fig, widget):
            buf = BytesIO()
            fig.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)

            pixmap = QPixmap()
            pixmap.loadFromData(buf.getvalue())
            widget.setPixmap(pixmap)

        plt_to_img(fig_ws, self.ws_graph)
        plt_to_img(fig_ace, self.ace_graph)
        plt_to_img(fig_co2, self.co2_graph)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Joyson_prediction()
    window.show()
    sys.exit(app.exec_())