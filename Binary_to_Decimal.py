num = input("enter number:")

count = len(num)
result = 0

for i in range (0,count):
    ans = int(num[-1]) * 2**i
    num = num[0:(count-(i+1))]
    result = result + ans

print(result)

    
