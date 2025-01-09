
SELECT Product, Stage, AVG(DeliveryTime) as AvgDeliveryTime
FROM ProductPipeline
GROUP BY Product, Stage;
