# CS50 Final Project – Stock Analyzer

Currently in development. Python app that uses API data to display and analyze historical stock prices.

Status: Core logic and API integration in progress.

# Requirements
To run the DCF Stock Analyzer, you need Python 3.9 or higher and the packages streamlit, requests, python-dotenv, as well as the standard libraries os and time.
Make sure you have valid API keys for both Alpha Vantage and FRED.

- Create a file named .env in the project directory containing:
ALPHA_API_KEY=your_alpha_vantage_key \
FRED_API_KEY=your_fred_key

-These keys are loaded in the script using
import requests \
import os \
import time \
from dotenv import load_dotenv \

- After installing the requirements and adding your API keys, you can start the web application with: 
streamlit run main.py

# Update 4 (11.10.2025):

Added a Streamlit web application with improved error handling.
Introduced a simple DCF analyzer web interface built with Streamlit and added basic input validation and error messages for missing or invalid data.

# Update 3 (30.07.2025): 

Core functionality has been implemented successfully and is producing initial results. The current focus is on:

- Improving calculation logic and overall stability
- Handling API rate limits (Alpha Vantage)
- Refactoring for better code structure and reusability

# AI Usage

Artificial intelligence tools (such as ChatGPT) have been used exclusively for debugging support and syntax clarification during development.
All core logic, architectural decisions, and code structure have been designed and implemented independently by the developer.
The goal is to strengthen personal programming and problem-solving skills while using AI as a learning and troubleshooting assistant — not as a code generator.

# Update 2 (28.07.2025): 

- First working version of Free Cash Flow history and CAGR logic
- Growth assumptions and average FCF margins integrated
- Connected FRED API for 10-year treasury yield as risk-free rate

# Update 1 (23.07.2025): Switched from yfinance to Alpha Vantage

Switched because yfinance does not provide enough data for a professional DCF calculation.



