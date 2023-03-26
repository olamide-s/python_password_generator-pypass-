#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#print greetings and ask for input
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#it generate random letter symbols and numbers it generate the exact amount the user want from each of them

# password list to save the random password generated
password = []

# loop through from 0 to any number the user put and generate only letters and save it to password list
for letter in range(0, nr_letters):
  random_letter = random.choice(letters)
  password += random_letter

# loop through from 0 to any number the user put and generate only symbols and save it to password list
for symbol in range(0, nr_symbols):
  random_symbols = random.choice(symbols)
  password += random_symbols

# loop through from 0 to any number the user put and generate only number and save it to password list
for number in range(0, nr_numbers):
  random_numbers = random.choice(numbers)
  password += random_numbers

#create a new variable
password2 = ""

##convert the list into normal string and saving it into the password2 variable by looping through all the
#password in the  list and addind them 1 by one 
for number in password:
  password2 += number
print(f"this is not a randomize password: {password2}")


#Hard Level - Order of characters randomised:

#it shuffle all the characters in the list 
random.shuffle(password)

#create a new variable 
password3 = ""

##convert the list into normal string and saving it into the password3 variable by looping through all the
#password in the  list and addind them 1 by one 
for number in password:
  password3 += number
print(f"this is a randomize password: {password3}")

#below is a simpler way to do it but my instructured wanted more than this 
print(''.join(random.sample(password, len(password))))
