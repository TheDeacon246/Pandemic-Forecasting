# app.py
from flask import Flask, render_template
import pandas as pd
from forercast import forecast
#To create the csv in the directory
forecast()

app = Flask(__name__)

@app.route('/')
def index():
    # Read data from CSV file
    df = pd.read_csv('covid_forecast_results.csv')

    return render_template('index.html', pred=df.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True)
