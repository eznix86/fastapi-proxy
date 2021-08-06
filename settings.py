import os

from dotenv import load_dotenv

# from pydantic import BaseSettings

# settings = BaseSettings(_env_path=_env_path)


_env_path = ".env"

if not os.path.exists(".env"):
    _env_path = ".env.sample"

load_dotenv(_env_path)

HOST, PORT = "localhost", 8081

PROXY_URL = str(os.environ.get("PROXY_URL"))
PROXY_STATUS = os.environ.get("PROXY_STATUS")
BODY = os.environ.get("PROXY_BODY")
DEBUG = bool(os.environ.get("DEBUG"))
