# Task 1: Price Updates

## Problem Statement

You are given an SQL table containing changes in prices of articles in a shop with the following structure:

| Column      | Type      |
|-------------|-----------|
| product     | varchar   |
| date        | date      |
| price       | int       |

Write an SQL query that lists all articles whose price increased with every update.

### Example:

#### Given the table:

| product          | date       | price |
|------------------|------------|-------|
| banana [single]  | 2020-01-21 | 1     |
| banana [single]  | 2020-01-22 | 2     |
| cheese           | 2020-01-23 | 1     |
| potatoes [pack]  | 2020-01-21 | 3     |
| potatoes [pack]  | 2020-01-30 | 3     |

#### Your query should return:

| product          |
|------------------|
| banana [single]  |

#### Explanation:
- The price of "banana [single]" increased with every update.
- The price of "cheese" was entered only once, so there was not enough data to determine whether it was increasing.
- The price of "potatoes [pack]" did not increase with every update, as it remained the same on the second date.

## Running the Task

### Steps:
1. Create the table and populate it with data using the Python scripts:
```bash
python -m tasks.task1_price_updates.setup.create_tables
python -m tasks.task1_price_updates.setup.insert_data
```
2. Run the main query to find products with strictly increasing prices:
```powershell
$env:PYTHONPATH = (Get-Location).Path; task1_run_main
```
```bash
PYTHONPATH=$(pwd) task1_run_main
```
