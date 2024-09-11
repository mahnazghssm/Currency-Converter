"""
Author: Mahnaz Ghassemi
Date created: 09,11,2024
Description: Currency Converter streamlit
"""

import streamlit as st  # Import Streamlit to create a web interface

from constant import (
    currencies,  # Import the list of available currencies from constants
)
from currency_converter import (  # Import exchange rate and conversion functions
    convert_currency,
    get_exchange_rate,
)

# Set the title of the Streamlit app with a dollar emoji
st.title(":dollar: Currency Converter")

# Add a description for the tool using markdown
st.markdown("""
This tool allows you to instantly convert amounts between different currencies.

Enter the amount and choose the currencies to see the result.
""")

# Dropdown for selecting the base currency (currency you are converting from)
base_currency = st.selectbox("From currency (base):", currencies)

# Dropdown for selecting the target currency (currency you are converting to)
target_currency = st.selectbox("To currency (target):", currencies)

# Input field for the amount to be converted with a minimum value of 0.0 and a max of 100.0
amount = st.number_input("Please enter amount:", min_value=0.0, max_value=100.0)

# Check if the amount entered is greater than 0 and both currencies are selected
if amount > 0 and base_currency and target_currency:
    # Fetch the exchange rate using the base and target currencies
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    
    # If the exchange rate is successfully fetched
    if exchange_rate:
        # Convert the input amount using the fetched exchange rate
        converted_amount = convert_currency(amount, exchange_rate)
        
        # Display the exchange rate using a success message
        st.success(f"✅ Exchange Rate: {exchange_rate:.2f}")
        
        # Create three columns to display the base amount, arrow, and converted amount
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Display the base amount and currency in the first column
            st.metric(label="Base Currency", value=f"{amount:.2f} {base_currency}")
        
        with col2:
            # Display a right arrow between the columns with custom styling
            st.markdown("<h1 style='text-align: center; margin: 0; color: green;'>&#8594;</h1>", unsafe_allow_html=True)
        
        with col3:
            # Display the converted amount and target currency in the third column
            st.metric(label="Target Currency", value=f"{converted_amount:.2f} {target_currency}")
    else:
        # Display an error message if the exchange rate couldn't be fetched
        st.error("Error fetching exchange rate.")

# Add a horizontal line as a separator
st.markdown("---")

# Add a section for tool information using markdown
st.markdown("### ℹ️ About This Tool")
st.markdown("""
This currency converter uses real-time exchange rates provided by the ExchangeRate-API.

- The conversion updates automatically as you input the amount or change the currency.
- Enjoy seamless currency conversion without the need to press a button!
""")