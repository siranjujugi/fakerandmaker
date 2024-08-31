import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Function to identify data type and generate random data
def generate_data(column, dtype, num_rows):
    data = []
    for _ in range(num_rows):
        if pd.api.types.is_integer_dtype(dtype):
            data.append(random.randint(1, 100))  # Generating a random integer
        elif pd.api.types.is_float_dtype(dtype):
            data.append(random.uniform(1.0, 100.0))  # Generating a random float
        elif pd.api.types.is_datetime64_any_dtype(dtype):
            data.append(fake.date_time())  # Generating a random datetime
        elif pd.api.types.is_bool_dtype(dtype):
            data.append(fake.boolean())  # Generating a random boolean
        elif pd.api.types.is_string_dtype(dtype):
            if "name" in column.lower():
                data.append(fake.name())  # Generating a random name
            elif "email" in column.lower():
                data.append(fake.email())  # Generating a random email
            elif "address" in column.lower():
                data.append(fake.address())  # Generating a random address
            elif "phone" in column.lower():
                data.append(fake.phone_number())  # Generating a random phone number
            else:
                data.append(fake.word())  # Generating a random word for other strings
        else:
            data.append(fake.text())  # Fallback to random text for unsupported types
    return data

# Input CSV file
input_file = 'input.csv'  # Replace with your CSV file path
df = pd.read_csv(input_file)

# Get the number of rows to generate
num_rows = int(input("Enter the number of rows to generate: "))

# Dictionary to store the generated data
generated_data = {}

# Iterate over each column and generate data based on its data type
for column in df.columns:
    dtype = df[column].dtype
    generated_data[column] = generate_data(column, dtype, num_rows)

# Create a DataFrame with the generated data
generated_df = pd.DataFrame(generated_data)

# Save the generated data to a new CSV file
generated_df.to_csv('generated_data.csv', index=False)

print(f"Generated {num_rows} rows of random data and saved to 'generated_data.csv'.")
