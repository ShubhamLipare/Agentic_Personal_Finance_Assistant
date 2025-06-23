# Classifies expenses from CSV
from langchain_core.tools import tool
import pandas as pd
import os

@tool
def analyze_spending(csv_path:str)->str:
    "Analyze spending patterns from a user-uploaded expense CSV."
    
    if not os.path.exists(csv_path):
        return "File path not find."
    
    try:
        df=pd.read_csv(csv_path)

        if "Amount" not in df.columns or "Category" not in df.columns:
            return "csv file must contain Amount and Category columns "
        
        df["Amount"]=pd.to_numeric(df["Amount"],errors='coerce')
        df.dropna(subset=["Amount"],inplace=True)

        category_summary=df.groupby("Category")["Amount"].sum().sort_values(ascending=True)
        total_spent=category_summary.sum()

        summary_lines=[f"Total Spending: ₹{total_spent:.2f}\n"]

        for cat,amount in category_summary.items():
            summary_lines.append(f"{cat}:Rs.{amount}")

        return "\n".join(summary_lines)
        
    except Exception as e:
        return f"Error:{str(e)}"
    