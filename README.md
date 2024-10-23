
# Cookiecutter AIOHTTP

A Cookiecutter template for creating AIOHTTP applications with best practices.


## Usage

First, make sure you have cookiecutter installed:

```bash
pip install cookiecutter
```

Then generate your project:
```bash
cookiecutter https://github.com/AlbinAimleap/cookiecutter-aiohttp
```

You'll be prompted for basic info about your project:

- project_name: Your project name
- project_slug: The name used in setup.py and other files
- schema_model: Schema model name
- project_description: A brief description of your project
- site_url: Url for the site you are scraping
- output_file_name: outputfilename
- author_name: Your name
- author_email: Your email
- project_version: version for your project
- logger_name: name of the logger
- python_version: Initial version of your project

## Project Structure
```
project/
    ├── README.md
    ├── requirements.txt
    ├── main.py
    ├── schema.py
    ├── aio_http/
        ├── __init__.py
        ├── core/
            ├── __init__.py
            ├── base.py
            ├── schema.py
            └── logger.py
```

## Happy Coding ;)


