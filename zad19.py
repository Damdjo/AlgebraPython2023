numbers = []
for number in range(1,31):
    numbers.append(number)
print(numbers)

factorOf3 = 0
factorOf6 = 0
factorOf9 = 0

for number in numbers:
    
    if number % 9 == 0 and number % 6 == 0:
        factorOf6 +=1
        factorOf9 += 1
        print(f"{number} je djeljiv sa 9, 6 i sa 3")
    
    elif number % 9 == 0:
        factorOf9 += 1
        factorOf3 += 1
        print(f"{number} je djeljiv sa 9 i sa 3")
    
    elif number % 6 == 0:
        factorOf6 += 1
        factorOf3 += 1
        print(f"{number} je djeljiv sa 6 i sa 3")
    
    elif number % 3 == 0:
        factorOf3 += 1
        print(f"{number} je djeljiv sa 3")
    
    else:
        print(F"{number} nije djeljiv sa brojevima 3, 6 ili 9")
        
print(f"Djeljivi sa 3: {factorOf3}, sa 6: {factorOf6}, sa 9: {factorOf9}") 