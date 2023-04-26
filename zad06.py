#prikazati IP adresu 192.168.0.184 u binarnom, oktalnom i heksadekadskom prikazu
oktet1 = 192
oktet2 = 168
oktet3 = 0
oktet4 = 184


print(f"Binarni prikaz: \n\t{bin(oktet1)}.{bin(oktet2)}.{bin(oktet3)}.{bin(oktet4)}")
print(f"Oktalni prikaz: \n\t{oct(oktet1)}.{oct(oktet2)}.{oct(oktet3)}.{oct(oktet4)}")
print(f"Heksadekadski prikaz: \n\t{hex(oktet1)}.{hex(oktet2)}.{hex(oktet3)}.{hex(oktet4)}")
print(f"Dekadski prikaz: \n\t{(oktet1)}.{(oktet2)}.{(oktet3)}.{(oktet4)}")