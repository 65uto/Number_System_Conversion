num = input("enter number:")
character = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
count = len(num)
result = 0

for i in range (0,count):
    if num[-1] in character:
        ans = int(character[num[-1]]) * 16**i
        num = num[0:(count-(i+1))]
        result = result + ans
    else:
        ans = int(num[-1]) * 16**i
        num = num[0:(count-(i+1))]
        result = result + ans

print(result)

    
