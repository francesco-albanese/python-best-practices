import os
from pathlib import Path

class Config:
    def __init__(self):
        self.database_url = Path(os.getenv("DATABASE_URL", "sqlite:///default.db"))
        self.api_key = os.getenv("API_KEY")
        self.debug = os.getenv("DEBUG", "False").lower() in ('true', '1', 't')

if __name__ == "__main__":
    config = Config()
    print(f"Database URL: {config.database_url}")
    print(f"API Key: {config.api_key}")
    print(f"Debug Mode: {config.debug}")