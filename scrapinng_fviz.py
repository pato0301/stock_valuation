import requests
from bs4 import BeautifulSoup

def get_eps_5year_growth(stock):

    url = f"https://finviz.com/quote.ashx?t={stock}"

    # Set headers to mimic a typical browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Send a GET request to the URL
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the element containing "EPS next 5Y"
        target_element = soup.find('td', string='EPS next 5Y')

        # If the target_element is found, grab the next item
        if target_element:
            next_item = target_element.find_next('td')

            # Get the text content of the next item
            result_text = next_item.get_text(strip=True)

            # Remove the percentage sign and convert to float
            result_float = float(result_text.rstrip('%'))

            #print("Value after 'EPS next 5Y' as float:", result_float)
            return result_float
        else:
            #print("Target not found on the page.")
            return 0
    else:
        #print("Failed to fetch the web page. Status code:", response.status_code)
        return 0

def get_yield_corporate_bonds_aaa():

    url = "https://ycharts.com/indicators/us_coporate_aaa_effective_yield"

    # Set headers to mimic a typical browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Send a GET request to the URL
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the element containing "EPS next 5Y"
        target_element = soup.find('td', string='Last Value')

        # If the target_element is found, grab the next item
        if target_element:
            next_item = target_element.find_next('td')

            # Get the text content of the next item
            result_text = next_item.get_text(strip=True)

            # Remove the percentage sign and convert to float
            result_float = float(result_text.rstrip('%'))

            #print("Value after 'EPS next 5Y' as float:", result_float)
            return result_float
        else:
            #print("Target not found on the page.")
            return 0
    else:
        #print("Failed to fetch the web page. Status code:", response.status_code)
        return 0