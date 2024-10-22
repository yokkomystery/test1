import requests

def get_transaction_details():
    url = "https://api.example.com/transactions"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    transactions = []
    for item in data:
        transaction = {
            "日付": item["date"],
            "内容": item["details"],
            "入金": item["deposit"],
            "出金": item["withdrawal"],
            "残高": item["balance"]
        }
        transactions.append(transaction)

    return transactions
