def apply_discount(customers):
    eligible_customers = filter(lambda customer: 18 <= customer['age'] <= 40, customers)
    
    discounted_customers = map(
        lambda customer: {
            
            "name": customer["name"],  
        "age": customer["age"],
            "total_purchase": customer['total_purchase'] * (0.9 if customer['age'] <= 25 else 0.95)
        },
        eligible_customers
    )
    
    return list(discounted_customers)


customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

discounted_customers = apply_discount(customers)

print(discounted_customers)