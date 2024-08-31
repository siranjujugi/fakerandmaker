# fakerandmaker
A set of Python scripts to generate a random set of data based on identifying the data type of columns from the CSV files automatically and also masks the PII

# PII Detection, Random Data Generation, and Masking in CSV Files

This project provides Python scripts to:
1. **Detect Personally Identifiable Information (PII)** in a CSV file using regular expressions and heuristics.
2. **Generate Random Data** for a CSV file by identifying data types automatically.
3. **Mask Sensitive Information** in a CSV file by replacing it with random, realistic data using the `Faker` library.

## Features

- **PII Detection**: Identifies common types of PII such as emails, phone numbers, credit card numbers, SSNs, and more.
- **Random Data Generation**: Automatically detects data types from a CSV file and generates realistic random data.
- **PII Masking**: Replaces sensitive information in a CSV file with random data to ensure privacy.

## Requirements

- **Python 3.x**: Ensure you have Python installed.
- **Required Libraries**: Install the necessary libraries by running:
  ```bash
  pip install pandas faker
