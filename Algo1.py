
# Function to fetch historical data
def  gt_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end)
    return data

# Function to implement the moving average crossover strategy
def moving_average_crossover(data, short_window=20, long_window=50):
    signals = pd.DataFrame(index=data.index)
    signals['Price'] = data['Close']
    signals['Short_MA'] = data['Close'].rolling(window=short_window, min_periods=1).mean()
    signals['Long_MA'] = data['Close'].rolling(window=long_window, min_periods=1).mean()
    signals['Signal'] = 0
    signals['Signal'][short_window:] = np.where(signals['Short_MA'][short_window:] > signals['Long_MA'][short_window:], 1, 0)
    signals['Position'] = signals['Signal'].diff()
    return signals

# Streamlit UI
st.title("Algorithmic Trading with Streamlit")

# User inputs
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL)", "AAPL")
start_date = st.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", pd.to_datetime("today"))

if st.button("Run Strategy"):
    data = get_data(ticker, start_date, end_date)
    signals = moving_average_crossover(data)

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close Price', alpha=0.5)
    plt.plot(signals['Short_MA'], label='Short Moving Average', alpha=0.75)
    plt.plot(signals['Long_MA'], label='Long Moving Average', alpha=0.75)

    # Plot buy signals
    plt.plot(signals[signals['Position'] == 1].index,
             signals['Short_MA'][signals['Position'] == 1], 
             '^', markersize=10, color='g', label='Buy Signal')

    # Plot sell signals
    plt.plot(signals[signals['Position'] == -1].index,
             signals['Short_MA'][signals['Position'] == -1], 
             'v', markersize=10, color='r', label='Sell Signal')

    plt.title(f'{ticker} Moving Average Crossover Strategy')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    st.pyplot(plt)

    # Display signals
    st.subheader('Trading Signals')
    st.write(signals)
