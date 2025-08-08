def main():
    try:
        # Prompt user for input
        price = float(input("Enter the original price of the item: $"))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate the final price using the function
        final_price = calculate_discount(price, discount_percent)
        
        # Display results
        if discount_percent >= 20:
            savings = price - final_price
            print(f"\nDiscount applied: {discount_percent}%")
            print(f"Original price: ${price:.2f}")
            print(f"You saved: ${savings:.2f}")
            print(f"Final price: ${final_price:.2f}")
        else:
            print(f"\nDiscount of {discount_percent}% is less than 20%, so no discount applied.")
            print(f"Final price: ${final_price:.2f}")
    
    except ValueError:
        print("Please enter valid numbers for price and discount percentage.")
