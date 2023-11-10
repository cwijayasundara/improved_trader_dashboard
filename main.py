import streamlit as st
import matplotlib.pyplot as plt
from financial_analyst import (financial_analyst, get_company_news, get_stock_evolution, get_financial_statements,
                               get_balance_sheet)

st.set_page_config(layout="wide")

st.header("AI Financial Analyst App")


stocks = {
    "Alphabet - 'GOOG'": {"name": "Alphabet Inc.", "symbol": "GOOG", "cik": "0001652044"},
    "Apple - 'AAPL'": {"name": "APPLE INC", "symbol": "AAPL", "cik": "0000320193"}
}

col1, col2 = st.columns((1, 3))
col1, col2, col3 = st.columns((1, 2, 2))


def main():
    selected_stock = col1.selectbox("Select a stock", options=list(stocks.keys()))
    selected_stock_name = stocks[selected_stock]["name"]
    company_news = get_company_news(selected_stock_name)
    get_company_news_titles(company_news)

    col3.write(get_stock_evolution(stocks[selected_stock]["symbol"]))

    col2.write(get_balance_sheet(stocks[selected_stock]["symbol"]))


def get_company_news_titles(news):
    titles = []
    for news_item in news:
        if news_item is not None:
            title = news_item.get('title')
            titles.append(title)
            col2.write(title)
    return titles


if __name__ == "__main__":
    main()
