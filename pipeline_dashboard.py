
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Simulated Data Extraction
def extract_data():
    data = {
        "Product": ["Product A", "Product B", "Product C"],
        "Stage": ["Warehouse", "Transit", "Store"],
        "Delivery Time (Days)": [3, 5, 2],
        "Shipping Cost ($)": [15, 25, 10],
        "Customer Satisfaction (1-10)": [8, 6, 9],
        "Profit Margin (%)": [25, 15, 30]
    }
    return pd.DataFrame(data)

# Adding a flag for late products
def add_late_product_flag(df):
    df["Late Product"] = df["Delivery Time (Days)"] > 4
    return df

# Visualizing KPIs with late product highlights
def visualize_with_late_products(df):
    # Set the style for modern visuals
    sns.set_theme(style="whitegrid")

    # Create the figure and axes
    fig, ax1 = plt.subplots(figsize=(12, 7))

    # Bar chart for Delivery Time
    sns.barplot(x="Product", y="Delivery Time (Days)", data=df, ax=ax1, color="skyblue", label="Delivery Time (Days)")
    ax1.set_xlabel("Product")
    ax1.set_ylabel("Delivery Time (Days)", color="blue")
    ax1.tick_params(axis="y", labelcolor="blue")
    ax1.set_title("Product KPIs with Late Product Highlights", fontsize=14)

    # Line chart for Shipping Costs
    ax2 = ax1.twinx()
    sns.lineplot(x="Product", y="Shipping Cost ($)", data=df, ax=ax2, color="green", marker="o", label="Shipping Cost ($)")
    ax2.set_ylabel("Shipping Cost ($)", color="green")
    ax2.tick_params(axis="y", labelcolor="green")

    # Line chart for Customer Satisfaction
    ax3 = ax1.twinx()
    ax3.spines["right"].set_position(("outward", 60))  # Positioning third y-axis
    sns.lineplot(x="Product", y="Customer Satisfaction (1-10)", data=df, ax=ax3, color="red", marker="s", linestyle="--", label="Customer Satisfaction")
    ax3.set_ylabel("Customer Satisfaction (1-10)", color="red")
    ax3.tick_params(axis="y", labelcolor="red")

    # Line chart for Profit Margin
    ax4 = ax1.twinx()
    ax4.spines["right"].set_position(("outward", 120))  # Positioning fourth y-axis
    sns.lineplot(x="Product", y="Profit Margin (%)", data=df, ax=ax4, color="orange", marker="d", linestyle="-.", label="Profit Margin (%)")
    ax4.set_ylabel("Profit Margin (%)", color="orange")
    ax4.tick_params(axis="y", labelcolor="orange")

    # Highlight late products with an annotation
    for i, row in df.iterrows():
        if row["Late Product"]:
            ax1.text(i, row["Delivery Time (Days)"] + 0.2, "Late", color="red", ha="center", fontsize=10, fontweight="bold")

    # Save the chart as an image
    plt.savefig("product_kpi_chart.png")
    plt.show()

if __name__ == "__main__":
    data = extract_data()
    data_with_flags = add_late_product_flag(data)
    visualize_with_late_products(data_with_flags)
