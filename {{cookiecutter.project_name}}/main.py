"""{{cookiecutter.project_name}}

This module serves as the main entry point for:

{{cookiecutter.project_description}}
"""

__author__ = "{{cookiecutter.author_name.title()}}"
__email__ = "{{cookiecutter.author_email.lower()}}"
__version__ = "{{cookiecutter.project_version}}"


import asyncio
import json
from typing import NoReturn

from aio_http.core.base import AioHttpClientManager
from aio_http.core.logger import logger

from config import Config


async def main() -> NoReturn:
    """{{cookiecutter.project_description}}"""
    url = "{{cookiecutter.site_url}}"
    outputfile = Config.OUTPUT_FILE
    try:
        # Your main application logic here
        client = AioHttpClientManager()
        client.set_headers(Config.HEADERS)
        client.set_proxies(Config.PROXIES)
        
        
        
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise


def run() -> None:
    """Execute the main application."""
    asyncio.run(main())