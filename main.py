#This game is similar to the original card game called War, but there are few changes. First of all, the programm asks a person how many cards the player wants to play with. Second, it is also a mathematical game in which each player has to take 2 cards and add them up to see if their final number is larger than other player's number. The player gets a point if he calculate numbers correctly and if not the person gets -1 point. Also, if person's number in general is larger than the second person, the first player will also get a point. (MAYBE YOU WILL CONSIDER THIS AS A SMALL EXTRA CREDIT OR MAYBE NOT)
import random
game = True

while game:
  player1 = input("Enter player 1 name: ")
  player2 = input("Enter player 2 name: ")
  number = int(input("How many cards in a deck do you want to have(In each deck there are 52 cards, so type in a number like 1 or 2 or 3: "))

  score_of_p1 = 0
  score_of_p2 = 0

  def shuffledDeck():
    global number
    number = number*52
    standardDeck = list(range(number))
    random.shuffle(standardDeck)
    return standardDeck
    

  def playerTurn(playerName):
    for i in range(1):
      card = deck.pop()
      card2 = deck.pop()
    print(playerName, "drew cards:",card, card2)
    final = card + card2
    return final

  deck = shuffledDeck()
  current_cards = 0

  while len(deck) > 0:
    cardp1 = playerTurn(player1)
    outcomep1 = input("What is the sum of those numbers?: ")
    cardp2 = playerTurn(player2)
    outcomep2 = input("What is the sum of those numbers?: ")

    if cardp1 == int(outcomep1):
      print(player1, ", you are good with adding numbers!")
      print()
      score_of_p1 += current_cards
      score_of_p1 += 1
    if cardp2 == int(outcomep2):
      print(player2, ", you are good with adding numbers!")
      print()
      score_of_p2 += current_cards
      score_of_p2 += 1
    if cardp2 != int(outcomep2):
      print(player2, ", you are wrong!")
      print()
      score_of_p2 += current_cards
      score_of_p2 -= 1
    if cardp1 != int(outcomep1):
      print(player1, ", you are wrong!")
      print()
      score_of_p1 += current_cards
      score_of_p1 -= 1
    
    if cardp1 > cardp2:
      score_of_p1 += current_cards
      score_of_p1 += 1
      print(player1 + ", gets a point because his number was higher than the other's player number!")
      print()

    elif cardp2 > cardp1:
      score_of_p2 += current_cards
      score_of_p2 += 1
      print(player2 + ", gets a point because his number was higher than the other's player number!")
      print()

    elif cardp1 == cardp2:
     winner = True
     print("War!")
     
     while winner:
       cardp1 = (deck.pop())
       cardp2 = (deck.pop())
       print(player1,":", cardp1)
       print(player2,":", cardp2)
       if cardp1 > cardp2:
        score_of_p1 += current_cards
        print(player1 + ", is the winner in this round because second card the ", player1, "drew had larger value than ", player2, "!")
        print()
        score_of_p1 += 1
        print(score_of_p1)
        winner = False

       elif cardp2 > cardp1:
        score_of_p2 += current_cards
        print(player2 + ", is the winner in this round because second card ", player2, "drew had larger value than ", player1, "!")
        print()
        score_of_p2 += 1
        print(score_of_p2)
        winner = False

       elif cardp1 == cardp2:
         winner = True 

  if score_of_p1 > score_of_p2:
    print("Game results: ", score_of_p1, "and ", score_of_p2)
    print(player1, "won this game! Congrats")
  elif score_of_p1 < score_of_p2:
    print("Game results: ", score_of_p1, "and ", score_of_p2)
    print(player2, "won this game, congrats!")
  else:
    print("Game results: ", score_of_p1, "and ", score_of_p2)
    print(player1, ", and ", player2, "have a tie game!")

  again = input("Do you want to play again? y/n  ")
  if again == "y":
    game = True
  elif again == "n":
    print("Thanks for playing!")
    game = False
