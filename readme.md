# SQL Project

## Overview

This project is designed to solve various SQL-related tasks using Python and PostgreSQL. It focuses on practical exercises that involve creating, managing, and interacting with SQL databases. Each task is organized into modular components for better scalability and code management.

## Features

- Modular task-based structure for scalability.
- Use of SQLAlchemy for database interaction.
- PostgreSQL as the primary database backend.
- Logging setup using the `loguru` library.
- `flake8` and `black` for linting and code formatting.
- Easily extensible for new tasks and SQL challenges.

## Project Structure
```r
|   .flake8
|   logging_config.py             # Centralized logging configuration for all tasks.
|   pyproject.toml                # Project dependencies and configuration.
|   readme.md
|   
+---.vscode
|       labs1_SQL.code-workspace
|       launch.json
|       settings.json
|       
+---database                      # Contains PostgreSQL configuration and Docker setup files.
|   |   .env
|   |   docker-sompose.yml
|   |   
|   +---config
|           pg_hba.conf
|           postgresql.conf
|
+---logs
+---scripts                       # Bash scripts for managing the database lifecycle.
|       clean_db.sh
|       clean_pycache.py
|       restart_db.sh
|       start_db.sh
|       stop_db.sh
|       
+---tasks                         # # Directory for modular SQL tasks, with separate subdirectories for each task.
    +---task1_price_updates
        |   main.py
        |   readme_task1.md
        |   
        +---setup
                create_tables.py
                insert_data.py
                models.py
                __init__.py
```

## Setup Instructions

1. Create a virtual environment:
```bash
   python -m venv venv
```
2. Activate the virtual environment:<br>
On Windows: `.\venv\Scripts\activate`<br>
On Linux/Mac: `source ./venv/bin/activate`
3. Upgrade pip and setuptools:
```bash
   python -m pip install --upgrade pip setuptools
```
4. Install dependencies:
```bash
   pip install -e .
   pip install -e .[flake8]
```
