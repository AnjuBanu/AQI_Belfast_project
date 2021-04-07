# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 23:03:25 2021

@author: Anjum Ismail
"""

from Plot_AQI import avg_data_year
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import os


#Webscrapping the file(dependent and independent features)
def meta_data(month, year):
    file_html = open(f"../Data/Html_Data/{year}/{month}.html", "rb")
    plain_text = file_html.read()
    soup = BeautifulSoup(plain_text, "lxml")
    temp_D1 = []
    scrap_data = True
    final_data = []
    
    for table in soup.find_all("table", {"class":"medias mensuales numspan"}):
        for tbody in table:
            if (scrap_data):    
                for th in tbody:
                    if th.get_text() == "Monthly means and totals:":
                        scrap_data=False
                        break
                    a = th.get_text()
                    temp_D1.append(a)
 
    row = round(len(temp_D1) / 15)
    
    for time in range(row):
        temp_D2 = []
        for irow in range(15):
            temp_D2.append(temp_D1[0])
            temp_D1.pop(0)
        final_data.append(temp_D2)
    
    month_df = pd.DataFrame(final_data[1:])   
    return month_df




def combine_all_data():
    real_combined_data = pd.DataFrame()
    print ("combine_all_data")
    for year in range (2013,2019):
        data = pd.read_csv(f"../Data/Real-Data/real_{year}.csv")
        real_combined_data = pd.concat([real_combined_data,data],ignore_index=True)
    real_combined_data.to_csv(f"../Data/Real-Data/Real_Combine.csv", index=False)


if __name__ == "__main__":
    if not os.path.exists("../Data/Real-Data"):
        os.makedirs("../Data/Real-Data")
    for year in range (2013,2019):
        combined_year_df = pd.DataFrame()
        for month in range (1,13):
            month_df = meta_data(month, year)
            print (month_df)
            combined_year_df = pd.concat([combined_year_df,month_df],ignore_index=True)
        col=[0,6,10,11,12,13,14]
        combined_year_df =  combined_year_df.drop(col, axis=1)
        val = pd.DataFrame(avg_data_year(year))
        final_df = pd.concat([combined_year_df, val], axis=1)
        final_df.columns = ['T','TM','Tm','SLP','H','VV','V','VM','PM2.5']
        final_df.replace('', np.nan, inplace=True)
        final_df.replace('-', np.nan, inplace=True)
        final_df.dropna(inplace=True)
        final_df.reset_index(drop=True, inplace=True)
        final_df.to_csv(f"../Data/Real-Data/real_{year}.csv", index=False)
    combine_all_data()
    Read_Combine = pd.read_csv(f"../Data/Real-Data/Real_Combine.csv")
    

        
            
            