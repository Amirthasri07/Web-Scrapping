import pandas as pd

# Load the CSV file
data = pd.read_csv("noon_products.csv")

# Ensure `priceNow` column contains strings and handle missing values
if 'priceNow' in data.columns:
    data['priceNow'] = data['priceNow'].fillna('').astype(str)
    
    # Remove 'AED', commas, and convert to float
    data['priceNow'] = (
        data['priceNow']
        .str.replace('AED', '', regex=False)
        .str.replace(',', '', regex=False)
    )
    
    # Convert the cleaned strings to float
    try:
        data['priceNow'] = data['priceNow'].astype(float)
    except ValueError:
        print("Some rows in 'priceNow' could not be converted to float. Check the data.")
else:
    print("The 'priceNow' column does not exist in the dataset.")

# Display the cleaned data
print(data.head())

# Save cleaned data back to CSV
data.to_csv("cleaned_noon_products.csv", index=False)

most_expensive = data.loc[data['priceNow'].idxmax()]
print("Most Expensive Product:")
print(most_expensive)

# Cheapest product
cheapest = data.loc[data['priceNow'].idxmin()]
print("Cheapest Product:")
print(cheapest)

# Count products by brand
brand_counts = data['Brand'].value_counts()
print("Number of Products from Each Brand:")
print(brand_counts)








