import random
import time
import os

def deck_setup(number_of_players):
    
    deck1 = ["0blue", "1blue", "1blue", "2blue", "2blue", "3blue", "3blue",
             "4blue", "4blue","5blue", "5blue", "6blue", "6blue", "7blue", 
             "7blue", "8blue", "8blue", "9blue", "9blue", "Sblue", "Sblue",
             "Rblue", "Rblue", "D2blue", "D2blue",

             "0red", "1red", "1red", "2red", "2red", "3red", "3red", "4red",
             "4red", "5red", "5red", "6red", "6red", "7red", "7red", "8red",
             "8red", "9red", "9red", "Sred", "Sred", "Rred", "Rred", "D2red",
             "D2red",

             "0yellow", "1yellow", "1yellow", "2yellow", "2yellow", "3yellow",
             "3yellow", "4yellow", "4yellow", "5yellow", "5yellow", "6yellow",
             "6yellow", "7yellow", "7yellow", "8yellow", "8yellow", "9yellow",
             "9yellow", "Syellow", "Syellow", "Ryellow", "Ryellow", "D2yellow",
             "D2yellow",

             "0green", "1green", "1green", "2green", "2green", "3green",
             "3green", "4green", "4green", "5green", "5green", "6green",
             "6green", "7green", "7green", "8green", "8green", "9green",
             "9green", "Sgreen", "Sgreen", "Rgreen", "Rgreen", "D2green",
             "D2green",

             "Wild1", "Wild2", "Wild3", "Wild4",
             "D4Wild1", "D4Wild2", "D4Wild3", "D4Wild4", ]

    if number_of_players > 4:
        deck1 = 2 * deck1
    random.shuffle(deck1)
    return deck1


##############################################################################

def playercheck():
    # players = 0
    print("enter number of players:")
    players = int(input())

    if players >= 1 and players <= 8:
        print(" \n Game set for Play \n")

    else:
        print(" \n Invalid number of players,PLease choose 1 to 8 players to proceed \n")
        players = playercheck()

    return players, playerlists(players)

##############################################################################

def playerlists(number):
    plist = []
    for i in range(1, number + 1):
        plist.append([])
    return (plist)

##############################################################################
    
def firstdistribution(players,pLayerlists,finaldeck):

    card_track = []
    for i in range(1, 8): 
        for j in range(0, players):
            k = 0
            while k == 0:
                card = finaldeck[0]
                finaldeck = finaldeck[1:]
                if card in finaldeck:
                    card_track.append(card)
                    pLayerlists[j-1].append(card)

                    k = k + 1

    return finaldeck

###############################################################################

def reverse_order(player_turn,i):
    for m in range(0, len(player_turn)):
        if player_turn[m] == i:
            reverse_list = player_turn[0:m]
            reverse_list.reverse()
            player_turn_reverse = player_turn.copy()
            player_turn_reverse.reverse()
            player_turn = player_turn[0:m + 1] + reverse_list + player_turn_reverse
    return player_turn

###############################################################################
    
def exception_handling(player_turn,i):
    try:
        player_turn[i+1]
    except:
        player_turn = player_turn + player_turn
    return player_turn

###############################################################################
    
def maingame(player_list, finaldeck, opencard):
    game_ends = 0
    player_turn = []
    for i in range(0, players):
        player_turn.append(i)

    while not game_ends:
        for i in player_turn:

            print(" \n Player" + str(i+1) + " turn to play:")
            if opencard[0] in ['0','1','2','3','4','5','6','7','8','9']:
                opencardcolor = opencard[1:]
            elif opencard.startswith('Wild'):
                print("Please enter color: ")
                opencardcolor = input()
            elif opencard.startswith('S') or opencard.startswith('R'):
                opencardcolor = opencard[1:]
            elif opencard.startswith('D2') :
                opencardcolor = opencard[2:]
            elif opencard.startswith('D4'):
                print("please enter color : ")
                opencardcolor = input()

            opencard,player_turn,finaldeck = normaldeal(opencard, opencardcolor, player_list, i, finaldeck, player_turn)
            player_turn = exception_handling(player_turn, i)
            os.system('cls')
        if not finaldeck:
            print(" \n \n Game Drawn  \n  \n")
            game_ends = 1

###############################################################################

def normaldeal(opencard, opencardcolor, player_list, i,final_deck,player_turn):
    print(" \n Open card is:" + opencard)
    if opencard.startswith("R"):
        print(" \n Player played reverse card")       
        player_turn = reverse_order(player_turn, i)
        time.sleep(3)
        print(player_turn)
        opencard = opencard[1:]

    else:
        print(" \n Deal with a card in " + opencardcolor + " color")

        print("\n Your cards are :" +str( player_list[i]))
        print("\n Choose your choice of play: \n Go for new card--> NC \n Play your card-->PC \n Player "+str(i+1))
        choose = input()
        if choose == "NC":
            if opencard.startswith("S"):
                print("Player chance skipped")
            elif opencard.startswith('Wild'):
                print('Do nothing')
            elif opencard.startswith("D2"):
                print("Your cards are being updated")
                for m in range(0,2):
                    player_list[i].append(final_deck[0])
                    final_deck = final_deck[1:]
                    time.sleep(3)
            else:
                player_list[i].append(final_deck[0])
                final_deck = final_deck[1:]
            print("Your updated list is :",player_list[i])
            time.sleep(2)
        elif choose == "PC":
            print("choose the card you want to open")
            playedcard = input()
            print('checking')
            time.sleep(2)
            opencard,player_list,final_deck = cardmatchcheck(playedcard,opencard,player_turn,i,player_list,final_deck)

            if not player_list:  # checking if player cards are done
                print("\n Player" + i + "has finished his game \n game ends here")
                exit()
            elif opencard.startswith("Wild"):
                print("\n Choose color of your choice :")
                opencardcolor = input()
                opencard = opencardcolor
            elif opencard.startswith('R'):
                print("\n Reverse the order")
                player_turn = reverse_order(player_turn,i)
                print(player_turn)
                  
        else:
            print("incorrect choice \n choose again as per the instructions")
            normaldeal(opencard, opencardcolor, player_list, i,final_deck,player_turn)

    return opencard,player_turn,final_deck

##############################################################################
    
def cardmatchcheck(playedcard, opencard,player_turn,i,player_list,final_deck):  # to check if open card and played card are in compliance
    colors = ["yellow", "red", "blue", "green"]

    if opencard == playedcard:
        print("exact card dealt")
        print("option 1")
        player_list[i].remove(playedcard)
        print('Updated list is :', player_list[i])
        return playedcard,player_list,final_deck

    elif opencard[0] == playedcard[0]:
        print("number matched card dealt")
        print("option 2")
        player_list[i].remove(playedcard)
        print('Updated list is :', player_list[i])
        return playedcard,player_list,final_deck

    elif (opencard[0]) in ['0','1','2','3','4','5','6','7','8','9']:
        print('YES 2 ',playedcard, player_turn)
        if opencard[1:] == playedcard[1:]:
            if playedcard[0] in ['0','1','2','3','4','5','6','7','8','9']:
                print("color matched card dealt")
                print("option 3")
                player_list[i].remove(playedcard)
                print(' \n \n Updated list is :', player_list[i])
                return playedcard,player_list,final_deck
            elif playedcard[0] == 'S':
                print("Player played skip card")
                player_list[i].remove(playedcard)
                print('\n \n Updated list is :', player_list[i])
                return playedcard,player_list,final_deck
            elif playedcard[0] == 'R':
                print("Player played reverse card")
                player_list[i].remove(playedcard)
                print('\n \n Updated list is :', player_list[i])
                return playedcard,player_list,final_deck
            elif playedcard.startswith("D2") and opencard[1:] == playedcard[2:]:
                print("Player played with Draw 2 card of same color")
                player_list[i].remove(playedcard)
                print('Updated list is :', player_list[i])
                return playedcard,player_list,final_deck
            elif playedcard.startswith('Wild'):
                print("player played with wild card")
                player_list[i].remove(playedcard)
                print('Updated list is :', player_list[i])
                return playedcard,player_list,final_deck
            elif playedcard.startswith('D4') and playedcard[2:] == opencard[1:]:
                print("player played with wild card")
                player_list[i].remove(playedcard)
                print('Updated list is :', player_list[i])
                return playedcard,player_list,final_deck

        elif playedcard.startswith('D2') and opencard[1:] == playedcard[2:]:
            print("color matched with Draw2 card, card dealt")
            print("option 3")
            player_list[i].remove(playedcard)
            print('\n \n Updated list is :', player_list[i])
            return playedcard,player_list,final_deck
        elif playedcard.startswith('S') and opencard[1:] == playedcard[1:]:
            print("color matched with skip card, card dealt")
            print("option 4")
            player_list[i].remove(playedcard)
            print('\n \n Updated list is :', player_list[i])
            return playedcard,player_list,final_deck

    elif opencard.startswith("D2") == playedcard.startswith("D2"):

        print("\n \n Action Type card matched \n card dealt")
        print("option 7")
        player_list[i].remove(playedcard)
        print('Updated list is :', player_list[i])
        return playedcard,player_list,final_deck

    elif opencard.startswith("Wild") == playedcard.startswith("Wild"):
        print("\n \n Action Type card matched \n card dealt")
        print("enter color of your choice")
        playedcard = input()
        player_list[i].remove(playedcard)
        print('Updated list is :', player_list[i])
        return playedcard,player_list,final_deck

    elif opencard.startswith("D4Wild") :
        if playedcard.startswith("D4Wild"):
            print("\n \n Action Type card matched \n card dealt")
            print("option 9")
            player_list[i].remove(playedcard)
            print('Updated list is :', player_list[i])
            return playedcard,player_list,final_deck
        else:

            for i in range(1,5):
                player_list[i].append(final_deck[0])
                final_deck = final_deck[1:]
            return playedcard,player_list,final_deck

    else:  # already checked in normaldeal() , just an additional print for it
        print("\n you played: " + playedcard + "  it is invalid")
        print("option 10")
        return playedcard,player_list,final_deck

##############################################################################

if __name__ == "__main__":

    players, playerlists = playercheck()
    deck = deck_setup(players)

    finaldeck = firstdistribution(players,playerlists,deck)
    opencard = finaldeck[0]

    #
    maingame(playerlists, finaldeck, opencard)

##############################################################################