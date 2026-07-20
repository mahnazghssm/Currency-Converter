"""
Author: Mahnaz Ghassemi
Date created: 09,09,2024
Description: Currency Converter
"""

import requests  # Import the requests module to make HTTP requests to the API
from cachetools import (  # Import caching tools to reduce repeated API calls
    TTLCache,
    cached,
)

# Create a cache with a maximum size of 100 entries and a Time-to-Live (TTL) of 3 hours
cache = TTLCache(maxsize=100, ttl=3*60*60)

@cached(cache)
# Function to get the exchange rate between two currencies
def get_exchange_rate(base_currency, target_currency):
    """
    This function fetches the exchange rate for the target currency 
    based on the provided base currency using the ExchangeRate API.

    Parameters:
    base_currency (str): The currency you're converting from (e.g., "USD").
    target_currency (str): The currency you're converting to (e.g., "EUR").

    Returns:
    float: The exchange rate between the base and target currencies.
    None: If there was an issue with the API request or the target currency isn't available.
    """
    # Construct the API URL with the base currency dynamically inserted
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    
    # Make an HTTP GET request to the API to fetch the latest exchange rates
    response = requests.get(url)

    # If the request is not successful (i.e., status code is not 200), return None
    if response.status_code != 200:
        return None  # Indicates that the API request failed
    
    # Extract and return the exchange rate for the target currency from the JSON response
    return response.json()["rates"][target_currency]

# Function to convert an amount using the exchange rate
def convert_currency(amount, exchange_rate):
    """
    This function converts an amount using the given exchange rate.

    Parameters:
    amount (float): The amount of money to convert.
    exchange_rate (float): The exchange rate between the base and target currencies.

    Returns:
    float: The converted amount in the target currency.
    """
    # Multiply the amount by the exchange rate to convert the currency
    return amount * exchange_rate

# Main block where the program execution starts
if __name__ == "__main__":
    # Prompt the user to input the base currency (the currency they want to convert from)
    base_currency = input("Enter base currency (e.g., USD, EUR): ")
    
    # Prompt the user to input the target currency (the currency they want to convert to)
    target_currency = input("Enter target currency (e.g., JPY, GBP): ")
    
    # Prompt the user to input the amount to be converted and ensure it's a valid float number
    amount = float(input("Enter amount to convert: "))
    
    # Get the exchange rate for the base and target currencies by calling the function
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    
    # Convert the provided amount using the retrieved exchange rate
    converted_amount = convert_currency(amount, exchange_rate)
    
    # Display the result, formatted to two decimal places for readability
    print(f"{amount:.2f} {base_currency} is {converted_amount:.2f} {target_currency}")