import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='History',
    page_icon=':)',
    layout='wide'
)

st.title("Prediction History")

# History page to display previous predictions
def display_prediction_history():
    csv_path = "./data/Prediction_history.csv"
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        # Return an empty DataFrame with a placeholder message
        df = pd.DataFrame(columns=["No data available"])
    
    return df

if __name__ == "__main__":
    df = display_prediction_history()
    st.dataframe(df)

    