# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 16:45:29 2021

@author: Anjum Ismail
"""

import pandas as pd
import matplotlib.pyplot as plt


def avg_data_year(year):
    average =[]
    temp_i = 0
    for rows in pd.read_csv(f"../Data/AQI/aqi{year}.csv", chunksize=24):
        data=[]
        total_p = 0.0
        avg=0.0
        df = pd.DataFrame(rows)
        for index,row in df.iterrows():
            data.append(row ['PM2.5'])
        
        for i in data:
            if type(i) is int or type(i) is float:
                total_p = total_p+i
            elif type(i) is str and (i.strip().isdigit() or is_float(i.strip())):
                default_val = float (i)
                total_p = total_p+default_val
        
        avg = total_p/len(df)
        temp_i= temp_i+1
        average.append(avg) 
        
    return average


def is_float(string):
    try:
        return float(string) and '.' in string  # True if string is a number contains a dot
    except ValueError:  # String is not a number
        return False
    
    
if __name__ == "__main__":
    dic_year={}
    for year in range (2013,2019):
        dic_year[f'list{year}'] = avg_data_year(year)
        plt.plot(range(0,len(dic_year[f'list{year}'])), dic_year[f'list{year}'], label=f"Data for year {year}")
    plt.show()
    