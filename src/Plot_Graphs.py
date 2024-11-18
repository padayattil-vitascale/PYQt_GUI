##Plot and & save other graphs
import os
import matplotlib.pyplot as plt


def plot_other_graphs(df, folder_path):
            fig, ax = plt.subplots(figsize=(8,6))
            #markerstyles = ['v','o','+','*','.']
            ax.plot(df['Ethanol'], linewidth=0.5, label='Ethanol', color='b')    
            ax.title.set_text('Ethanol & Windspeed')
            ax.set_ylabel('Ethanol')
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

            plt.savefig(os.path.join(folder_path, 'Ethanol VS Windspeed.png'))