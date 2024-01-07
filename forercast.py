from bs4 import BeautifulSoup
import requests
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime, timedelta
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from pmdarima import auto_arima #This one has to be installed using pip
import matplotlib.pyplot as plt

def Ingestion():
    # My baseurl for collecting new cases each day/30 days 
    base_url = 'https://www.nicd.ac.za/latest-confirmed-cases-of-covid-19-in-south-africa-{}/'
    
    #starting on the 2 of August 2021 while the Virus was still peaking and the website's structure at this time was a plus
    start_date = datetime(2021, 8, 2)
    num_days = 30
    
    #generating links for each day since the only thing changing on the url is the date
    # example url='https://www.nicd.ac.za/latest-confirmed-cases-of-covid-19-in-south-africa-11-August-2021/'
    urls = [base_url.format((start_date + timedelta(days=i)).strftime('%d-%B-%Y').lstrip('0')) for i in range(num_days)]
    
    #for my daily cases
    data= []
    
    #this is the fun :( part of the ingestion:web scraping
    #Iterating through each day and only taking the daily cases(and Province)
    for url in urls:
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        table= soup.find_all('table')[1]
        titles =table.find_all('tr')[0]
        headings = [title.text.strip() for title in titles if title.text.strip()]
        heading = [headings[0],headings[4]]
        df = pd.DataFrame(columns=heading)
        column_data = table.find_all('tr')
        for row in column_data[1:]:
            row_data = row.find_all('td')
            single = [row_data[0].text.strip(), row_data[4].text.strip()]
            length = len(df)
            df.loc[length] = single

        total_value = df.loc[df['Province'] == 'Total', heading[1]].values
        total = float(total_value[0].replace(',', '').replace(' ', '')) if total_value else None
        data.append(total)
    return data

def Modeling(data):
    # Convert the data into a pandas DataFrame
    df = pd.DataFrame({'date': pd.date_range(datetime(2021, 8, 2), periods=len(data), freq='D'), 'new_cases': data})
    
    #TO find the best parameters for my model
    '''step= auto_arima(df['new_cases'],trace=True,supress_warnings=True)
    step.summary()'''


    #alwasy told to split my data in training,testing and validation data
    #found not to be neccessary that much in this case
    '''train=df.iloc[:-10]
    #test=df.iloc[-10:]
    #print(train.shape,test.shape)
    model = ARIMA(train['new_cases'], order=(2, 0, 0 ))
    model = model.fit()
    model.summary()'''

    #This is where I train and predict using my model
    model = ARIMA(df['new_cases'],order=(2,0,0))
    model=model.fit()
    last=df.tail()
    #print(last)
    future_dates= pd.date_range(start="2021-09-01",end="2021-09-07")
    pred= model.predict(start=len(df),end=len(df)+6,type="levels").rename('ARIMA Predictions')
    pred.index =future_dates
    return pred
    
    
#for my interface
def forecast():
    data = Ingestion()
    pred = Modeling(data)
    pred = pred.reset_index().to_csv('covid_forecast_results.csv', index=False, header=['date', 'new_cases'])
    
    
