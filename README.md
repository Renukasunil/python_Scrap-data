# python_Scrap-data
fetch_html(url)
This function takes a URL as input, makes an HTTP GET request to the URL, and returns the HTML content of the page if the request is successful. If the request fails, it raises an exception with the status code.

parse_property_details(html)
This function takes the HTML content of a page as input and uses BeautifulSoup to parse the HTML. It extracts the property details such as price, address, number of bedrooms, bathrooms, car spaces, and agent details. It returns a list of dictionaries, each containing the details of one property.

save_to_csv(data, filename)
This function takes a list of dictionaries (data) and a filename as input. It converts the list of dictionaries to a pandas DataFrame and saves it as a CSV file with the given filename.

Main Script
The main script defines the URL for the search results of properties in Epping. It fetches the HTML content, parses the property details, and saves 
