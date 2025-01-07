##Plot and & save other graphs
import os
import matplotlib.pyplot as plt
import pandas as pd

import Plot_Draeger


def plot_other_graphs(df, folder_path):
    def two_axis_line(y1, y2, df, y1_label, y2_label):
        fig, ax = plt.subplots(figsize=(6,3.5))
        #markerstyles = ['v','o','+','*','.']
        ax.plot(y1, linewidth=1, label=y1_label, color='b')    
        ax.title.set_text(f"{y1_label} Vs {y2_label}")
        ax.set_ylim(bottom = 0)
        ax.set_ylabel(y1_label, fontsize=9)
        ax.set_xlabel('Samples', fontsize=9)
        
        xtick_labels = df.index
        step = max(1, len(xtick_labels) // 30)  # Adjusting step size
        ax.set_xticks(xtick_labels[::step])
        ax.set_xticklabels(xtick_labels[::step], rotation=90, fontsize=7)

        ax2 = ax.twinx()
        ax2.plot(y2, color='r', linewidth=1, label=y2_label)
        if y2_label not in ['Acetone', 'Temperature', 'Humidity']:
            ax2.set_ylim(bottom = 0)
        ax2.set_ylabel(y2_label, fontsize=9)
        lines_1, labels_1 = ax.get_legend_handles_labels()
        lines_2, labels_2 = ax2.get_legend_handles_labels()

        lines = lines_1 + lines_2
        labels = labels_1 + labels_2

        ax.legend(lines, labels, fontsize = 6, loc='upper right', bbox_to_anchor=(1.1, 1.1))

        plt.savefig(os.path.join(folder_path, f'{y1_label} VS {y2_label}.png'))
        fig = ax.get_figure()
        print(f'Plotted {y1_label} Vs {y2_label}')
        return fig
    #fig_width = widget_width / 100
    #fig_height = widget_height / 100
    fig_ws = two_axis_line(df['Ethanol'], df['windspeed'], df, y1_label= 'Ethanol' , y2_label = 'Windspeed')
    fig_ace = two_axis_line(df['Ethanol'], df['Acethone'], df, y1_label= 'Ethanol' , y2_label = 'Acetone')
    two_axis_line(df['Ethanol'], df['temperature'], df, y1_label= 'Ethanol' , y2_label = 'Temperature')
    two_axis_line(df['Ethanol'], df['humidity'], df, y1_label= 'Ethanol' , y2_label = 'Humidity')
    two_axis_line(df['windspeed'], df['windspeed_corr'], df, y1_label= 'Windspeed' , y2_label = 'Corrected_windspeed')
    fig_co2 = two_axis_line(df['Ethanol'], df['CO2'], df, y1_label= 'Ethanol' , y2_label = 'CO2')

    return fig_ws, fig_ace, fig_co2
"""
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
"""
