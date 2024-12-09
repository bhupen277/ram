import requests
import time

def fetch_joke():
    url = "https://example.com/api/shayaris"  # API that provides random jokes in English

    try:
        # Fetch the joke from the API
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        joke_data = response.json()  # Parse the response to JSON

        # Extract the setup and punchline
        setup = joke_data['setup']
        punchline = joke_data['punchline']

        # Print the joke (one at a time)
        print("Here's a joke for you:\n")
        print(setup)
        time.sleep(2)  # Wait for 2 seconds before displaying punchline
        print(punchline)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the joke: {e}")

if __name__ == "__main__":
    fetch_joke()
