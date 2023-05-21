import requests

def get_card_info(card_name):
    # Replace spaces in the card name with '+' to form the query string
    query = card_name.replace(' ', '+')
    
    # Construct the URL for the card search endpoint
    url = f"https://api.scryfall.com/cards/named?fuzzy={query}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        
        card_info = response.json()
        return card_info
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
card_name = "Black Lotus"
card_info = get_card_info(card_name)

# Display relevant information about the card
print("Card Name:", card_info["name"])
print("Mana Cost:", card_info["mana_cost"])
print("Type Line:", card_info["type_line"])
print("Oracle Text:", card_info["oracle_text"])
