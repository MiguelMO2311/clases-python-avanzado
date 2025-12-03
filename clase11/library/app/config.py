import os
import configparser
from pathlib import Path
from dataclasses import dataclass

@dataclass(frozen=True)
class AppSettings:
    env: str
    data_dir: Path
    data_file: str
    encoding: str
    json_indent: int
    ensure_ascii: bool

def load_settings() -> AppSettings:
    # Carga desde config.ini
    config = configparser.ConfigParser()
    config.read("config.ini")

    app_cfg = config["app"] if "app" in config else {}

    # Lectura con prioridad .env > config.ini > defaults
    env = os.getenv("APP_ENV", app_cfg.get("env", "development"))
    data_dir = Path(os.getenv("DATA_DIR", app_cfg.get("data_dir", "./data"))).resolve()
    data_file = os.getenv("DATA_FILE", app_cfg.get("data_file", "database.json"))
    encoding = app_cfg.get("encoding", "utf-8")
    json_indent = int(app_cfg.get("json_indent", "2"))
    ensure_ascii = app_cfg.get("ensure_ascii", "false").lower() == "true"

    # Crear directorio si no existe
    data_dir.mkdir(parents=True, exist_ok=True)

    return AppSettings(
        env=env,
        data_dir=data_dir,
        data_file=data_file,
        encoding=encoding,
        json_indent=json_indent,
        ensure_ascii=ensure_ascii,
    )
