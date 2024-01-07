# Pandemic Forecasting

This project is a COVID-19 forecasting application that predicts the number of new cases over the next seven days based on historical data.

## Requirements

- Python (>=3.6)
- Flask
- pandas
- matplotlib
- chart.js (included via CDN in the HTML file)
- JupyterNotebook(Please run the app on the terminal of jupyter because most libraries have already been installed)

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/Pandemic-Forecasting.git
    cd Pandemic-Forecasting
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Make sure you have the required dependencies installed.

2. Run the Flask app:

    ```bash
    python app.py
    ```

3. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the COVID-19 forecasting results.

## File Structure

- `app.py`: The main Flask application.
- `templates/index.html`: HTML template for rendering the forecasting results.
- `forecast.py`: Module containing functions for data ingestion, modeling, and reporting.
- `your_data_file.csv`: CSV file containing historical COVID-19 data (But automatically updates everytime you run the app).

## Cons
- The app will take a while to run, not very sure if it is my network speed or the Ingestion part all on its own
- A little Patience is require
## Pros
- It works :)