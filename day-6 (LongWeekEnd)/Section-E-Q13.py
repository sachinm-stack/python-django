# Q13.List — Shopping Cart:

# Save as: section_e.py

cart = ["milk", "bread", "eggs"]


# 1. Add 'butter' to the end

cart.append("butter")
print(cart)

# 2. Add 'juice' at position 1 (index 1)
cart.insert(1,"butter")
print(cart)

# 3. Remove "bread" by value
cart.remove("bread")
print(cart)

# 4. Print how many items are in the cart
print(len(cart))

# 5. Sort the cart alphabetically and print
cart.sort()
print(cart)
# 6. Print the LAST item without using index -1 (use len())

print(cart[len(cart) - 1])
 
# 7. Check if "eggs" is in cart → print True/False
print( "eggs" in cart)

# 8. Pop the last item and print what was removed
removed_item = cart.pop()
print(removed_item)


# 9. Print the final cart

print(cart)
