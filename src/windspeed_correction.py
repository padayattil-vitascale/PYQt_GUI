
#Equation to apply correction
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
        if row['Distance'] ==200:
            row['windspeed_corr'] = 1.7437*pow(row['windspeed'], 1.2998)
            return row['windspeed_corr']
        if row['Distance'] ==250:
            row['windspeed_corr'] = 1.719*pow(row['windspeed'], 1.3351)
            return row['windspeed_corr']
        if row['Distance'] ==300:
            row['windspeed_corr'] = 1.6498*pow(row['windspeed'], 1.2803)
            return row['windspeed_corr']
        if row['Distance'] ==350:
            row['windspeed_corr'] = 1.7159*pow(row['windspeed'], 1.2958)
            return row['windspeed_corr']
        if row['Distance'] ==400:
            row['windspeed_corr'] = 1.6229*pow(row['windspeed'], 1.251)
            return row['windspeed_corr']
        if row['Distance'] ==450:
            row['windspeed_corr'] = 1.4935*pow(row['windspeed'], 1.1701)
            return row['windspeed_corr']
        if row['Distance'] ==500:
            row['windspeed_corr'] = 1.8564*pow(row['windspeed'], 1.3472)
            return row['windspeed_corr']


    df['windspeed_corr'] = df.apply(apply_corr, axis = 1)
    return df