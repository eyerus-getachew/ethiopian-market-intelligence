"""Project paths and settings."""
from pathlib import Path
import os
import yaml
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = ROOT / "data" / "raw"
DATA_INTERIM = ROOT / "data" / "interim"
DATA_PROCESSED = ROOT / "data" / "processed"
DATA_ANNOTATED = ROOT / "data" / "annotated"

load_dotenv(ROOT / ".env")

TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
TELEGRAM_SESSION_NAME = os.getenv("TELEGRAM_SESSION_NAME", "emi_session")


def load_channels_config() -> dict:
    with open(ROOT / "configs" / "channels.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)
