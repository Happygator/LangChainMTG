import requests

def get_all_card_names():
    url = "https://api.scryfall.com/catalog/card-names"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        card_names = response.json()
        return card_names
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")



# Example usage
if __name__ == '__main__':
    all_card_names = get_all_card_names()

    # Display the total number of card names retrieved
    print(len(all_card_names['data']))
    print(all_card_names['data'][:10])
