num = int(input(":"))

#decimal to binary
binary = " "

while True:
    if num // 2 >= 1:
        binary = str(num%2)+ binary
        num = num // 2
    elif num // 2 <= 1:
        binary = str(num%2)+ binary
        break
print(binary)
