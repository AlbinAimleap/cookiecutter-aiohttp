from pathlib import Path

CURRENT_DIR = Path(__file__)

output_dir = CURRENT_DIR / "output"
if not output_dir.exists():
    output_dir.mkdir(parents=True)

class Config:
    OUTPUT_FILE = output_dir / "output.json"
    HEADERS = {}
    PROXIES = {}