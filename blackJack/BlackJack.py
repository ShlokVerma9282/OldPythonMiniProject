import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10]
game = input("Do you want to play blackjack y or n:\n")
def check_for_ace(sum,first_card_player,second_card_player):
    if sum > 21 and first_card_player==11:
        sum += -11
    elif sum > 21 and second_card_player==11:
        sum += -11
def cont():
 loop = True
 while loop:
    if game=="y":
        player_card=["Your cards are:"]
        dud_card=0
        first_card_player=random.choice(cards)
        player_card.append(first_card_player)
        cards.remove(first_card_player)
        second_card_player=random.choice(cards)
        player_card.append(second_card_player)
        cards.remove(second_card_player)
        sum_of_player=first_card_player+second_card_player
        print(  *player_card)
        check_for_ace(sum_of_player, first_card_player,second_card_player)
        print(f"The sum is: {sum_of_player}")
        computer_card=["Computer first card is"]
        first_card_computer = random.choice(cards)
        computer_card.append(first_card_computer)
        cards.remove(first_card_computer)
        print(*computer_card)
        second_card_computer = random.choice(cards)
        computer_card.append(second_card_computer)
        cards.remove(second_card_computer)
        sum_of_computer = first_card_computer + second_card_computer
        check_for_ace(sum_of_computer,first_card_computer,second_card_computer)
        new=True
        while new:
            ask_for_new_card=input("Do you want a new card: y or n\n")
            if ask_for_new_card=="y" and sum_of_player<21:
                new_card = random.choice(cards)
                player_card.append(new_card)
                cards.remove(new_card)
                sum_of_player+=new_card
                if sum_of_player<=21:
                    print(*player_card, sep=",")
                    check_for_ace(sum_of_player, first_card_player, second_card_player)
                    check_for_ace(sum_of_player, new_card, dud_card)
                    print(f"The sum is: {sum_of_player}")
                elif sum_of_player>21:
                    print("It's a bust.Computer Win!!!")
                    new=False
                    loop=False
                    new_game=input("Do you want to continue: y or n\n")
                    if new_game=="y":
                        cont()
            elif ask_for_new_card=="n":
                not_enough=True
                while not_enough:
                  if sum_of_computer<17:
                    new_card_computer = random.choice(cards)
                    cards.append(computer_card)
                    cards.remove(new_card_computer)
                    sum_of_computer+=new_card_computer
                    check_for_ace(sum_of_computer, first_card_computer, second_card_computer)
                    check_for_ace(sum_of_computer,new_card_computer,dud_card)
                    if sum_of_computer<17:
                        print("Compuer sum is less than 17")
                        print("Computer is picking a new card")
                    elif sum_of_computer>=17 and sum_of_computer<=21:
                         not_enough=False
                    elif sum_of_computer>21:
                         new=False
                         loop=False
                         not_enough=False
                         print("It's a bust.Player Win!!!")
                         new_game = input("Do you want to continue: y or n\n")
                         if new_game == "y":
                          cont()
            if sum_of_computer<=21 and sum_of_player<=21:
                if sum_of_computer>sum_of_player:
                   print("Computer Win!!!")
                   new=False
                   loop=False
                   not_enough=False
                   new_game = input("Do you want to continue: y or n\n")
                   if new_game == "y":
                      cont()
                   elif sum_of_player>sum_of_computer:
                        print("Player Win!!!")
                        new = False
                        loop = False
                        not_enough = False
                        new_game = input("Do you want to continue: y or n\n")
                        if new_game == "y":
                           cont()
cont()










