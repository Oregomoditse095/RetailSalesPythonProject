# a) Product Names
product_names = []
for i in range(5):
    product_name = input(f"Enter the name of product {i + 1}: ")
    product_names.append(product_name)

# b) Sales Data Entry
sales_data = [[0 for _ in range(5)] for _ in range(4)]
for week in range(4):
    for product in range(5):
        sales_quantity = int(input(f"Enter the sales quantity for {product_names[product]} in week {week + 1}: "))
        sales_data[week][product] = sales_quantity

# c) Total Sales per Product
total_sales_per_product = [sum(sales_data[week][product] for week in range(4)) for product in range(5)]
for product, total_sales in enumerate(total_sales_per_product):
    print(f"Total sales of {product_names[product]}: {total_sales}")

# d) Total Sales per Week
total_sales_per_week = [sum(sales_data[week][product] for product in range(5)) for week in range(4)]
for week, total_sales in enumerate(total_sales_per_week):
    print(f"Total sales in week {week + 1}: {total_sales}")

# e) Best Selling Product
best_product_index = total_sales_per_product.index(max(total_sales_per_product))
print(f"Best selling product: {product_names[best_product_index]}, Quantity: {total_sales_per_product[best_product_index]}")

# f) Weekly Performance
average_sales_per_week = sum(total_sales_per_week) / len(total_sales_per_week)
print(f"Average sales per week: {average_sales_per_week}")

# g) Product Performance
average_sales_per_product = [sum(sales_data[week][product] for week in range(4)) / 4.0 for product in range(5)]
for product, average_sales in enumerate(average_sales_per_product):
    print(f"Average sales of {product_names[product]}: {average_sales}")

# h) Sales Growth Analysis
max_sales_increase_week = 0
max_sales_increase = 0
for week in range(1, 4):
    sales_increase = total_sales_per_week[week] - total_sales_per_week[week - 1]
    if sales_increase > max_sales_increase:
        max_sales_increase = sales_increase
        max_sales_increase_week = week
print(f"Week with highest sales increase: Week {max_sales_increase_week + 1}, Increase: {max_sales_increase}")

# i) Lowest Sales Product
lowest_product_index = total_sales_per_product.index(min(total_sales_per_product))
print(f"Lowest selling product: {product_names[lowest_product_index]}, Quantity: {total_sales_per_product[lowest_product_index]}")

# j) Sales Forecasting
sales_forecast = [0] * 5
for product in range(5):
    sales_forecast[product] = int(input(f"Enter the predicted sales quantity for {product_names[product]} in the next week: "))
print("Sales Forecast:")
for product, forecast in enumerate(sales_forecast):
    print(f"{product_names[product]}: {forecast}")

# k) Sales Report
print("\nSales Report:")
print(f"Total Sales: {sum(total_sales_per_week)}")
print(f"Best Selling Product: {product_names[best_product_index]}, Quantity: {total_sales_per_product[best_product_index]}")
print(f"Lowest Selling Product: {product_names[lowest_product_index]}, Quantity: {total_sales_per_product[lowest_product_index]}")
print(f"Average Sales per Week: {average_sales_per_week}")
for product, average_sales in enumerate(average_sales_per_product):
    print(f"Average Sales of {product_names[product]}: {average_sales}")
