# Suggests investments using tools
from langchain_core.tools import tool

@tool
def investment_advisor(monthly_amount: str, risk_profile: str = "medium") -> str:

    """Suggests investment options based on monthly amount and user's risk profile."""
    try:
        amount = float(monthly_amount)
        risk = risk_profile.lower()

        if amount < 1000:
            return "Minimum suggested investment is ₹1,000."

        if risk not in {"low", "medium", "high"}:
            risk = "medium"

        response = [f"Investment Plan for ₹{amount:.2f}/month ({risk.title()} Risk)"]

        if risk == "low":
            response.extend([
                "60%: Bank FD or Post Office RD (Safe, ~6.5% returns)",
                "30%: Short-term Debt Mutual Funds (Low volatility)",
                "10%: Gold ETF or Sovereign Gold Bonds"
            ])
        elif risk == "medium":
            response.extend([
                "50%: Mutual Fund SIP (Balanced or Flexi Cap)",
                "30%: Gold ETF or Index Funds (Nifty/Sensex)",
                "20%: Crypto (e.g., Bitcoin, Ethereum, small allocation)"
            ])
        elif risk == "high":
            response.extend([
                "40%: Crypto (Bitcoin, Ethereum, MATIC)",
                "40%: Small-cap Stocks or Thematic ETFs",
                "20%: Mutual Fund SIP (Aggressive Growth Fund)"
            ])

        response.append("\n🧠 Tip: Rebalance every 3–6 months based on performance.")

        return "\n".join(response)

    except Exception as e:
        return f"Error while generating investment suggestions: {str(e)}"


