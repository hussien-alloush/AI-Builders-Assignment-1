# AI Builders Bootcamp — Assignment 1

## Python Fundamentals

This repository contains Assignment 1 of the AI Builders Bootcamp, focused on applying Python fundamentals to a structured student dataset.

## Topics Covered

- Lists, dictionaries, and nested data structures
- Loops and conditional statements
- Filtering and list comprehensions
- Data aggregation and transformation
- Sets and unique values
- Reusable functions
- Sorting and basic data pipelines

## Project Structure

```text
AI-Builders-Assignment-1/
├── data/           # Student dataset
├── part_1/         # Exploring the data
├── part_2/         # Filtering
├── part_3/         # Aggregating
├── part_4/         # Transforming
├── part_5/         # Reusable functions
├── Bonus/          # Mini data pipeline
├── .gitignore
├── requirements.txt
└── README.md
```

## Requirements

- Python 3
- No external Python packages required for the assignment

## Environment Setup

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install any listed dependencies:

```bash
pip install -r requirements.txt
```

## Running the Assignment

From the project root directory, execute:

```bash
python -m part_1.Exploring_the_data
python -m part_2.Filtering
python -m part_3.Aggregating
python -m part_4.Transforming
python -m part_5.Reusable_functions
python -m Bonus.Mini_data_pipeline
```

## Dataset

The assignment uses a list of student dictionaries containing names, ages, learning tracks, study hours, and assessment scores.

## Mini Data Pipeline

The bonus exercise implements a reusable data pipeline that filters student records, calculates average scores, transforms data, and sorts results by performance.

**Filter → Transform → Aggregate → Sort**

## AI Assistance

ChatGPT was used for guided learning, debugging, code review, and documentation support.