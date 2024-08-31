import re
import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Function to parse DDL and extract column names and their data types
def parse_ddl(ddl):
    # Regular expression to extract column name and data type
    column_pattern = re.compile(r"(\w+)\s+(\w+)")
    columns = column_pattern.findall(ddl)
    return columns

# Function to generate random data based on data type
def generate_data_by_type(data_type, num_rows):
    data = []
    for _ in range(num_rows):
        if data_type.startswith('INT') or data_type.startswith('BIGINT'):
            data.append(random.randint(1, 100))  # Random integer
        elif data_type.startswith('FLOAT') or data_type.startswith('DOUBLE'):
            data.append(random.uniform(1.0, 100.0))  # Random float
        elif data_type.startswith('DATE'):
            data.append(fake.date())  # Random date
        elif data_type.startswith('DATETIME') or data_type.startswith('TIMESTAMP'):
            data.append(fake.date_time())  # Random datetime
        elif data_type.startswith('CHAR') or data_type.startswith('VARCHAR') or data_type.startswith('TEXT'):
            data.append(fake.text(max_nb_chars=20))  # Random text
        elif data_type.startswith('BOOLEAN'):
            data.append(fake.boolean())  # Random boolean
        elif data_type.startswith('DECIMAL') or data_type.startswith('NUMERIC'):
            data.append(round(random.uniform(1.0, 100.0), 2))  # Random decimal
        else:
            data.append(fake.word())  # Fallback random word for any other types
    return data

# Input: DDL statement (as a string)
ddl_statement = """
CREATE TABLE example_table (
    id INT,
    name VARCHAR(255),
    email VARCHAR(255),
    birth_date DATE,
    salary DECIMAL(10, 2),
    is_active BOOLEAN
);
"""

# Number of rows to generate
num_rows = int(input("Enter the number of rows to generate: "))

# Parse the DDL to get column names and types
columns = parse_ddl(ddl_statement)

# Dictionary to store generated data for each column
generated_data = {}

# Generate random data for each column based on its type
for column_name, data_type in columns:
    generated_data[column_name] = generate_data_by_type(data_type, num_rows)

# Create a DataFrame with the generated data
generated_df = pd.DataFrame(generated_data)

# Save the generated data to a CSV file
generated_df.to_csv('generated_data_from_ddl.csv', index=False)

print(f"Generated {num_rows} rows of random data based on the DDL and saved to 'generated_data_from_ddl.csv'.")
