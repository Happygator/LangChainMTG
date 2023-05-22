import requests
import scrython

query = "legal:standard"
"""
def get_all_card_names():
    url = "https://api.scryfall.com/catalog/card-names"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        card_names = response.json()
        return card_names
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
"""
def get_all_card_names():
    cardnames = []
    search = scrython.cards.Search(q=query)
    pagenumber = 1
    while True:
        for i in search.data():
            cardnames.append(i['name'])
        if not search.has_more():
            break
        pagenumber += 1
        search = scrython.cards.Search(q=query, page=pagenumber)
    return cardnames


# Example usage
if __name__ == '__main__':
    all_card_names = get_all_card_names()

    # Display the total number of card names retrieved
    print(len(all_card_names))
    print(all_card_names[:10])
