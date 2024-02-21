# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.set(style="whitegrid")

# def run_transaction_analysis_app():
#     st.title("Transactional Data Analysis")
#     st.write("This section analyzes your transactional data over a period of time.")

#     # Simulate transactional data
#     num_transactions = st.number_input("Number of simulated transactions", min_value=10, max_value=1000, value=100, step=10)
#     transaction_dates = pd.date_range(start="2023-01-01", periods=num_transactions, freq="D")
#     transaction_amounts = np.random.uniform(10, 500, num_transactions)

#     transaction_data = {
#         'Date': transaction_dates,
#         'Amount': transaction_amounts
#     }
#     transactions_df = pd.DataFrame(transaction_data)

#     st.write("Sample Transactional Data:")
#     st.dataframe(transactions_df)

#     # Plot Transaction Trends
#     plt.figure(figsize=(10, 6))
#     plt.plot(transactions_df['Date'], transactions_df['Amount'], marker='o')
#     plt.xlabel('Date')
#     plt.ylabel('Transaction Amount')
#     plt.title('Transaction Trends')
#     st.write("Transaction Trends:")
#     st.pyplot(plt)

# if __name__ == "__main__":
#     # st.sidebar.title("Navigation")
#     # app_mode = st.sidebar.selectbox("Choose a mode", ["Introduction", "Financial Tracker", "Transaction Analysis"])

#     # if app_mode == "Introduction":
#     #     st.sidebar.success("To view the financial tracker, select 'Financial Tracker' from the dropdown.")
#     #     st.sidebar.success("To analyze transaction data, select 'Transaction Analysis' from the dropdown.")
#     # elif app_mode == "Financial Tracker":
#     #     st.sidebar.success("You're in Financial Tracker mode.")
#     #     run_financial_tracker_app()
#     # elif app_mode == "Transaction Analysis":
#     #     st.sidebar.success("You're in Transaction Analysis mode.")
#     run_transaction_analysis_app()


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


def run_transaction_analysis_app():
    st.title("Transactional Data Analysis")
    st.write("This section analyzes your transactional data over a period of time.")

    # Simulate transactional data
    num_transactions = st.number_input("Number of simulated transactions", min_value=10, max_value=1000, value=100, step=10)
    min_date = pd.to_datetime("2015-01-10")
    max_date = pd.to_datetime("2023-12-29")
    transaction_dates = pd.date_range(start=min_date, end=max_date, periods=num_transactions)
    transaction_categories = np.random.choice(['Groceries', 'Dining', 'Shopping', 'Transportation', 'Entertainment'], num_transactions)
    transaction_labels = np.random.choice(['Groceries', 'Bills', 'Rent', 'Shopping', 'Dining', 'Transportation'], num_transactions)
    transaction_amounts = np.random.uniform(10, 500, num_transactions)

    transaction_data = {
        'Date': transaction_dates,
        'Category': transaction_categories,
        'SpendLabel': transaction_labels,
        'Amount': transaction_amounts
    }
    transactions_df = pd.DataFrame(transaction_data)

    st.write("Sample Transactional Data:")
    st.dataframe(transactions_df)

    # Interactive Date Range Selection
    st.write("Select Date Range for Analysis:")
    date_range = st.date_input("Select start date", min_value=min_date.date(), max_value=max_date.date())
    date_range = pd.to_datetime(date_range)  # Convert to datetime64
    transactions_selected = transactions_df[transactions_df['Date'] >= date_range]

    # Interactive Category Selection
    selected_category = st.selectbox("Select a transaction category", transactions_selected['Category'].unique())
    transactions_category = transactions_selected[transactions_selected['Category'] == selected_category]

    # Visualize Transaction Trends
    st.write(f"Transaction Trends for Category: {selected_category}")
    plt.figure(figsize=(10, 6))
    plt.plot(transactions_category['Date'], transactions_category['Amount'], marker='o')
    plt.xlabel('Date')
    plt.ylabel('Transaction Amount')
    plt.title(f'Transaction Trends for {selected_category}')
    st.pyplot(plt)

    # # Total Spending by SpendLabel
    # st.write("Total Spending by SpendLabel:")
    # spendlabel_spending = transactions_selected.groupby('SpendLabel')['Amount'].sum()
    # plt.figure(figsize=(10, 6))
    # spendlabel_spending.sort_values(ascending=False).plot(kind='bar')
    # plt.xlabel('SpendLabel')
    # plt.ylabel('Total Amount')
    # plt.title('Total Spending by SpendLabel')
    # plt.xticks(rotation=45)
    # st.pyplot(plt)

    # # Total Spending by SpendLabel
    # st.write("Total Spending by SpendLabel:")

    spendlabel_spending = transactions_selected.groupby('SpendLabel')['Amount'].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(spendlabel_spending, labels=spendlabel_spending.index, autopct="%1.1f%%", startangle=140)
    plt.axis('equal')
    plt.title('Total Spending by SpendLabel')
    st.pyplot(plt)

    # Time Series Line Chart for SpendLabel Trends
    st.write("Time Series Line Chart for SpendLabel Trends:")

    plt.figure(figsize=(10, 6))
    for spend_label in transactions_selected['SpendLabel'].unique():
        spend_label_data = transactions_selected[transactions_selected['SpendLabel'] == spend_label]
        plt.plot(spend_label_data['Date'], spend_label_data['Amount'], marker='o', label=spend_label)
    plt.xlabel('Date')
    plt.ylabel('Transaction Amount')
    plt.title('SpendLabel Trends Over Time')
    plt.legend()
    st.pyplot(plt)

    # Monthly Spending Analysis
    st.write("Monthly Spending Analysis:")

    # Group data by month and calculate total spending
    transactions_selected['Month'] = transactions_selected['Date'].dt.to_period('M')
    monthly_spending = transactions_selected.groupby('Month')['Amount'].sum()

    plt.figure(figsize=(10, 6))
    plt.plot(monthly_spending.index.astype(str), monthly_spending.values, marker='o')
    plt.xlabel('Month')
    plt.ylabel('Total Spending')
    plt.title('Monthly Spending Analysis')
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Summary Statistics
    st.write("Summary Statistics:")
    total_spending = transactions_selected['Amount'].sum()
    avg_transaction_amount = transactions_selected['Amount'].mean()
    max_transaction_amount = transactions_selected['Amount'].max()
    min_transaction_amount = transactions_selected['Amount'].min()

    st.write(f"Total Spending: ${total_spending:.2f}")
    st.write(f"Average Transaction Amount: ${avg_transaction_amount:.2f}")
    st.write(f"Maximum Transaction Amount: ${max_transaction_amount:.2f}")
    st.write(f"Minimum Transaction Amount: ${min_transaction_amount:.2f}")

if __name__ == "__main__":
    # st.sidebar.title("Navigation")
    # app_mode = st.sidebar.selectbox("Choose a mode", ["Introduction", "Financial Tracker", "Transaction Analysis"])

    # if app_mode == "Introduction":
    #     st.sidebar.success("To view the financial tracker, select 'Financial Tracker' from the dropdown.")
    #     st.sidebar.success("To analyze transaction data, select 'Transaction Analysis' from the dropdown.")
    # elif app_mode == "Financial Tracker":
    #     st.sidebar.success("You're in Financial Tracker mode.")
    #     run_financial_tracker_app()
    # elif app_mode == "Transaction Analysis":
    #     st.sidebar.success("You're in Transaction Analysis mode.")
    run_transaction_analysis_app()
