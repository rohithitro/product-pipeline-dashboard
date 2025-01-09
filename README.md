
# Product Pipeline Visibility Dashboard

This project tracks product lifecycles from warehouses to stores using Python, SQL, and Power BI. The goal is to improve delivery time visibility, identify bottlenecks, and provide actionable insights with clear visualizations.

## Features
- Extract, transform, and visualize product delivery data with Python.
- Aggregate and analyze lifecycle data with SQL.
- Highlight late products with visual annotations.
- Build a dashboard to monitor KPIs such as delivery times, shipping costs, customer satisfaction, and profit margins.

## How to Run
1. Clone this repository and navigate to the directory.
2. Install required Python libraries:
   ```bash
   pip install pandas matplotlib seaborn
   ```
3. Run the Python script:
   ```bash
   python updated_pipeline_dashboard_with_chart.py
   ```

## Outputs
- The script generates a chart highlighting key KPIs and flags late products. The chart is saved as `product_kpi_chart.png`.

## Visualization
Below is an example of the generated chart, showcasing delivery times, shipping costs, customer satisfaction, and profit margins for different products.

![Product KPI Chart](product_kpi_chart.png)

## SQL Query
Use the `pipeline_aggregation.sql` script to analyze aggregated product data:
```sql
SELECT Product, Stage, AVG(DeliveryTime) as AvgDeliveryTime
FROM ProductPipeline
GROUP BY Product, Stage;
```

## Customization
- You can modify the thresholds for "late products" in the script.
- Update the KPI values in the `extract_data` function to test various scenarios.
