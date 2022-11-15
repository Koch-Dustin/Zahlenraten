import random
    
def game():
  numberToGuess = random.randint(1, 100) 
  trysTakeToGuess = 0

  print("Ich denke an eine Zahl zwischen 1 - 20. Kannst du sie erraten?")

  userGuessedNumber = -1
  
  while True:
    userGuessedNumber = input("Was denkst du: ")
  
    if(userGuessedNumber.isdigit()):
      trysTakeToGuess = trysTakeToGuess + 1
      
      isOutOfRangeFrom50 = int(userGuessedNumber) < numberToGuess - 50 or int(userGuessedNumber) > numberToGuess + 50
      isOutOfRangeFrom25 = int(userGuessedNumber) < numberToGuess - 25 or int(userGuessedNumber) > numberToGuess + 25
      isOutOfRangeFrom10 = int(userGuessedNumber) < numberToGuess - 10 or int(userGuessedNumber) > numberToGuess + 10
      isOutOfRangeFrom5 = int(userGuessedNumber) < numberToGuess - 5 or int(userGuessedNumber) > numberToGuess + 5
      isOutOfRangeFrom2 = int(userGuessedNumber) < numberToGuess - 2 or int(userGuessedNumber) > numberToGuess + 2
      
      if(isOutOfRangeFrom50):
        print("Sehr Kalt")
      
      elif(isOutOfRangeFrom25): 
        print("Kalt")
        
      elif(isOutOfRangeFrom10):
        print("Lauwarm")
        
      elif(isOutOfRangeFrom5):
        print("Warm")
        
      elif(isOutOfRangeFrom2):
        print("Sehr Warm")
      else:
        print("Klasse! Du hast meine Zahl erraten!")
        print("Gebrauchte Versuche: " + str(trysTakeToGuess))
        playAgain = input("Willst du nochmal spielen? [Y / N] : ")
        if(playAgain == "Y"):
          game()
        break
    
    else:
      print("Es heißt nicht umsonst ZAHLENraten! Versuch es nochmal!")

game()