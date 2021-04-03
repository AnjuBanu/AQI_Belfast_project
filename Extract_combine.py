# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 23:03:25 2021

@author: Anjum Ismail
"""

from Plot_AQI import avg_data_year
import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup

#Webscrapping the file(dependent and independent features)
def meta_data(month, year):
    file_html = open("Data/Html_Data/2013/1.html", "rb")
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
        


for year in range(2013,2019):
    for month in range(1,13):
        meta_data(month, year)