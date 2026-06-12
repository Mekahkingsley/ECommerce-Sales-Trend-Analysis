-- Project: Year-over-Year Sales & Seasonal Trend Analysis

-- Query 1: Monthly Total Revenue Breakdown to compare 2010 vs 2011 (YoY)
SELECT 
    EXTRACT(YEAR FROM InvoiceDate) AS sales_year,
    EXTRACT(MONTH FROM InvoiceDate) AS sales_month,
    ROUND(SUM(Quantity * UnitPrice)::numeric, 2) AS monthly_revenue,
    COUNT(DISTINCT InvoiceNo) AS total_orders
FROM 
    cleaned_retail_data
GROUP BY 
    sales_year, sales_month
ORDER BY 
    sales_month, sales_year;


-- Query 2: Peak Shopping Hours Analysis for Operational Optimization
SELECT 
    EXTRACT(HOUR FROM InvoiceDate) AS purchase_hour,
    COUNT(DISTINCT InvoiceNo) AS unique_orders_placed,
    ROUND(SUM(Quantity * UnitPrice)::numeric, 2) AS hourly_revenue
FROM 
    cleaned_retail_data
GROUP BY 
    purchase_hour
ORDER BY 
    unique_orders_placed DESC;
