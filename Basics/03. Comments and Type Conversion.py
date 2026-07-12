# Comments in Python = Comments are written for humans, not for Python. Python completely ignores comments while running the code.
# In Python, comments start with the '#' symbol.

# What is Type Conversion? =    Type conversion means changing one data type into another.


    # Q) Take a product price as a float and print the price after adding 18% GST.

product_price = float(input("Enter Product Price = "))
GST = product_price * 0.18

Final_Price = product_price + GST

print("Final Price of the Product is ", Final_Price)

print(type(product_price))
print(type(GST))

    # Q) Convert "123" into an integer and multiply it by 10.

num = "123"
print(num, " Data type is ", type(num))

num1 = int(num)
print(f"Now {num1} Data type is {type(num1)}")
print(num1 * 10)