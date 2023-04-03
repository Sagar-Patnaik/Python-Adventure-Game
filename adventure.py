import json
import sys

# Checking if the Map filename argument is provided
if len(sys.argv) < 2:
    print("Please enter a Map File name for the game while entering run command.")
    sys.exit(1)

# Store the filename in a variable
filename = sys.argv[1]

# Loading game data from json file
with open(filename, 'r') as f:
    game_data = json.load(f)

# Variables required in game.
current_room = game_data[0]
game_status = 'prison'  # Setting the initial game status to prison
room_name = current_room
room_change = 'New'
inventory = []

# Creating a dictionary containing a list of valid verbs along with their respective descriptions or meanings.
verbs = {
    'help': 'Print all possible verbs.',
    'look': 'Print a description of the current room.',
    'go': 'Move to another room in the specified direction.',
    'get': 'Pick up an item in the current room and add it to your inventory.',
    'drop': 'Drop an item in the current room',
    'inventory': 'Display the items currently in your inventory.',
    'quit': 'Exit the game.'
}

# Check that all rooms have a name field
for room in game_data:
    if "name" not in room:
        print("Error: A room does not have a name field!")
        exit()

# check that all exits lead to valid rooms
for i, room in enumerate(game_data):
    if room["name"] == "Outside":
        continue
    if "exits" not in room:
        continue
    for exit_index in room["exits"].values():
        if exit_index >= len(game_data) or exit_index < 0:
            print(f"Error: Room {room['name']} has an exit to a non-existent room ({exit_index})!")
            exit()

# Game loop
while True:
    try:

        # Getting the name of the current room
        for room_data in game_data:
            if room_data['name'] == current_room['name']:
                room_name = room_data['name']
                break

        if room_change == 'New':
            # Printing current room description
            print('\n> ' + room_name + '\n')
            print(current_room['desc'])

            if room_name == 'Outside':
                print("\nGoodbye!")
                break

            # Printing available exits
            if 'exits' in current_room:
                print('\nExits:', ', '.join(current_room['exits']), '\n')

            # Printing available items (if any)
            if 'items' in current_room and current_room['items']:
                print('Items:', ', '.join(current_room['items']), '\n')

            # Changing room_change status
            room_change = 'old'

        # Prompting user for input
        user_input = None
        user_input = input('What would you like to do? ').strip().lower().split()

        # Parsing user input
        verb = user_input[0]

        if len(user_input) > 1:
            noun = user_input[1]
        else:
            noun = None

        # Special conditional check for Directions become verbs.
        if noun is None and verb is not {'go','get','drop','inventory','inv','help','look','quit'}:
            if 'east'.startswith(verb):
                verb = 'go'
                noun = 'east'

            elif 'west'.startswith(verb):
                verb = 'go'
                noun = 'west'

            elif 'north'.startswith(verb):
                verb = 'go'
                noun = 'north'

            elif 'south'.startswith(verb):
                verb = 'go'
                noun = 'south'

            elif verb == 'nw':
                verb = 'go'
                noun = 'north-west'

            elif verb == 'ne':
                verb = 'go'
                noun = 'north-east'

            elif verb == 'sw':
                verb = 'go'
                noun = 'south-west'

            elif verb == 'se':
                verb = 'go'
                noun = 'south-east'

        # Processing user input
        if verb == 'quit':
            print('Goodbye!')
            break

        elif verb == 'help':
            print('Possible verbs:')
            for key, value in verbs.items():
                print(key + ':', value)

        elif verb == 'drop':
            if not inventory:
                print("You're not carrying anything.")

            elif noun in inventory:
                inventory.remove(noun)
                if 'items' in current_room:
                    current_room['items'].append(noun)
                else:
                    current_room['items'] = [noun]
                print('You have dropped the {}.'.format(noun))
            elif noun is None:
                print('Sorry, you need to \'drop\' something.')
            else:
                print("You don't have {} in your inventory.".format(noun))

        elif verb == 'look':
            room_change = 'New'
            pass

        elif verb == 'go':
            if noun in current_room['exits']:
                print(f'You go {noun}.')

                # Condition for winning.
                temp_room = current_room
                current_room = game_data[current_room['exits'][noun]]

                # Updating the room name if the player has moved to a new room
                room_name = current_room['name']

                # Updating the room change status if the player has moved to a new room
                room_change = 'New'

                # Checking if the player has escaped the prison
                if room_name == 'Outside':
                    if 'rope' in inventory and 'knife' in inventory:
                        game_status = 'escaped'
                        print('\nYou are escaping the prison.')

                    else:
                        current_room = temp_room
                        print("But you cant escape!!!. You lack necessary items in inventory to make this move successful\n")
                        room_change = 'Old'

            elif noun is None:
                print('Sorry, you need to \'go\' somewhere')

            else:
                print("There's no way to go {}.".format(noun))

        elif verb == 'get':
            if noun in current_room['items']:
                current_room['items'].remove(noun)
                print('You are picking up the {}.'.format(noun))
                inventory.append(noun)

            elif noun is None:
                print('Sorry, you need to \'get\' something.')

            else:
                print('There is no {} here.'.format(noun))

        elif verb == 'inventory' or verb == 'inv':
            if not inventory:
                print("You're not carrying anything.")

            else:
                print("Inventory:")
                for item in inventory:
                    print("  " + item)
        else:
            print("I don't understand that.")

    except EOFError:
        print("Use 'quit' to exit.")
        pass