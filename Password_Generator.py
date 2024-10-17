import random


randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
randomNumber = chr(random.randint(48, 57))
randomSymbol = chr(random.randint(33, 47))

randomPassword = (randomLowerLetter + randomLowerLetter + randomUpperLetter + randomUpperLetter + randomNumber + randomNumber + randomSymbol + randomSymbol)

randomPassword_list = list(randomPassword)
random.shuffle(randomPassword_list)
shuffledPassword = ''.join(randomPassword_list)

print(shuffledPassword)