
import math
#Equation to apply correction above 25slm
"""
200mm = 1.7437x 1.2998
250mm = 1.719x 1.3351
300mm = 1.6498x 1.2803
350mm = 1.7159x 1.2958
400mm = 1.6229x 1.251
450mm = 1.4935x 1.1701
500mm = 1.8564x 1.3472
"""

def windspeed_corr(df):
    def apply_corr(row):
        if row['filtered_windspeed'] < (-0.129 * math.log(row['Distance']) + 0.872):  # Low windspeeds are not corrected..equation to the minimum windspeed
            row['windspeed_corr'] = row['filtered_windspeed']
            return row['windspeed_corr']
        elif row['filtered_windspeed'] > (-0.129 * math.log(row['Distance']) + 0.872) and row['Distance'] <= 450:
            C = math.log(-0.0043*(row['Distance']) + 6.6584)
            T = math.log(-0.0018*(row['Distance'])  + 4.1475)
            row['windspeed_corr'] = C*pow(row['filtered_windspeed'], T)
            return row['windspeed_corr']
        elif row['filtered_windspeed'] > (-0.129 * math.log(row['Distance']) + 0.872) and row['Distance'] < 450:
            C = math.log(0.0133 *(row['Distance']) - 0.691)
            T = math.log(0.0035 *(row['Distance']) + 1.9333)
            row['windspeed_corr'] = C*pow(row['filtered_windspeed'], T)
            return row['windspeed_corr']

        """
        if row['Distance'] ==200 and row['filtered_windspeed'] > 0.2:
            row['windspeed_corr'] = 1.7437*pow(row['filtered_windspeed'], 1.2998)
            return row['windspeed_corr']
        if row['Distance'] ==200 and row['filtered_windspeed'] <= 0.2:
            row['windspeed_corr'] = row['filtered_windspeed']
            return row['windspeed_corr']
        elif row['Distance'] ==250 and row['filtered_windspeed'] > 0.16:
            row['windspeed_corr'] = 1.719*pow(row['filtered_windspeed'], 1.3351)
            return row['windspeed_corr']
        elif row['Distance'] ==250 and row['filtered_windspeed'] <= 0.16:
            row['windspeed_corr'] = row['filtered_windspeed']
            return row['windspeed_corr']
        elif row['Distance'] ==300 and row['filtered_windspeed'] > 0.13:
            row['windspeed_corr'] = 1.6498*pow(row['filtered_windspeed'], 1.2803)
            return row['windspeed_corr']
        elif row['Distance'] ==300 and row['filtered_windspeed'] <= 0.13:
            row['windspeed_corr'] = row['filtered_windspeed']
            return row['windspeed_corr']
        elif row['Distance'] ==350 and row['filtered_windspeed'] > 0.11:
            row['windspeed_corr'] = 1.7159*pow(row['filtered_windspeed'], 1.2958)
            return row['windspeed_corr']
        elif row['Distance'] ==350 and row['filtered_windspeed'] <= 0.11:
            row['windspeed_corr'] = row['filtered_windspeed']
            return row['windspeed_corr']
        elif row['Distance'] ==400 and row['filtered_windspeed'] > 0.1:
            row['windspeed_corr'] = 1.6229*pow(row['filtered_windspeed'], 1.251)
            return row['windspeed_corr']
        elif row['Distance'] ==400 and row['filtered_windspeed'] <= 0.1:
            row['windspeed_corr'] = row['filtered_windspeed']
            return row['windspeed_corr']
        elif row['Distance'] ==450 and row['filtered_windspeed'] > 0.09:
            row['windspeed_corr'] = 1.4935*pow(row['filtered_windspeed'], 1.1701)
            return row['windspeed_corr']
        elif row['Distance'] ==450 and row['filtered_windspeed'] <= 0.09:
            row['windspeed_corr'] = row['filtered_windspeed']
            return row['windspeed_corr']
        elif row['Distance'] ==500 and row['filtered_windspeed'] > 0.08:
            row['windspeed_corr'] = 1.8564*pow(row['filtered_windspeed'], 1.3472)
            return row['windspeed_corr']
        elif row['Distance'] ==500 and row['filtered_windspeed'] <= 0.08:
            row['windspeed_corr'] = row['filtered_windspeed']
            return row['windspeed_corr']
"""

    df['windspeed_corr'] = df.apply(apply_corr, axis = 1)
    return df