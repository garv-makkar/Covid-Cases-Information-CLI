import requests
import json
import pprint

# Base API URL for COVID-19 statistics
url_base = "https://covid-193.p.rapidapi.com/statistics"

# Headers for API authentication
headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "e1efe199e7msh728a1b3ef2ef874p12038fjsnb10c532921bb"  # API Key
}

# Fetching data from the API
response = requests.get(url_base, headers=headers)
data = response.json()  # Converting response to JSON format

# Function to display the number of cases in a specific country
def display_cases(country, data):
    for item in data['response']:
        if item['country'].upper() == country:
            pprint.pprint(item['cases'])
            break
    else:
        print("Country does not exist")

# Function to display the continent of a specific country
def display_continent(country, data):
    for item in data['response']:
        if item['country'].upper() == country:
            print(item['continent'])
            break
    else:
        print("Country does not exist")

# Function to display the population of a specific country
def display_population(country, data):
    for item in data['response']:
        if item['country'].upper() == country:
            print(item['population'])
            break
    else:
        print("Country does not exist")

# Function to display the number of deaths in a specific country
def display_deaths(country, data):
    for item in data['response']:
        if item['country'].upper() == country:
            pprint.pprint(item['deaths'])
            break
    else:
        print("Country does not exist")

# Function to display the number of tests conducted in a specific country
def display_tests(country, data):
    for item in data['response']:
        if item['country'].upper() == country:
            pprint.pprint(item['tests'])
            break
    else:
        print("Country does not exist")

# Function to display the number of cases in a country on a specific date
def cases_on_date(country, date):
    url_history = "https://covid-193.p.rapidapi.com/history"
    query_params = {"country": country, "day": date}
    headers_history = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "07b69b8116msh9ba68351b2f0b4dp158637jsn9f8c4233fac9"
    }
    response = requests.get(url_history, headers=headers_history, params=query_params)
    data = response.json()
    
    # Find the most recent record for the specified date
    timestamps = [int(item['time'][11:13] + item['time'][14:16]) for item in data['response']]
    if timestamps:
        max_time_index = timestamps.index(max(timestamps))
        pprint.pprint(data['response'][max_time_index])
    else:
        print("No data available for this country on the specified date")

# Function to display a list of all countries
def display_all_countries():
    url_countries = "https://covid-193.p.rapidapi.com/countries"
    response = requests.get(url_countries, headers=headers)
    data = response.json()
    pprint.pprint(data["response"])

# Main menu-driven program
while True:
    choice = int(input('''============================MENU============================
    0 -> Display all the countries
    1 -> Display Continent
    2 -> Display Population
    3 -> Display Number of Cases
    4 -> Display Number of Deaths
    5 -> Display Number of Tests Conducted
    6 -> Display Cases in a Country on a Specific Date
    ==========================================================
    Enter your choice: '''))

    # Loop to display list of countries if choice is 0
    if choice == 0:
        display_all_countries()
        choice = int(input("Please enter the operation to perform: "))

    country_name = input("Please enter the name of the country: ").upper()

    # Handle user selection
    if choice == 1:
        display_continent(country_name, data)
    elif choice == 2:
        display_population(country_name, data)
    elif choice == 3:
        display_cases(country_name, data)
    elif choice == 4:
        display_deaths(country_name, data)
    elif choice == 5:
        display_tests(country_name, data)
    elif choice == 6:
        date = input("Enter date in format yyyy-mm-dd: ")
        cases_on_date(country_name, date)
    else:
        print("Invalid choice, please try again.")

    # Ask user if they want to run another operation
    more = input("Would you like to perform another operation? (Y/N): ")
    if more.lower() == 'n':
        break
