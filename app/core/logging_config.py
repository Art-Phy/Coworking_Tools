
import logging
from logging.config import dictConfig

LOG_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(levelname)s] %(asctime)s — %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "access": {
            "format": '%(asctime)s | %(client_addr)s | "%(request_line)s" %(status_code)s',
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

def init_logging():
    dictConfig(LOG_CONFIG)
    logging.info("Logging inicializado correctamente 🚀")
