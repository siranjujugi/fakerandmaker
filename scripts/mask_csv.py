import pandas as pd
from faker import Faker
import re

# Initialize Faker
fake = Faker()

# Function to detect sensitive information and mask it
def mask_sensitive_info(column, data):
    # Convert the column name to lowercase for easier comparison
    column_lower = column.lower()
    
    # Check if the column name or data suggests it's sensitive information
    if "name" in column_lower:
        return [fake.name() for _ in data]
    elif "email" in column_lower:
        return [fake.email() for _ in data]
    elif "address" in column_lower:
        return [fake.address() for _ in data]
    elif "phone" in column_lower or "mobile" in column_lower:
        return [fake.phone_number() for _ in data]
    elif "ssn" in column_lower or "social security" in column_lower:
        return [fake.ssn() for _ in data]
    elif "credit card" in column_lower or "cc" in column_lower:
        return [fake.credit_card_number() for _ in data]
    elif "dob" in column_lower or "date of birth" in column_lower:
        return [fake.date_of_birth() for _ in data]
    else:
        # Fallback to check for sensitive patterns in data
        if any(re.match(r".*@.*\..*", str(val)) for val in data):  # Detect emails
            return [fake.email() for _ in data]
        elif any(re.match(r"\d{3}-\d{2}-\d{4}", str(val)) for val in data):  # Detect SSN pattern
            return [fake.ssn() for _ in data]
        elif any(re.match(r"\d{16}", str(val)) for val in data):  # Detect credit card number
            return [fake.credit_card_number() for _ in data]
        elif any(re.match(r"\d{10}", str(val)) for val in data):  # Detect phone number pattern
            return [fake.phone_number() for _ in data]
        else:
            # Return data as-is if not detected as sensitive
            return data

# Input CSV file
input_file = 'input.csv'  # Replace with your CSV file path
df = pd.read_csv(input_file)

# Mask sensitive data
masked_df = df.apply(lambda column: mask_sensitive_info(column.name, column))

# Save the masked data to a new CSV file
masked_df.to_csv('masked_data.csv', index=False)

print("Sensitive information has been masked and saved to 'masked_data.csv'.")