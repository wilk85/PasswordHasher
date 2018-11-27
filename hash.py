# hasowanie przy pomocy passwordmeter
import random, string, os
import hashlib

print()
print('Program dokleji odpowiednią ilość znaków')
userInput = int(input('Podaj jaką bazową długość ma posiadać hasło : '))

# print(userInput)
def generate(number):
    stringList = string.punctuation + string.digits + string.ascii_letters
    
    passWord = ''.join(random.sample(stringList,number))

    print()
    print('Twoje losowe hasło to : ' + passWord)
    print()

    salt = ''.join(random.sample(stringList,5))
    salt2 = os.urandom(5).hex()

    # sklejanie hasła w jedną całość
    newPass = str(salt) +  passWord + str(salt2) #+ str(salt) + str(two)

    
    print('Twoje hasło ma teraz długość : ' + str(len(newPass)) , end=' ')
    print()
    print('W tym momencie tak wygląda twoje hasło : ', newPass)
    print()
    

generate(userInput)
