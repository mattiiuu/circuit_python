userInput = input("What did you buy? ")
buyStr = "" + userInput
priceInput = input("What was the price? ")
priceInput = float(priceInput)
theTotal = 0 + priceInput
userInput2 = input("Do you have another item to enter? ")


while userInput2 != "No":
  userInput = input("What's the other item? ")
  priceInput = input("What's the price? ")
  priceInput = float(priceInput)
  userInput2 = input("Would you like to enter another item? If not, enter: No. ")
  buyStr = buyStr + "," + userInput
  theTotal = theTotal + priceInput
  

print("These are your items: ", buyStr)
print("This is the total cost:", theTotal)
  
