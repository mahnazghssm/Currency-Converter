# Currency Converter Tool

## Overview

This project provides a simple currency conversion tool built with Python and Streamlit. It leverages the ExchangeRate API to fetch real-time exchange rates and perform currency conversions. The tool allows users to convert amounts between different currencies using an intuitive web interface.

## Features

- **Real-Time Conversion**: Fetches and uses real-time exchange rates to provide accurate currency conversions.
- **Interactive Interface**: Built with Streamlit for a user-friendly web interface.
- **Caching**: Utilizes caching to minimize API calls and improve performance.
- **Wide Range of Currencies**: Supports a comprehensive list of currencies.

## Components

### `currency_converter.py`

Contains functions for fetching exchange rates and converting amounts.

- `get_exchange_rate(base_currency, target_currency)`: Fetches the exchange rate for converting from `base_currency` to `target_currency`.
  - **Parameters**:
    - `base_currency` (str): The currency you are converting from (e.g., "USD").
    - `target_currency` (str): The currency you are converting to (e.g., "EUR").
  - **Returns**: 
    - `float`: The exchange rate between the base and target currencies.
    - `None`: If the API request fails or the target currency is not available.

- `convert_currency(amount, exchange_rate)`: Converts a given amount using the provided exchange rate.
  - **Parameters**:
    - `amount` (float): The amount of money to convert.
    - `exchange_rate` (float): The exchange rate between the base and target currencies.
  - **Returns**: `float` - The converted amount in the target currency.

### `constants.py`




Contains a list of supported currencies:

```python
currencies = [
    'USD', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 
    'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 
    'BRL', 'BSD', 'BTN', 'BWP', 'BYN', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 
    'CNY', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD', 
    'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'FOK', 'GBP', 'GEL', 'GGP', 
    'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 
    'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 
    'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KID', 'KMF', 'KRW', 'KWD', 'KYD', 
    'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL', 'MGA', 
    'MKD', 'MMK', 'MNT', 'MOP', 'MRU', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 
    'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 
    'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 
    'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 
    'SRD', 'SSP', 'STN', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 
    'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU', 'UZS', 'VES', 
    'VND', 'VUV', 'WST', 'XAF', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 
    'ZMW', 'ZWL'
]
```

### `app.py`

Creates a Streamlit web application for the currency converter.

	•	Title: Sets the title of the Streamlit app with a dollar emoji.
	•	Description: Provides a brief description of the tool’s functionality.
	•	Dropdown Menus: Allows users to select base and target currencies.
	•	Amount Input: Lets users enter the amount to convert.
	•	Conversion and Display: Fetches exchange rates, performs conversion, and displays the result.

## Installation

1.	Clone the repository:

    git clone https://github.com/your-username/currency-converter.git
    cd currency-converter

2.	Install the required packages:

    pip install requests cachetools streamlit

3.	Run the Streamlit app:

    streamlit run app.py

## Usage

•	Open the Streamlit application in your browser.
•	Select the base currency and target currency from the dropdown menus.
•	Enter the amount you wish to convert.
•	The converted amount and the exchange rate will be displayed.

## License

This project is licensed under the MIT License.

## Acknowledgments

•	ExchangeRate API for providing real-time exchange rates.

•	Streamlit for creating the web interface.







