# Define the coupon codes and rates for each day in week
coupon_codes = {
    "monday": 0.1,   # 10% discount
    "tuesday": 0.2,  # 20% discount
    "wednesday": 0.15,  # 15% discount
    "thursday": 0.25,  # 25% discount
    "friday": 0.3,   # 30% discount
    "saturday": 0.1,   # 10% discount
    "sunday": 0.5,   # 50% discount
}

# Get the current day
current_day = str.lower(input("Enter the day of the week for the current discount : \n"))
# Check if the current day is in the coupon codes dictionary
if current_day in coupon_codes:
    discount_rate = coupon_codes[current_day]
    coupon_code = f"DISCOUNT{int(discount_rate * 100)}"
    print(f"Today's discount rate is {discount_rate * 100}%")
    print(f"Use coupon code: {coupon_code}")
else:
    print("No discount available for today.")