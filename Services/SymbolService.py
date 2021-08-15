import requests

def get_symbol_data(symbol, api_key):

    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={symbol}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()["bestMatches"]
    print("Enter the number corresponding to the required symbol.\n")

    resultDict = {}
    for i, result in enumerate(data, start=1):
        resultDict[i] = result
        print(i, "  ", result["2. name"])

    symbolId = int(input())
    print(f'{resultDict[symbolId]["2. name"]} is selected.')
    return resultDict[symbolId]