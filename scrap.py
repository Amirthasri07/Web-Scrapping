from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# Setup Selenium with Proxy
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--proxy-server=http://<proxy_ip>:<proxy_port>')  # Replace with actual proxy details

# Set up WebDriver
service = Service('C:/Users/amirt/Downloads/edgedriver_win64/msedgedriver.exe')  # Update with your ChromeDriver path
driver = webdriver.Edge(service=service, options=options)
# url = "https://www.noon.com/uae-en/yoga-barre-socks-non-slip-anti-skid-sticky-silicone-grips-cotton-for-pilates-gym-pure-ballet-dance-barefoot-workout-ankle-multiuse-black-grey-skin-color-3pcs/Z2F9046D53376D3F6A8B7Z/p/?o=z2f9046d53376d3f6a8b7z-1"
# URL to scrape
url = "https://www.noon.com/uae-en/sports-and-outdoors/exercise-and-fitness/yoga-16328/"
driver.get(url)
time.sleep(3)

# # Simulated product data
products = [
    {"Title": "Yoga Mat", "priceNow": "1689", "Brand": "Sparnood Fitness", "Sales": "970"},
    {"Title": "Dumbbells", "priceNow": "100", "Brand": "BrandB", "Sales": "1099"},
    {"Title": "SF-3200:4HP", "priceNow": "1625", "Brand": "Brand s", "Sales": "876"},
    {"Title": "Yoga pants", "priceNow": "8096", "Brand": "Brand B", "Sales": "998"},
    {"Title": "Handgrippers", "priceNow": "3429", "Brand": "Sparnood Fitness", "Sales": "1498"},
]

#Convert to DataFrame and save to CSV
df = pd.DataFrame(products)
df.to_csv("noon_products.csv", index=False)
print("Data saved successfully!")




if products:
    df = pd.DataFrame(products)
    df.to_csv("noon_products.csv", index=False)
    print(f"Saved {len(products)} products to CSV.")
else:
    print("No products scraped. CSV file not saved.")
print(products)  # Check the content of the products list

#xtract product details
# products = []
while len(products) < 200:
    items = driver.find_elements(By.CLASS_NAME, "productContainer")
    for item in items:
        try:
            title = item.find_element(By.CLASS_NAME, "data-qa").text
            priceNow = item.find_element(By.CLASS_NAME, "priceNow").text
            brand = item.find_element(By.CLASS_NAME, "brandname").text
            seller = item.find_element(By.CLASS_NAME, "seller").text
            products.append({
                "Title": title,
                "priceNow": priceNow,
                "Brand": brand,
                "Seller": seller
            })
        except Exception as e:
            print("Error extracting item: {e}")

    # Click on "Next Page" if available
    try:
        next_button = driver.find_element(By.CLASS_NAME, "nextButton")
        next_button.click()
        time.sleep(2)
    except Exception:
        print("No more pages")
        break

driver.quit()

if not products:
    print("No products were scraped.")
else:
    print(f"Saving {len(products)} products to CSV.")

# Convert the list of products to a DataFrame
new_data = pd.DataFrame(products)

try:
    # Read existing data if the file exists
    existing_data = pd.read_csv("noon_products.csv")
    new_data = pd.DataFrame(products)
    combined_data = pd.concat([existing_data, new_data]).drop_duplicates(ignore_index=True)
except FileNotFoundError:
    combined_data = new_data

# Save the combined data to CSV
if not combined_data.empty:
    combined_data.to_csv("noon_products.csv", index=False)
    print("Data saved to 'noon_products.csv'")
else:
    print("No data to save to CSV.")
    
    
# Save data to the CSV file
combined_data.to_csv("noon_products.csv", index=False)
print("Data saved to 'noon_products.csv'")

# Save data to CSV
df = pd.DataFrame(products)
df.to_csv("noon_products.csv", index=False)
print("Data saved to 'noon_products.csv'")
print(new_data.head())


