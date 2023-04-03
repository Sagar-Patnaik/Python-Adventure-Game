Name: Sagar Patnaik
StevensLogin: spatnaik@stevens.edu

GitHUb Link :- https://github.com/Sagar-Patnaik/Python-Adventure-Game

Estimated time spent in hours: 40

To test adventure.py, I designed test cases and compared the expected output to the actual output to ensure accuracy. I had to meticulously match the output bit by bit, checking for errors and discrepancies to ensure the program functioned correctly.

Text-based Adventure Game
This text-based adventure game is a simple game built using Python. In the game, the player is stuck in a prison and must escape by navigating through various rooms, picking up items, and interacting with objects to progress.The game is played entirely through the command line, and the player interacts with the game by entering commands such as "go north" or "get key". The game consists of a series of rooms that the player can navigate through, each with its own description and set of exits. The objective of the game is to escape from a prison by finding and using various items scattered throughout the rooms. The game is implemented using JSON data to store the game world, and various Python data structures and control structures to implement the game mechanics.



Game Setup
The game data is stored in a JSON file of ".map" extention type. It is provided to the game via commandline argument and is loaded into the game using the json library. Each room in the game has a name, a description, and a list of exits that the player can use to navigate to other rooms. Additionally, rooms can contain items that the player can pick up and add to their inventory.

Game Loop
The game loop is the main loop that runs the game. It uses a while loop to continually prompt the user for input and process their commands until the game is over. Within the game loop, the following steps are taken:


Print the current room description, available exits, and available items (if any).
Prompt the user for input.
Parse the user's input into a verb and a noun (if applicable).
Process the user's input by executing the appropriate action based on the verb and noun.
The game loop can be exited by entering the quit command or by navigating to the "Outside" room, which signifies that the player has escaped the prison and won the game.


Valid Verbs
The game has a set of valid verbs that the player can use to interact with the game world. These verbs and their descriptions are defined in a dictionary called verbs. The valid verbs are:

help: Print all possible verbs.
look: Print a description of the current room.
go: Move to another room in the specified direction.
get: Pick up an item in the current room and add it to your inventory.
drop: Drop an item in the current room.
inventory: Display the items currently in your inventory.
quit: Exit the game.


Error Handling
The game contains some basic error handling to ensure that the game data is valid and that the player's commands are valid. For example, the game checks that all rooms have a name field and that all exits lead to valid rooms. If an error is detected, the game will print an error message and exit.


Running the Game
To run the game, simply run the Python script in a terminal or command prompt. The game will begin and the player can start entering commands to interact with the game world. To exit the game, simply enter the quit command or navigate to the "Outside" room.

Note: the game data is stored in a JSON file called "test.map". If you want to create your own game or modify the existing game, you can create a new JSON file and modify the game data accordingly.


How to Play
Download the code and save it to your local machine.
Open the terminal or command prompt and navigate to the folder where the code is saved.
Run the command python game.py to start the game.
The game will start with a description of your current location and available exits.
Use the commands to navigate through the game and collect items:
help: displays all possible commands
look: displays the description of the current location
go <direction>: move to another location
get <item>: pick up an item in the current location
drop <item>: drop an item from your inventory in the current location
inventory: displays the items in your inventory
quit: exits the game
Use the collected items to solve puzzles and find a way to escape the prison.
If you successfully find your way out of the prison along with required inventory, you win the game.


 ---Game MAP---
  
![image](https://user-images.githubusercontent.com/129694148/229389599-d8f43c6a-bbf5-4536-884d-3062140101dc.png)




Winning Condition
Move to the room leading "outside" and have "kinfe" and "rope" in your inventory.

How to Win
To win the game, you have to find a way to escape the prison. Explore different locations, collect items and use them to solve puzzles. Some items may be hidden, so be sure to thoroughly search each location. Once you have collected all the necessary items and solved all the puzzles, you will find a way out of the prison and win the game.

Good luck and have fun!


Enhancements
1. The "Directions become verbs" enhancement allows players to use cardinal directions as verbs to navigate the game world. When a player types a direction as a verb, the code maps it to the "go" verb and sets the noun to the corresponding direction. This enhances the gameplay experience by providing a more natural language interface for movement. It reduces the need for players to memorize specific commands, and instead allows them to use more intuitive language. This enhancement is simple and easy to implement and is a great addition to any text-based game.

2. The "help" verb is an essential feature of any text-based adventure game, providing players with a list of valid verbs they can use to interact with the game world. In our game, the help verb will print all the possible verbs the player can use. This can be incredibly useful for new players who may not be familiar with the game mechanics or for players who have forgotten certain commands. By providing a comprehensive list of valid verbs, players can feel more in control of their experience, and the game can become more accessible to a wider audience.

3. The "drop" verb allows the player to remove an item from their inventory and place it in the current room for others to find or interact with.



Note for Testers
If using a different map, it is important to ensure that it has the same basic structure with different rooms connected by exits. Additionally, it should have a room named "outside" with no exits, as this is the ultimate goal of the game. It is also important to ensure that the items "rope" and "knife" are present in some rooms as they are necessary for completing certain tasks in the game. Finally, each room should have a clear and descriptive name and description to help the player understand their surroundings and make informed decisions about their actions.


Possible Improvements
There are several possible improvements that could be made to the game, including:

Adding more rooms and puzzles to increase the complexity of the game.
Implementing a scoring system to encourage the player to explore and interact with the game world.
Adding more descriptive text to enhance the player's immersion in the game world.
Implementing a save/load system so that the player can save their progress and resume the game later.
Adding more complex interactions between items and objects in the game world.
