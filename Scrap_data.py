import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch the page, status code: {response.status_code}")

def parse_property_details(html):
    soup = BeautifulSoup(html, 'html.parser')
    properties = []

    # Find the property listings
    listings = soup.find_all('article', class_='resultBody')

    for listing in listings:
        # Extract property details
        price = listing.find('span', class_='priceText').get_text(strip=True) if listing.find('span', class_='priceText') else "N/A"
        address = listing.find('a', class_='residential-card__address-heading').get_text(strip=True) if listing.find('a', class_='residential-card__address-heading') else "N/A"
        beds = listing.find('span', class_='general-features__beds').get_text(strip=True) if listing.find('span', class_='general-features__beds') else "N/A"
        baths = listing.find('span', class_='general-features__baths').get_text(strip=True) if listing.find('span', class_='general-features__baths') else "N/A"
        cars = listing.find('span', class_='general-features__cars').get_text(strip=True) if listing.find('span', class_='general-features__cars') else "N/A"
        agent = listing.find('span', class_='agent__name').get_text(strip=True) if listing.find('span', class_='agent__name') else "N/A"

        # Add to the list
        properties.append({
            'Price': price,
            'Address': address,
            'Bedrooms': beds,
            'Bathrooms': baths,
            'Car Spaces': cars,
            'Agent': agent
        })

    return properties

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    url = "https://www.realestate.com.au/buy/in-epping,+nsw+2121/list-1"
    html_content = fetch_html(url)
    properties = parse_property_details(html_content)
    save_to_csv(properties, 'epping_properties.csv')
