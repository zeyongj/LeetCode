# Write your MySQL query statement below
WITH FirstQuarterSales AS (
    SELECT DISTINCT product_id
    FROM Sales
    WHERE sale_date BETWEEN '2019-01-01' AND '2019-03-31'
),
OtherSales AS (
    SELECT DISTINCT product_id
    FROM Sales
    WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31'
)
SELECT p.product_id, p.product_name
FROM Product p
JOIN FirstQuarterSales fqs ON p.product_id = fqs.product_id
LEFT JOIN OtherSales os ON p.product_id = os.product_id
WHERE os.product_id IS NULL

