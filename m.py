import requests
from bs4 import BeautifulSoup
import random

def fetch_poems():
    try:
        # URL of the poetry website
        url = "https://www.amarujala.com/kavya"
        
#         # Send a GET request to fetch the website's content
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract poetry titles or content - adjust based on the site's structure
        # Example: Extract titles from <h3> tags with a specific class
        poem_elements = soup.find_all('h3', class_='post-title')

        # Collect the text and links for each poem
        poems = [{"title": poem.get_text(strip=True), "link": poem.find('a')['href']} for poem in poem_elements]

        # Check if any poems were found
        if not poems:
            print("No poems found on the website. Please check the structure of the page.")
            return

        # Pick one poem randomly
        selected_poem = random.choice(poems)

        # Print the title and the link
        print("\nHere's a Poem for you:\n")

        print(f"Title: {selected_poem['title']}")
        print(f"Read more: {selected_poem['link']}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_poems()
