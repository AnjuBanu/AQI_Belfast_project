# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 14:08:33 2021

@author: Anjum Ismail


"""


import os
import time
import requests
import sys



# Data is collected from https://en.tutiempo.net
# Collected data for city Belfats for very month and year
# Sample URL: https://en.tutiempo.net/climate/01-2020/ws-39240.html
# URL can be modified accordingly to get all the data

def retrieve_html ():
    for year in range (2013, 2019):
        print (f"Collecting data for {year}")
        for month in range (1,13):
            if (month < 10):
                url = (f'https://en.tutiempo.net/climate/0{month}-{year}/ws-421820.html')

            else:
                url= (f'https://en.tutiempo.net/climate/{month}-{year}/ws-421820.html')
     
            texts = requests.get(url)
            text_utf = texts.text.encode('utf=8')

            if not os.path.exists(f'Data/Html_Data/{year}'):
                os.makedirs(f'Data/Html_Data/{year}')
            with open(f'Data/Html_Data/{year}/{month}.html', "wb") as output:
                output.write(text_utf)
        
        sys.stdout.flush()




if __name__ == '__main__':
    start_time = time.time()
    retrieve_html()
    stop_time = time.time()
    print (f'Time taken = {stop_time - start_time}')
    