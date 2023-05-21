import requests
import csv
import string
# import pandas
import get_all_card_names
cardFile = open("cards.csv", 'w')
writer = csv.writer(cardFile, quoting=csv.QUOTE_ALL)
importantKeys = ['name', 'mana_cost', 'type_line', 'oracle_text']
header = ['name', 'mana_cost', 'type_line', 'oracle_text', 'power', 'toughness', 
'name2', 'mana_cost2', 'type_line2', 'oracle_text2', 'power2', 'toughness2']
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
    return {}        

def flat(card_info):
    row = {}
    if 'card_faces' in card_info:
        for i,face in enumerate(card_info['card_faces']):
            for key in importantKeys:
                row[key+str(i)] = remove_unprintable(face[key])
    else:
        for key in importantKeys:
            row[key+'0'] = remove_unprintable(card_info[key])
    return row

def dictionaries_to_csv(dictionaries, output_file):
    # Extract all unique keys from the dictionaries
    keys = set().union(*dictionaries)

    # Open the output CSV file in write mode
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)

        # Write the header row
        writer.writeheader()

        # Write each dictionary as a row in the CSV file
        for dictionary in dictionaries:
            
            writer.writerow(dictionary)

def remove_unprintable(str):
    return str.replace('\u2212', '-')



# Example usage
if __name__ == '__main__':
    cards_names = get_all_card_names.get_all_card_names()['data'][:100]
    cards = [get_card_info(c) for c in cards_names]
    cards = [flat(c) for c in cards]
    dictionaries_to_csv(cards, "data/sample.csv")


    # writer.writerow(header)

    # card_name = "Suspicious Stowaway // Seafaring Werewolf"

    # card_info = get_card_info(card_name)
    # row = []
    # if 'card_faces' in card_info:
    #     for face in card_info['card_faces']:
    #         for key in importantKeys:
    #             row.append(face[key])
    #         if 'power' in card_info:
    #             row += [face['power'], face['toughness']]
    #         else:
    #             row += [None, None]
    # else:
    #     for key in importantKeys:
    #         row.append(card_info[key])
    #     if 'power' in card_info:
    #         row += [card_info['power'], card_info['toughness']]
    #     else:
    #         row += [None, None]
    #     row += [None] * 6
    # writer.writerow(row)
        