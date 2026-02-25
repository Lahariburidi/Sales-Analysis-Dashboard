-- 1. EXECUTIVE OVERVIEW METRICS

SELECT 
    SUM(Revenue) AS Total_Revenue,
    SUM(Profit) AS Total_Profit,
    ROUND((SUM(Profit) / SUM(Revenue)) * 100, 2) AS Overall_Profit_Margin_Pct,
    COUNT(Order_ID) AS Total_Orders
FROM sales_data;

-- 2. REVENUE BY REGION
-- (Matches the 'Revenue by Region' chart in Power BI and your Python map)
SELECT 
    Region, 
    SUM(Revenue) AS Total_Revenue
FROM sales_data
GROUP BY Region
ORDER BY Total_Revenue DESC;

-- 3. TOP 5 PRODUCTS BY PROFIT
-- (Matches your Power BI 'Profit' tab and deep-dive logic)
SELECT 
    Product_Category, 
    SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Product_Category
ORDER BY Total_Profit DESC
LIMIT 5;

-- 4. MONTHLY REVENUE TRENDS
-- (Matches the 'Monthly Revenue Trend' line charts)
SELECT 
    strftime('%m', Order_Date) AS Month_Number, 
    SUM(Revenue) AS Monthly_Revenue
FROM sales_data
GROUP BY Month_Number
ORDER BY Month_Number;

-- 5. CUSTOMER SEGMENTATION ANALYSIS
-- (Matches the 'Revenue by Customer Segment' donut chart)
SELECT 
    Customer_Segment, 
    SUM(Revenue) AS Segment_Revenue,
    COUNT(Order_ID) AS Order_Count
FROM sales_data
GROUP BY Customer_Segment
ORDER BY Segment_Revenue DESC;

-- 6. TOP 10 HIGH-VALUE CUSTOMERS
-- (Matches your 'Sales Deep Dive' table)
SELECT 
    Customer_ID, 
    SUM(Revenue) AS Total_Spend
FROM sales_data
GROUP BY Customer_ID
ORDER BY Total_Spend DESC
LIMIT 10;