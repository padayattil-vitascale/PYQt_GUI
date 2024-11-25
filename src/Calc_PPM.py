import math

def cal_ppm(new_delta: float, constant: float, expo: float) -> float:
    row_new = constant * math.exp(expo * new_delta)
    return row_new

def predict_ppm_on_distance(df):

    #Function to calculate PPM based on the Max deviation reference 2.3
    def apply_cal_PPM_2_3(row):
        const = 0
        expo = 0

        if row['Distance'] == 200:
            if row['Windspeed_max_filtered'] <= 0.74:
                const = 10.984 * math.log(row['Windspeed_max_filtered']) + 30.714
                expo = -0.3 * math.log(row['Windspeed_max_filtered']) + 2.235
            elif 0.74 < row['Windspeed_max_filtered'] <= 0.96:
                const = 22.24 * math.log(row['Windspeed_max_filtered']) + 39.48
                expo = -0.241 * math.log(row['Windspeed_max_filtered']) + 2.255
            else:
                const = 18.456 * math.log(row['Windspeed_max_filtered']) + 36.805
                expo = -0.0186 * math.log(row['Windspeed_max_filtered']) + 2.355
        elif row['Distance'] == 250:
            if row['Windspeed_max_filtered'] <= 0.65:
                const = 10.135 * math.log(row['Windspeed_max_filtered']) + 34.925
                expo = -0.191 * math.log(row['Windspeed_max_filtered']) + 2.305
            elif 0.65 < row['Windspeed_max_filtered'] <= 0.86:
                const = 21.14 * math.log(row['Windspeed_max_filtered']) + 45.52
                expo = -0.215 * math.log(row['Windspeed_max_filtered']) + 2.26
            else:
                const = 32.598 * math.log(row['Windspeed_max_filtered']) + 49.8
                expo = -0.326 * math.log(row['Windspeed_max_filtered']) + 2.274
        elif row['Distance'] == 300:
            if row['Windspeed_max_filtered'] <= 0.55:
                const = 7.272 * math.log(row['Windspeed_max_filtered']) + 36.55
                expo = -0.046 * math.log(row['Windspeed_max_filtered']) + 2.415
            elif 0.55 < row['Windspeed_max_filtered'] <= 0.77:
                const = 17.03 * math.log(row['Windspeed_max_filtered']) + 51.3
                expo = -0.012 * math.log(row['Windspeed_max_filtered']) + 2.35
            else:
                const = 44.86 * math.log(row['Windspeed_max_filtered']) + 62.57
                expo = -0.519 * math.log(row['Windspeed_max_filtered']) + 2.125
        elif row['Distance'] == 350:
            if row['Windspeed_max_filtered'] <= 0.5:
                const = 9.696 * math.log(row['Windspeed_max_filtered']) + 48.344
                expo = -0.127 * math.log(row['Windspeed_max_filtered']) + 2.18
            elif 0.5 < row['Windspeed_max_filtered'] <= 0.74:
                const = 26.78 * math.log(row['Windspeed_max_filtered']) + 72.24
                expo = -0.213 * math.log(row['Windspeed_max_filtered']) + 2.02
            else:
                const = 22.085 * math.log(row['Windspeed_max_filtered']) + 63.9
                expo = 0.0542 * math.log(row['Windspeed_max_filtered']) + 2.3
        elif row['Distance'] == 400:
            if row['Windspeed_max_filtered'] <= 0.43:
                const = 10.035 * math.log(row['Windspeed_max_filtered']) + 57.529
                expo = -0.047 * math.log(row['Windspeed_max_filtered']) + 2.29
            elif 0.43 < row['Windspeed_max_filtered'] <= 0.61:
                const = 26.62 * math.log(row['Windspeed_max_filtered']) + 81
                expo = -0.187 * math.log(row['Windspeed_max_filtered']) + 2.09
            else:
                const = 29.94 * math.log(row['Windspeed_max_filtered']) + 81.5
                expo = -0.07 * math.log(row['Windspeed_max_filtered']) + 2.2
        elif row['Distance'] == 450:
            if row['Windspeed_max_filtered'] <= 0.37:
                const = 4.27 * math.log(row['Windspeed_max_filtered']) + 48.39
                expo = 0.176 * math.log(row['Windspeed_max_filtered']) + 2.8
            elif 0.37 < row['Windspeed_max_filtered'] <= 0.51:
                const = 24.43 * math.log(row['Windspeed_max_filtered']) + 81.18
                expo = -0.08 * math.log(row['Windspeed_max_filtered']) + 2.31
            else:
                const = 47.351 * math.log(row['Windspeed_max_filtered']) + 103
                expo = -0.457 * math.log(row['Windspeed_max_filtered']) + 2.03
        elif row['Distance'] == 500:
            if row['Windspeed_max_filtered'] <= 0.32:
                const = 5.268 * math.log(row['Windspeed_max_filtered']) + 60.087
                expo = 0.1185 * math.log(row['Windspeed_max_filtered']) + 2.65
            elif 0.32 < row['Windspeed_max_filtered'] <= 0.51:
                const = 9.84 * math.log(row['Windspeed_max_filtered']) + 73.55
                expo = 0.156 * math.log(row['Windspeed_max_filtered']) + 2.54
            else:
                const = 45 * math.log(row['Windspeed_max_filtered']) + 105.6
                expo = -0.405 * math.log(row['Windspeed_max_filtered']) + 2.12
        else:
            const = 1.0
            expo = 1.0
        
        ppm_2_3 = cal_ppm(new_delta=row['New_Delta_Ref_2.3'], constant=const, expo=expo)

        return ppm_2_3
    
    #Function to calculate PPM based on the Max deviation reference 3
    def apply_cal_PPM_3(row):
        const = 0
        expo = 0

        if row['Distance'] == 200:
            if row['Windspeed_max_filtered'] <= 0.74:
                const = (10.984 * math.log(row['Windspeed_max_filtered']) + 30.714)/4
                expo = -0.3 * math.log(row['Windspeed_max_filtered']) + 2.235
            elif 0.74 < row['Windspeed_max_filtered'] <= 0.96:
                const = (22.24 * math.log(row['Windspeed_max_filtered']) + 39.48)/3.2
                expo = -0.241 * math.log(row['Windspeed_max_filtered']) + 2.255
            else:
                const = (18.456 * math.log(row['Windspeed_max_filtered']) + 36.805)/3.6
                expo = -0.0186 * math.log(row['Windspeed_max_filtered']) + 2.355
        elif row['Distance'] == 250:
            if row['Windspeed_max_filtered'] <= 0.65:
                const = (10.135 * math.log(row['Windspeed_max_filtered']) + 34.925)/4
                expo = -0.191 * math.log(row['Windspeed_max_filtered']) + 2.305
            elif 0.65 < row['Windspeed_max_filtered'] <= 0.86:
                const = (21.14 * math.log(row['Windspeed_max_filtered']) + 45.52)/3.2
                expo = -0.215 * math.log(row['Windspeed_max_filtered']) + 2.26
            else:
                const = (32.598 * math.log(row['Windspeed_max_filtered']) + 49.8)/3.6
                expo = -0.326 * math.log(row['Windspeed_max_filtered']) + 2.274
        elif row['Distance'] == 300:
            if row['Windspeed_max_filtered'] <= 0.55:
                const = (7.272 * math.log(row['Windspeed_max_filtered']) + 36.55)/3.5
                expo = -0.046 * math.log(row['Windspeed_max_filtered']) + 2.415
            elif 0.55 < row['Windspeed_max_filtered'] <= 0.77:
                const = (17.03 * math.log(row['Windspeed_max_filtered']) + 51.3)/3.1
                expo = -0.012 * math.log(row['Windspeed_max_filtered']) + 2.35
            else:
                const = (44.86 * math.log(row['Windspeed_max_filtered']) + 62.57)/3.3
                expo = -0.519 * math.log(row['Windspeed_max_filtered']) + 2.125
        elif row['Distance'] == 350:
            if row['Windspeed_max_filtered'] <= 0.5:
                const = (9.696 * math.log(row['Windspeed_max_filtered']) + 48.344)/3.5
                expo = -0.127 * math.log(row['Windspeed_max_filtered']) + 2.18
            elif 0.5 < row['Windspeed_max_filtered'] <= 0.74:
                const = (26.78 * math.log(row['Windspeed_max_filtered']) + 72.24)/3.1
                expo = -0.213 * math.log(row['Windspeed_max_filtered']) + 2.02
            else:
                const = (22.085 * math.log(row['Windspeed_max_filtered']) + 63.9)/3.3
                expo = 0.0542 * math.log(row['Windspeed_max_filtered']) + 2.3
        elif row['Distance'] == 400:
            if row['Windspeed_max_filtered'] <= 0.43:
                const = (10.035 * math.log(row['Windspeed_max_filtered']) + 57.529)/2.9
                expo = -0.047 * math.log(row['Windspeed_max_filtered']) + 2.29
            elif 0.43 < row['Windspeed_max_filtered'] <= 0.61:
                const = (26.62 * math.log(row['Windspeed_max_filtered']) + 81)/2.6
                expo = -0.187 * math.log(row['Windspeed_max_filtered']) + 2.09
            else:
                const = (29.94 * math.log(row['Windspeed_max_filtered']) + 81.5)/3
                expo = -0.07 * math.log(row['Windspeed_max_filtered']) + 2.2
        elif row['Distance'] == 450:
            if row['Windspeed_max_filtered'] <= 0.37:
                const = (4.27 * math.log(row['Windspeed_max_filtered']) + 48.39)/2.9
                expo = 0.176 * math.log(row['Windspeed_max_filtered']) + 2.8
            elif 0.37 < row['Windspeed_max_filtered'] <= 0.51:
                const = (24.43 * math.log(row['Windspeed_max_filtered']) + 81.18)/2.6
                expo = -0.08 * math.log(row['Windspeed_max_filtered']) + 2.31
            else:
                const = (47.351 * math.log(row['Windspeed_max_filtered']) + 103)/3
                expo = -0.457 * math.log(row['Windspeed_max_filtered']) + 2.03
        elif row['Distance'] == 500:
            if row['Windspeed_max_filtered'] <= 0.32:
                const = (5.268 * math.log(row['Windspeed_max_filtered']) + 60.087)/2.3
                expo = 0.1185 * math.log(row['Windspeed_max_filtered']) + 2.65
            elif 0.32 < row['Windspeed_max_filtered'] <= 0.51:
                const = (9.84 * math.log(row['Windspeed_max_filtered']) + 73.55)/2.3
                expo = 0.156 * math.log(row['Windspeed_max_filtered']) + 2.54
            else:
                const = (45 * math.log(row['Windspeed_max_filtered']) + 105.6)/2.3
                expo = -0.405 * math.log(row['Windspeed_max_filtered']) + 2.12
        else:
            const = 1.0
            expo = 1.0
        
        ppm_3 = cal_ppm(new_delta=row['New_Delta_Ref_3'], constant=const, expo=expo)

        return ppm_3
    
    df['Calculated_PPM_Ref_2.3'] = df.apply(apply_cal_PPM_2_3, axis=1)
    df['Calculated_PPM_Ref_3'] = df.apply(apply_cal_PPM_3, axis=1)
    return df