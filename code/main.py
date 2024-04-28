# main.py

import data_retrieval
import data_processing
import visualization


def main():
    # Retrieve data from Yahoo Finance and Alpha Vantage APIs
    yahoo_data = data_retrieval.retrieve_yahoo_data(
        symbol='AAPL', start_date='2022-01-01', end_date='2024-03-31')
    alpha_vantage_data = data_retrieval.retrieve_alpha_vantage_data(
        symbol='AAPL', start_date='2022-0-01', end_date='2024-03-31')

    # Process and analyze the retrieved data
    processed_yahoo_data = data_processing.process_data(yahoo_data)
    processed_alpha_vantage_data = data_processing.process_data(
        alpha_vantage_data)

    # Compare the processed data
    comparison_result = data_processing.compare_data(
        processed_yahoo_data, processed_alpha_vantage_data)

    # Visualize the comparison results
    visualization.plot_comparison(comparison_result)


if __name__ == "__main__":
    main()
