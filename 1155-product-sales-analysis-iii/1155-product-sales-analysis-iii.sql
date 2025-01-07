# Write your MySQL query statement below

# product id, year, quantity, and price 
# first year of every product sold


SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) in (
    SELECT product_id, MIN(year) 
    FROM Sales
    GROUP BY product_id
)