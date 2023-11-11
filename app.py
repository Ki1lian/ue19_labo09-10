# Libraries :
import requests, json


def main():
    response = requests.get("https://punapi.rest/api/pun")  # Make a http get request
    response = json.loads(response.text)  # Convert the http get object json answer into dictionary
    print("The pun of the moment is :", response["pun"])  # Print the pun got form punapi.rest


if __name__ == '__main__':
    main()
