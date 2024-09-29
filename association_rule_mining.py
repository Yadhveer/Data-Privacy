import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Sample dataset (replace with your actual data)
data = [['Low Age', 'Medium Income', 'High Purchases'],
 ['Medium Age', 'Low Income', 'High Purchases'],
 ['High Age', 'High Income', 'Medium Purchases'],
 ['Low Age', 'High Income', 'Medium Purchases'],
 ['Medium Age', 'Medium Income', 'Low Purchases'],
 ['High Age', 'Low Income', 'Medium Purchases'],
 ['Low Age', 'Medium Income', 'High Purchases'],
 ['Medium Age', 'High Income', 'Low Purchases'],
 ['High Age', 'Low Income', 'Medium Purchases'],
 ['Low Age', 'Medium Income', 'High Purchases'],
 ['Medium Age', 'High Income', 'Low Purchases'],
 ['High Age', 'Low Income', 'Medium Purchases'],
 ['Low Age', 'Medium Income', 'High Purchases'],
 ['Medium Age', 'High Income', 'Low Purchases'],
 ['High Age', 'Low Income', 'Medium Purchases'],
 ['Low Age', 'Medium Income', 'High Purchases'],
 ['Medium Age', 'Medium Income', 'Medium Purchases'],
 ['High Age', 'Low Income', 'High Purchases'],
 ['Low Age', 'Medium Income', 'High Purchases'],
 ['Medium Age', 'High Income', 'High Purchases'],
 ['High Age', 'Low Income', 'Medium Purchases'],
 ['Low Age', 'Medium Income', 'High Purchases'],
 ['Medium Age', 'High Income', 'Low Purchases'],
 ['High Age', 'Low Income', 'Medium Purchases'],
 ['Low Age', 'Medium Income', 'High Purchases'],
 ['Medium Age', 'Medium Income', 'Medium Purchases'],
 ['High Age', 'Low Income', 'High Purchases'],
 ['Low Age', 'Medium Income', 'High Purchases'],
 ['Medium Age', 'Medium Income', 'Low Purchases'],
 ['High Age', 'Low Income', 'High Purchases'],
 ['Low Age', 'Medium Income', 'High Purchases']]

# Create a transaction encoder object
te = TransactionEncoder()
te_data = te.fit(data).transform(data)

# Convert the result to a pandas DataFrame
df = pd.DataFrame(te_data, columns=te.columns_)

# Apply Apriori algorithm with minimum support and confidence
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)  # Adjust min_support as needed
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)  # Adjust min_threshold as needed

# Print the mined rules
print(rules)
