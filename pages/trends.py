import requests
import streamlit as st
import pandas as pd
import json


def get_inflation_data_for_india():
    """Gets the inflation data for India from the FRED API."""
    base_url = "https://api.stlouisfed.org/fred"
    api_key = "ee9fd99b4380accc9399779924e322a9"

    # Example endpoint: Get data for Consumer Price Index (CPI) inflation rate in India
    series_id = "FPCPITOTLZGIND"  # Example series ID for CPI inflation in India
    url = f"{base_url}/series/observations?series_id={series_id}&api_key={api_key}&file_type=json"

    response = requests.get(url)
    data = response.json()
    df1 = pd.DataFrame(data)
    df = pd.DataFrame()
    df['date'] = df1['observations'].apply(lambda x: x['date'])
    # print(df['date'].dtype)
    df['date'] = pd.to_datetime(df['date'])

    df['inflation_value'] = df1['observations'].apply(lambda x: x['value'])
    df['inflation_value'] = pd.to_numeric(df['inflation_value'])
    # df.to_csv('out.csv')
    # print(df['value'].dtype)
    # print(df)

    return df

def plot_inflation_data_for_india(data):
    """Plots the inflation data for India in a Streamlit app."""
    st.title("Inflation in India")
    st.line_chart(data = data,x='date',y='inflation_value')


def get_resprop_prices_data_for_india():
    """Gets the inflation data for India from the FRED API."""
    base_url = "https://api.stlouisfed.org/fred"
    api_key = "ee9fd99b4380accc9399779924e322a9"

    # Example endpoint: Get data for Consumer Price Index (CPI) inflation rate in India
    series_id = "QINR628BIS"  # Example series ID for CPI inflation in India
    url = f"{base_url}/series/observations?series_id={series_id}&api_key={api_key}&file_type=json"

    response = requests.get(url)
    data = response.json()
    df1 = pd.DataFrame(data)
    df = pd.DataFrame()
    df['date'] = df1['observations'].apply(lambda x: x['date'])
    # print(df['date'].dtype)
    df['date'] = pd.to_datetime(df['date'])

    df['Index 2010=100'] = df1['observations'].apply(lambda x: x['value'])
    df['Index 2010=100'] = pd.to_numeric(df['Index 2010=100'])
    # df.to_csv('out.csv')
    # print(df['value'].dtype)
    # print(df)

    return df

def plot_resprop_prices_data_for_india(data):
    """Plots the inflation data for India in a Streamlit app."""
    st.title("Real Residential Property Prices for India (QINR628BIS) ")
    st.line_chart(data = data,x='date',y='Index 2010=100')


def get_interest_rate_data_for_india():
    """Gets the inflation data for India from the FRED API."""
    base_url = "https://api.stlouisfed.org/fred"
    api_key = "ee9fd99b4380accc9399779924e322a9"

    # Example endpoint: Get data for Consumer Price Index (CPI) inflation rate in India
    series_id = "INTDSRINM193N"  # Example series ID for CPI inflation in India
    url = f"{base_url}/series/observations?series_id={series_id}&api_key={api_key}&file_type=json"

    response = requests.get(url)
    data = response.json()
    df1 = pd.DataFrame(data)
    df = pd.DataFrame()
    df['date'] = df1['observations'].apply(lambda x: x['date'])
    # print(df['date'].dtype)
    df['date'] = pd.to_datetime(df['date'])

    df['Percent per annum'] = df1['observations'].apply(lambda x: x['value'])
    df['Percent per annum'] = pd.to_numeric(df['Percent per annum'])
    # df.to_csv('out.csv')
    # print(df['value'].dtype)
    # print(df)

    return df

def plot_interest_rate_data_for_india(data):
    """Plots the inflation data for India in a Streamlit app."""
    st.title("Interest Rates for India")
    st.line_chart(data = data,x='date',y='Percent per annum')

def get_economic_policy_uncertainity_index_data():
    """Gets the inflation data for India from the FRED API."""
    base_url = "https://api.stlouisfed.org/fred"
    api_key = "ee9fd99b4380accc9399779924e322a9"

    # Example endpoint: Get data for Consumer Price Index (CPI) inflation rate in India
    series_id = "EPUFINREG"  # Example series ID for CPI inflation in India
    url = f"{base_url}/series/observations?series_id={series_id}&api_key={api_key}&file_type=json"

    response = requests.get(url)
    data = response.json()
    df1 = pd.DataFrame(data)
    df = pd.DataFrame()
    df['date'] = df1['observations'].apply(lambda x: x['date'])
    # print(df['date'].dtype)
    df['date'] = pd.to_datetime(df['date'])

    df['Index'] = df1['observations'].apply(lambda x: x['value'])
    df['Index'] = pd.to_numeric(df['Index'])
    # df.to_csv('out.csv')
    # print(df['value'].dtype)
    # print(df)

    return df

def plot_economic_policy_uncertainity_index_data(data):
    """Plots the inflation data for India in a Streamlit app."""
    st.title("Economic Policy Uncertainty Index: Categorical Index: Financial Regulation (EPUFINREG) ")
    st.line_chart(data = data,x='date',y='Index')

def get_equity_market_volatility_data():
    """Gets the inflation data for India from the FRED API."""
    base_url = "https://api.stlouisfed.org/fred"
    api_key = "ee9fd99b4380accc9399779924e322a9"

    # Example endpoint: Get data for Consumer Price Index (CPI) inflation rate in India
    series_id = "EMVFINREG"  # Example series ID for CPI inflation in India
    url = f"{base_url}/series/observations?series_id={series_id}&api_key={api_key}&file_type=json"

    response = requests.get(url)
    data = response.json()
    df1 = pd.DataFrame(data)
    df = pd.DataFrame()
    df['date'] = df1['observations'].apply(lambda x: x['date'])
    # print(df['date'].dtype)
    df['date'] = pd.to_datetime(df['date'])

    df['Index'] = df1['observations'].apply(lambda x: x['value'])
    df['Index'] = pd.to_numeric(df['Index'])
    # df.to_csv('out.csv')
    # print(df['value'].dtype)
    # print(df)

    return df

def plot_equity_market_volatility_data(data):
    """Plots the inflation data for India in a Streamlit app."""
    st.title("Equity Market Volatility Tracker: Financial Regulation (EMVFINREG) ")
    st.line_chart(data = data,x='date',y='Index')

if __name__ == "__main__":
    data = get_inflation_data_for_india()
    plot_inflation_data_for_india(data)

    data2 = get_resprop_prices_data_for_india()
    plot_resprop_prices_data_for_india(data2)

    data3 = get_interest_rate_data_for_india()
    plot_interest_rate_data_for_india(data3)
    
    data4 = get_economic_policy_uncertainity_index_data()
    plot_economic_policy_uncertainity_index_data(data4)

    data5 = get_equity_market_volatility_data()
    plot_equity_market_volatility_data(data5)
