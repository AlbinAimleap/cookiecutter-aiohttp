from pathlib import Path

CURRENT_DIR = Path(__file__)

output_dir = CURRENT_DIR / "output"
output_dir.mkdir(exist_ok=True) 

class Config:
    OUTPUT_FILE = output_dir / "{{cookiecutter.output_file_name}}"
    HEADERS = {}
    PROXIES = {}