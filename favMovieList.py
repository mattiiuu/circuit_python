userInput = input("What are your favorite movies? ")
movieStr = "" + userInput
userInput2 = input("Would you like to enter another movie? If not, enter No. ")

while userInput2 != "No":
  userInput = input("What's your other favorite movies? ")
  userInput2 = input("Would you like to enter another movie? If not, enter: No. ")
  movieStr = movieStr + ", " + userInput

print("These are your favorite movies:", movieStr)
