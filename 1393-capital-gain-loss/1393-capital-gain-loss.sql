# Write your MySQL query statement below
SELECT 
    s.stock_name,
    SUM(
        CASE 
            WHEN s.operation = 'buy' THEN -price
            WHEN s.operation = 'sell' THEN price
        END
    ) AS capital_gain_loss
FROM Stocks s
GROUP BY s.stock_name