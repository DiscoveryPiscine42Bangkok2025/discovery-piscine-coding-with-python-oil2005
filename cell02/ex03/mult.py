A = int(input("Enter the first number: "))
print(f"{A}")
B = int(input("Enter the second number: "))
print(f"{B}")
C = A*B
print(f"{A} x {B} = {C}")
if C > 0 :
    print("The result is positive.")
if C < 0 :
    print("The result is negative.")
if C == 0 :
    print("The result is positive and negative.")