print("Happy no's")

def ishappy(n):
    if n == 1:
        return True
    if n == 4:
        return False
    sum = 0
    while n > 0:
        rem = n % 10
        sum += rem**2
        n = n //10
    return ishappy(sum)
print(ishappy(9))

