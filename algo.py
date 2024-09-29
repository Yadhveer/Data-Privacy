import numpy as np
import pandas as pd

# Define membership functions for fuzzy sets
def fuzzy_membership_age(age):
    return {
        'Low': max(0, min(1, (30 - age) / 10)),
        'Medium': max(0, min(1, (age - 25) / 10, (35 - age) / 10)),
        'High': max(0, min(1, (age - 30) / 10))
    }

def fuzzy_membership_income(income):
    return {
        'Low': max(0, min(1, (40000 - income) / 10000)),
        'Medium': max(0, min(1, (income - 50000) / 10000, (70000 - income) / 10000)),
        'High': max(0, min(1, (income - 60000) / 10000))
    }

def fuzzy_membership_purchases(purchases):
    return {
        'Low': max(0, min(1, (10 - purchases) / 5)),
        'Medium': max(0, min(1, (purchases - 10) / 5, (15 - purchases) / 5)),
        'High': max(0, min(1, (purchases - 15) / 5))
    }

# Step 1: Convert quantitative data into fuzzy sets
def convert_to_fuzzy(data):
    fuzzy_data = []
    for entry in data:
        age_fuzzy = fuzzy_membership_age(entry[0])
        income_fuzzy = fuzzy_membership_income(entry[1])
        purchases_fuzzy = fuzzy_membership_purchases(entry[2])
        fuzzy_data.append((age_fuzzy, income_fuzzy, purchases_fuzzy))
    return fuzzy_data

# Step 2: Identify sensitive transactions based on restrictive rules
def identify_sensitive_transactions(fuzzy_data, restrictive_rules):
    sensitive_transactions = []
    for index, fuzzy_entry in enumerate(fuzzy_data):
        # Check if the entry conflicts with any restrictive rules
        for rule in restrictive_rules:
            if rule in fuzzy_entry:
                sensitive_transactions.append((index, fuzzy_entry))
                break  # No need to check other rules if one is matched
    return sensitive_transactions

# Step 3: Select victim items based on fuzzy membership
def select_victim_items(sensitive_transactions, threshold):
    victim_items = []
    for transaction in sensitive_transactions:
        index, fuzzy_entry = transaction
        # Select victim items based on the highest membership grade
        max_item = max(fuzzy_entry, key=lambda x: max(fuzzy_entry[x]))
        if max(fuzzy_entry[max_item]) > threshold:
            victim_items.append((index, max_item))
    return victim_items

# Step 4: Calculate number of transactions to sanitize
def calculate_num_transactions(sensitive_count, sanitization_threshold):
    return int(sensitive_count * (1 - sanitization_threshold))

# Step 5: Sort transactions by degree of conflict
def sort_transactions(sensitive_transactions):
    sorted_transactions = sorted(
        sensitive_transactions,
        key=lambda x: sum(max(membership for membership in x[1].values())),  # Sum of memberships
        reverse=True
    )
    return sorted_transactions

# Step 6: Perform fuzzy sanitization
def sanitize_transactions(transactions, reduction_factor):
    for transaction in transactions:
        index, fuzzy_entry = transaction
        # Reduce the fuzzy membership grade based on the reduction factor
        for item in fuzzy_entry:
            fuzzy_entry[item] *= (1 - reduction_factor)  # Adjust membership
    return transactions

# Main function to execute the sanitization process
def main(data, restrictive_rules, sanitization_threshold, reduction_factor):
    # Step 1: Convert quantitative data into fuzzy sets
    fuzzy_data = convert_to_fuzzy(data)

    # Step 2: Identify sensitive transactions
    sensitive_transactions = identify_sensitive_transactions(fuzzy_data, restrictive_rules)

    # If no sensitive transactions, return original data
    if not sensitive_transactions:
        print("No sensitive transactions found.")
        return data

    # Step 4: Calculate number of transactions to sanitize
    num_transactions_to_sanitize = calculate_num_transactions(len(sensitive_transactions), sanitization_threshold)

    # Step 5: Sort transactions by degree of conflict
    sorted_transactions = sort_transactions(sensitive_transactions)

    # Step 6: Select the transactions to sanitize
    transactions_to_sanitize = sorted_transactions[:num_transactions_to_sanitize]

    # Step 7: Perform fuzzy sanitization
    sanitized_transactions = sanitize_transactions(transactions_to_sanitize, reduction_factor)

    # Update fuzzy_data with sanitized transactions
    for index, fuzzy_entry in sanitized_transactions:
        fuzzy_data[index] = fuzzy_entry  # Update the fuzzy set for the transaction

    return fuzzy_data

# Sample dataset (your actual data)
data = [
    [25, 55000, 12], [35, 42000, 13], [48, 72000, 6],
    [22, 78000, 8], [34, 65000, 4], [45, 39000, 7],
    [26, 58000, 15], [32, 70000, 5], [50, 44000, 9],
    [28, 52000, 14], [31, 73000, 4], [47, 39000, 11],
    [23, 60000, 16], [30, 72000, 4], [49, 46000, 10],
    [24, 55000, 18], [36, 68000, 5], [44, 47000, 12],
    [27, 59000, 17], [33, 71000, 10], [42, 48000, 8],
    [25, 56000, 14], [38, 70000, 3], [46, 42000, 9],
    [29, 55000, 15], [37, 69000, 5], [45, 48000, 10],
    [21, 53000, 17], [39, 65000, 4], [49, 49000, 11],
    [29, 55000, 15]
]

# Define restrictive rules as fuzzy sets (Example)
restrictive_rules = [
    'Medium',  # For age
    'Low',     # For income
    'High'     # For purchases
]

# Parameters
sanitization_threshold = 0.2  # Example threshold
reduction_factor = 0.2  # Example reduction factor

# Execute the main function
sanitized_data = main(data, restrictive_rules, sanitization_threshold, reduction_factor)

# Display sanitized data
for i, entry in enumerate(sanitized_data):
    print(f"{entry}")
