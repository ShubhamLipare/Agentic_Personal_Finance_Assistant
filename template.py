import os

# Define the folder structure
folders = [
    "agents",
    "tools",
    "memory",
    "database",
    "api",
    "ui",
    "rag",
    "langgraph_workflow",
    "data/sample_csv"
]

files = {
    "agents/__init__.py": "",
    "agents/budget_agent.py": "# Handles budget planning logic\n",
    "agents/goal_agent.py": "# Handles user goal-based savings\n",
    "agents/investment_agent.py": "# Suggests investments using tools\n",
    "agents/spending_analyzer.py": "# Classifies expenses from CSV\n",

    "tools/__init__.py": "",
    "tools/coingecko_tool.py": "# Real-time crypto prices from CoinGecko\n",
    "tools/yahoo_finance_tool.py": "# Live stock/ETF prices using Yahoo Finance API\n",

    "memory/__init__.py": "",
    "memory/memory_setup.py": "# LangGraph MemorySaver setup\n",

    "database/__init__.py": "",
    "database/models.py": "# SQLAlchemy models for chat, user goals, etc.\n",
    "database/db_utils.py": "# DB connection + helper functions\n",

    "api/__init__.py": "",
    "api/main.py": "# FastAPI app to interact with frontend/backend logic\n",

    "ui/__init__.py": "",
    "ui/app.py": "# Streamlit UI\n",

    "rag/__init__.py": "",
    "rag/expense_rag.py": "# RAG pipeline for parsing/uploading CSVs\n",

    "langgraph_workflow/__init__.py": "",
    "langgraph_workflow/graph_builder.py": "# Graph definition with agents + memory\n",

    "requirements.txt": "# Add dependencies here\n",
    "README.md": "# Personal Finance Assistant (Agentic AI with RAG, LangGraph, Groq, Streamlit, FastAPI)\n",
}

def create_structure():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    for file_path, content in files.items():
        with open(file_path, "w") as f:
            f.write(content)

    print("Project structure created successfully!")

if __name__ == "__main__":
    create_structure()
