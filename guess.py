import main
import random
print("Guessing Game")

print("Enter a bottom line for the range you want to guess in (inclusive)")
bottom_limit = int(input())  
print("Enter an upper limit for the range you want to guess in (inclusive)")
upper_limit = int(input())

while main.while_loop == 1:
  
  print("Guess a number in the range you gave.")
  
  answer = random.randint(bottom_limit, upper_limit)

  
  guess = int(input())
  
  if guess == answer:
    print("Congrats! you got it right, The answer was:")
    print(answer)
  else:
    print("Whoopsies! You were wrong, The answer was:")
    print(answer)
    print("Try Again!")