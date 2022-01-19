import string
import random
import ctypes
import time

## Change the name of the console title

import ctypes
Title = "Password Generator - $:git$"
ctypes.windll.kernel32.SetConsoleTitleW(Title)

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def password():

	length = int(input("Enter password length: "))

	random.shuffle(characters)
	
	password = []
	for i in range(length):
		password.append(random.choice(characters))

	random.shuffle(password)

	## converting the list to string
	## printing the list
	print(' ')
	print("".join(password))



## invoking the function
password()

print(' ')
bar = [
" [H]                ",
" [He]               ",
" [Hec]              ",
" [Hech]             ",
" [Hecho]            ",
" [Hecho p]          ",
" [Hecho po]         ",
" [Hecho por]        ",
" [Hecho por $]      ",
" [Hecho por $:]     ",
" [Hecho por $:g]    ",
" [Hecho por $:gi]   ",
" [Hecho por $:git]  ",
" [Hecho por $:git$] ",
]
i = 0

while True:
    print(bar[i % len(bar)], end="\r")
    time.sleep(.2)
    i += 1