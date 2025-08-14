import os

from dotenv import load_dotenv

load_dotenv(override=False)


class Config:
    """Config class for the application."""

    ENV = os.environ.get("ENV")

    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
    DB_HOST = os.getenv("DB_HOST", "db")
    DB_PORT = os.getenv("DB_PORT", "5434")
    DB_NAME = os.getenv("DB_NAME", "l3-db")

    DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


    AZURE_PUBSUB_CONNECTION_STRING = os.environ.get("AZURE_PUBSUB_CONNECTION_STRING")
    AZURE_PUBSUB_HUB_NAME = os.environ.get("AZURE_PUBSUB_HUB_NAME")

    ZEP_API_URL = os.environ.get("ZEP_API_URL")
    ZEP_API_KEY = os.environ.get("ZEP_API_KEY") or None

    JWT_EXPIRY = os.environ.get("JWT_EXPIRY")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

    GITHUB_CLIENT_ID = os.environ.get("GITHUB_CLIENT_ID")
    GITHUB_CLIENT_SECRET = os.environ.get("GITHUB_CLIENT_SECRET")

    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_REGION = os.environ.get("AWS_REGION")
    AWS_S3_BUCKET = os.environ.get("AWS_S3_BUCKET")

    AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

    SENTRY_DSN = os.environ.get("SENTRY_DSN")

    TEST_USER_EMAIL = os.environ.get("TEST_USER_EMAIL")
    TEST_USER_PASSWORD = os.environ.get("TEST_USER_PASSWORD")

    FRONTEND_URL = os.environ.get("FRONTEND_URL")
