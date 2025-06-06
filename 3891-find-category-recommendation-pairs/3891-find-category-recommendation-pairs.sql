-- Write your PostgreSQL query statement below
WITH format_product AS (
	SELECT user_id, category
	FROM ProductPurchases p
	INNER JOIN ProductInfo p1 ON p.product_id = p1.product_id
), main_proccess AS (
	SELECT P.category AS category1, P1.category AS category2, COUNT( DISTINCT P.user_id ) customer_count 
	FROM format_product P INNER JOIN format_product P1 ON P.category < P1.category AND P.user_id = P1.user_id
	GROUP BY P.category, P1.category
	HAVING(COUNT(DISTINCT P.user_id)) > 2
)
SELECT category1, category2,
customer_count
FROM main_proccess M
ORDER BY customer_count DESC, category1, category2