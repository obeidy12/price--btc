import requests
import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.title("Digital Currency Prices from Al-obeidy ")
root.geometry("300x200")


# Define function to get prices from API
def get_prices():
    # Send request to API
    response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD,LTC-USD")

    # Parse JSON response
    prices = response.json()["data"]
    bitcoin_price = prices[0]["amount"]
    litecoin_price = prices[1]["amount"]

    # Update labels with prices
    bitcoin_label.config(text=f"Bitcoin: ${bitcoin_price}")
    litecoin_label.config(text=f"Litecoin: ${litecoin_price}")

    # Schedule function to run again in 60 seconds
    root.after(60000, get_prices)


# Create labels to display prices
bitcoin_label = tk.Label(root, font=("Arial", 20))
litecoin_label = tk.Label(root, font=("Arial", 20))

# Position labels in window
bitcoin_label.pack(pady=10)
litecoin_label.pack(pady=10)

# Call function to get prices and update labels
get_prices()

# Run Tkinter main loop
root.mainloop()
