def get_transaction_details():
    transactions = []
    balance = 300000
    for i in range(1000):
        date = f"2023-01-{i % 30 + 1:02d}"
        details = f"取引内容{i + 1}"
        deposit = 0 if i % 2 == 0 else 10000
        withdrawal = 10000 if i % 2 == 0 else 0
        balance += deposit - withdrawal
        transactions.append({"日付": date, "内容": details, "入金": deposit, "出金": withdrawal, "残高": balance})
    return transactions
