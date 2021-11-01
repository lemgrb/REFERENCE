def divisible_by_3_or_2(num):
    if(num%2==0 and num%3==0):
        return "Divisible by both 2 and 3"
    elif(num%2==0):
        return "Divisible by 2"
    elif (num%3==0):
        return "Divisible by 3"
    else:
        return "Not divisible by 2 or 3"

print("6 is " + divisible_by_3_or_2(6))
print("12 is " + divisible_by_3_or_2(12))
print("1 is " + divisible_by_3_or_2(1))
print("3 is " + divisible_by_3_or_2(3))
print("2 is " + divisible_by_3_or_2(2))
