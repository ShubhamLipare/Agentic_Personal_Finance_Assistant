# Handles user goal-based savings
from langchain_core.tools import tool

@tool
def goal_advisor(goal_amount:str,months:str='auto',top_categories:str="")->str:
    """Suggests a saving plan based on user financial goal."""
    try:
        amount=float(goal_amount)

        if months=="auto":
            if amount<20000:
                months=3
            elif amount<50000:
                months=6

            else:
                months=12
        else:
            months=int(months)

        categories = top_categories.split(",") if top_categories else ["Food", "Entertainment"]
        categories = [cat.strip().title() for cat in categories]

        monthly_saving=round(amount/months,2)
        response = [
            f"To save ₹{amount:.2f},",
            f"You need to save ₹{monthly_saving:.2f} per month for {months} months.",
            "",
            "Personalized budgeting tips:"
        ]
        if categories:
            response.append(f"- Cut down 10–20% from top expenses like {', '.join(categories[:2])}")
        response.extend([
            "- Set up monthly auto-transfer to savings",
            "- Avoid unplanned purchases above ₹1,000",
            "",
            "🔍 Want smart investment suggestions to reach your goal faster?"
        ])
        return "\n".join(response)

    except Exception as e:
        return f"Error:{str(e)}"
    