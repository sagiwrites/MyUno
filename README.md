# MyUno
Online Uno Game
The python package “RANDOM” is used to shuffle and distribute the elements of the list of the deck of the cards, randomly among the players. The console is cleared after every turn (time for the current player to handover the console to the next player) in the terminal. For every round, the player must input the card from his set of cards and the loops and iterations are used to check the match for the open card (from the sample space/acceptability/next player end) or draw from the deck (another random number(key) generator).

The time module is used to provide time for card updation and console change time between players.

The OS module used in the code provides for interacting with the operating system i.e. when the game is played, it clears the previous players list and displays only the current player list(to provide card secrecy).

I used many individual functions to categorize the code into multiple repetitive blocks. As the game itself is a round-the-table 7 card limited player game, the functions can be used to call repetitively and iteratively (Calling-Called Function).
The main function calls the individual functions [playercheck -> Deck Setup -> First Distribution -> Maingame]
The Maingame function calls the normaldeal, Cardmatchchek, Reverse_order, Exception_Handling functions which are repetitive for each round and each individual player.
When the deck1 is empty the Maingame function handles it as a “Draw” game and terminates the game then and there and if any 1 player completes all his cards[list of cards is empty] checked at every round in the normaldeal function, the game is won by that player.
