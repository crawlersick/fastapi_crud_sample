tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]


from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    ENVIRONMENT: str
    db1url: str = "sqlite:///./sql_app.db"

    class Config:
        env_file = os.getenv("running_env", "test") + ".env"


