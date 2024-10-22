import os
import csv
from fpdf import FPDF
from api_stub import get_transaction_details

def generate_csv(transactions, output_dir):
    csv_file = os.path.join(output_dir, "transactions.csv")
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["日付", "内容", "入金", "出金", "残高"])
        writer.writeheader()
        for transaction in transactions:
            writer.writerow(transaction)

def generate_pdf(transactions, output_dir):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('Arial', '', 'arial.ttf', uni=True)
    pdf.set_font('Arial', '', 12)
    pdf.cell(200, 10, txt="銀行入出金明細", ln=True, align='C')

    for transaction in transactions:
        pdf.cell(200, 10, txt=f"日付: {transaction['日付']}, 内容: {transaction['内容']}, 入金: {transaction['入金']}, 出金: {transaction['出金']}, 残高: {transaction['残高']}", ln=True)

    pdf_file = os.path.join(output_dir, "transactions.pdf")
    pdf.output(pdf_file)

def main():
    transactions = get_transaction_details()
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    generate_csv(transactions, output_dir)
    generate_pdf(transactions, output_dir)

if __name__ == "__main__":
    main()
