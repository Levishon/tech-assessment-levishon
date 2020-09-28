import bs4
from bs4 import BeautifulSoup
import requests

from datetime import datetime
import re
import time
import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LEVIS;'
                      'Database=WeatherDB;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
def test():
    url='https://www.weather-forecast.com/'
    page = requests.get(url)
    
    eindtemp = re.search('(?s)Eindhoven.+?temp">([^<]+)', page.text).group(1)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print("Current Time =", current_time)
    print(eindtemp)
    
    eindtemp = float(eindtemp)
  
    
 
    sql_insert_query = """INSERT INTO dbo.Temp(Time, Temperature)
                           VALUES 
                           (?, ?) """
    data = (datetime.now(), eindtemp)
    cursor.execute(sql_insert_query,data )
    print("%d rows were inserted" % cursor.rowcount)
    cursor.execute("COMMIT")
 
    cursor.execute('SELECT * FROM dbo.Temp')
    for row in cursor:
        print(row)
        
while True:
    test() 
    time.sleep(300)
    