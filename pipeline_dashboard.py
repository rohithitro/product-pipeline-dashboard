
import pandas as pd
import matplotlib.pyplot as plt

# Simulated Data Extraction
def extract_data():
    data = {
        "Product": ["Product A", "Product B", "Product C"],
        "Stage": ["Warehouse", "Transit", "Store"],
        "Delivery Time (Days)": [3, 5, 2]
    }
    return pd.DataFrame(data)

# Transforming Data
def transform_data(df):
    df["Status"] = ["On Time", "Delayed", "On Time"]
    return df

# Visualizing Data
def visualize_data(df):
    df.plot(x="Product", y="Delivery Time (Days)", kind="bar", color="skyblue")
    plt.title("Product Delivery Times by Stage")
    plt.ylabel("Delivery Time (Days)")
    plt.show()

if __name__ == "__main__":
    data = extract_data()
    transformed_data = transform_data(data)
    visualize_data(transformed_data)
