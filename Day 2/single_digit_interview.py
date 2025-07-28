num = int(input("enter number"))

digit_sum = sum(int(digit) for digit in str(num))
print("the sum is ",digit_sum)

if digit_sum >= 10:
    print("double digit")
else:
    print("single digit")
