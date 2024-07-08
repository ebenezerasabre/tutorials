













import json
import random

# Character Classes
class Character:
    def __init__(self, name, hp, attack, defense, level=1):
                                # an integer that represents
        self.name = name        #attack power of the chrtr
        self.hp = hp            # health points of the chrtr, decrease when chrtr takes damage
        self.attack = attack    #exprnc points the character has accumulated, it reaches 10 his level increases
        self.defense = defense  #dfnsv power of the chrtr, reduces the damage taken from an enemy attack
        self.level = level      # crnt chrtr's level, starts at level 1 and increase by gaining experience
        self.experience = 0

    # a func to inflict damage on a player
    def take_damage(self, damage):
        self.hp -= max(0, damage - self.defense)

    # a function to check whether player is alive
    def is_alive(self):
        return self.hp > 0

    # a method to increase experience
    # Players expericen increase by 10 after he wins a battle
    # and his levels up
    def gain_experience(self, exp):
        self.experience += exp
        if self.experience >= self.level * 10:
            self.level_up()

    # method to level up
    def level_up(self):
        self.level += 1
        self.hp += 10
        self.attack += 5
        self.defense += 2
        self.experience = 0
        print(f"{self.name} leveled up to level {self.level}!")


# we will create different types of players with unique abilities

#Role: A  combat specialist with high physical strength and defense
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, hp=100, attack=20, defense=10)

#Role: A spellcaster who uses magic to deal damage or support allies.
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, hp=80, attack=30, defense=5)

#Role: A ranged combat specialist who excels at attacking from a distance.
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, hp=70, attack=25, defense=7)


""""

If you've ever played a game before your realize that the player can pick certain items
It could be a sword, or coins or stars
All those items are called inventory system


Inventory systems are important in game developement, It provides

Item Management: It allows players to collect, store, and manage items they find during their adventures. 
These items can include weapons, armor, potions, and other useful objects.

Resource Utilization: Players can use items from their inventory to heal, gain temporary boosts, or unlock new abilities.
This adds a strategic element to gameplay, as players must decide when and how to use their resources effectively.

Character Enhancement: The items in the inventory can enhance the character's abilities. 
For example, equipping a better weapon can increase attack power, while wearing better armor can increase defense.

Quest Items: Some items may be required to complete quests.
 The inventory keeps track of these items until they are used or given to NPCs.

"""


# First let us define an Item class
#Any item will have these attributes

# Inventory System
class Item:
    def __init__(self, name, item_type, effect):
        self.name = name
        self.item_type = item_type
        self.effect = effect

    # now we write the method that defines how to use an item
    # in this game we have two items Potion and Weapon
    def use(self, character):
        if self.item_type == 'potion':
            character.hp = min(character.hp + self.effect, character.level * 10 + 90)
            print(f"{character.name} used {self.name} and healed {self.effect} HP.")
        elif self.item_type == 'weapon':
            character.attack += self.effect
            print(f"{character.name} equipped {self.name} and gained {self.effect} attack.")



# And then an Inventory class
class Inventory:
    def __init__(self):
        self.items = []

    # we can add an item
    def add_item(self, item):
        self.items.append(item)

    #we should be able to remove items
    def remove_item(self, item):
        self.items.remove(item)

    #To use an item
    # we will loop through our items
    # use, we remove it when we are done
    def use_item(self, item_name, character):
        for item in self.items:
            if item.name == item_name:
                item.use(character)
                self.remove_item(item)
                return True
        # If i tem is not found
        print("Item not found.")
        return False

    # we can save an inventory
    def save_inventory(self, filename):
        with open(filename, 'w') as file:
            json.dump([item.__dict__ for item in self.items], file)

    # we can load an inventory
    def load_inventory(self, filename):
        with open(filename, 'r') as file:
            items = json.load(file)
            self.items = [Item(item['name'], item['item_type'], item['effect']) for item in items]




"""

The battle system in this game is a turn-based combat mechanism
where the player and enemies take turns to attack each other.

During each turn, the player can choose to perform actions such as attacking,
using an item from the inventory, or executing special abilities
 unique to their character class (Warrior, Mage, Archer).

The goal is to reduce the opponent's HP to zero while
keeping the player's character alive.

"""


# Battle System
# we will create a function for battle
def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        enemy.take_damage(player.attack)
        if enemy.is_alive():
            player.take_damage(enemy.attack)
        print(f"{player.name} HP: {player.hp}")
        print(f"{enemy.name} HP: {enemy.hp}")
    if player.is_alive():
        print("You won the battle!")
        player.gain_experience(10)
    else:
        print("You were defeated...")

 

""""
An important import of any game is the ability of a player to move
Sometimes the movement of a player can trigger an even
For example if the player touches a star his life span increase or whatever
In this game the play can be able to move north, south, east and west


Movement and Navigation: It allows the player to move between different locations on the map. 
The Map class can define possible movements and ensure that the player
 follows the intended paths within the game world.

Event Triggering: The map can trigger events when the player enters certain locations. 
These events can include encounters with enemies, finding items, meeting NPCs, or starting quests.

"""

# Map Exploration
class Map:
    def __init__(self, size):
        self.size = size
        self.map = [['.' for _ in range(size)] for _ in range(size)]
        self.player_pos = [size // 2, size // 2]

    # define how player moves
    def move_player(self, direction):
        if direction == 'north' and self.player_pos[0] > 0:
            self.player_pos[0] -= 1
        elif direction == 'south' and self.player_pos[0] < self.size - 1:
            self.player_pos[0] += 1
        elif direction == 'east' and self.player_pos[1] < self.size - 1:
            self.player_pos[1] += 1
        elif direction == 'west' and self.player_pos[1] > 0:
            self.player_pos[1] -= 1

        event = random.choice(['enemy', 'treasure', 'npc', 'nothing'])
        return event



""""
Quests give players specific objectives to accomplish within the game world.
 These objectives can range from simple tasks like fetching an item to 
 complex missions involving multiple steps and challenges.

Completing quests often rewards players with experience points, 
items (such as weapons or armor), in-game currency, or access to new areas.
This encourages exploration and engagement with the game's content.

"""

# Quests and Storyline
class Quest:
    def __init__(self, description, reward):
        self.description = description
        self.completed = False
        self.reward = reward

    def complete_quest(self, player):
        self.completed = True
        player.gain_experience(self.reward)
        print(f"Quest '{self.description}' completed! You gained {self.reward} experience.")


# The quest file has to be provided as part of the game
# Hence it has to be loaded
def load_quests(filename):
    quests = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 2:
                print(f"Skipping invalid line in quests file: {line}")
                continue
            description, reward = parts
            try:
                reward = int(reward)
                quests.append(Quest(description, reward))
            except ValueError:
                print(f"Invalid reward value: {reward} in line: {line}")
    return quests



"""
We will create a Non-Player character class
It will be responsible for quest management and also dialog
Which are not under the players control
It represents Characters controlled by the game's intelligence

"""

# NPC Interactions
class NPC:
    def __init__(self, name, dialog, quest=None):
        self.name = name
        self.dialog = dialog
        self.quest = quest

    def interact(self, player):
        print(f"{self.name}: {self.dialog}")
        if self.quest and not self.quest.completed:
            print(f"Quest available: {self.quest.description}")
            accept = input("Do you accept the quest? (yes/no): ")
            if accept.lower() == 'yes':
                return self.quest
        return None

# Let's define the main flow of the game
# We will start by providing the player with some options to choose from

# Main Game
def main():
    print("Welcome to QuestMaster: The Text-Based RPG Adventure!")
    while True:
        print("\nMain Menu:")
        print("1. Start New Game")
        print("2. Load Game")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            start_new_game()
        elif choice == '2':
            load_game()
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

# if he chooses to play a new game, he will hav to choose his character
def start_new_game():
    # when starting a new game, we ask the user for his name
    name = input("Enter your character's name: ")

    # after that user has to select his player type
    print("Choose your class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    class_choice = input("Choose a class: ")

    if class_choice == '1':
        player = Warrior(name)
    elif class_choice == '2':
        player = Mage(name)
    elif class_choice == '3':
        player = Archer(name)
    else:
        print("Invalid choice, defaulting to Warrior.")
        player = Warrior(name)

    # Then we will set up an inventory for him and add defualt items to his inventory
    inventory = Inventory()
    inventory.add_item(Item("Health Potion", "potion", 20))
    inventory.add_item(Item("Iron Sword", "weapon", 10))
    game_map = Map(5)                   # we will provide a map to track his movement
    quests = load_quests('quests.txt')  # and finally load the quests that he can embark on
    
    # Check if quests are available
    if not quests:
        print("No quests available. Please add quests to 'quests.txt'.")
        return

    # we call NPC to make interraction with the player
    # we look at our loaded quests and show one
    npcs = [NPC("Old Man", "Welcome to our village! We need your help.", quests[0])]


    #Now if the player is alive we will provide him with
    #  what he can do in the game and get his choice
    while player.is_alive():

        print("\nGame Menu:")
        print("1. Explore")
        print("2. Check Inventory")
        print("3. View Quests")
        print("4. Save Game")
        print("5. Quit")
        choice = input("Choose an option: ")   

        #depending on his choice
        if choice == '1':
            # event is returned after player is moved
            # he can meet an enemy, a treasure, npc or nothing
            event = game_map.move_player(random.choice(['north', 'south', 'east', 'west']))
            if event == 'enemy':
                enemy = Warrior("Goblin")
                print("An enemy appears!")
                battle(player, enemy)
            elif event == 'treasure':
                print("You found a treasure!")
                inventory.add_item(Item("Gold", "treasure", 0))
            elif event == 'n`pc':
                npc = random.choice(npcs)
                print(f"You meet {npc.name}.")
                quest = npc.interact(player)
                if quest:
                    quests.append(quest)
            else:
                print("Nothing happens.")

        #choice 2 is for inventory
        elif choice == '2':
            print(f"Inventory: {[item.name for item in inventory.items]}")
            item_choice = input("Enter item name to use or 'back' to return: ")
            if item_choice != 'back':
                inventory.use_item(item_choice, player)
        
        #If he chooses 3 he wants to see the quests
        elif choice == '3':
            print("Quests:")
            for quest in quests:
                status = "Completed" if quest.completed else "Incomplete"
                print(f"- {quest.description} [{status}]")
        elif choice == '4':
            save_game(player, inventory, game_map, quests)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

"""
We can define a function to save the game
"""

def save_game(player, inventory, game_map, quests):
    # we will create a file save_game.json
    # and get the state of the game
    with open('save_game.json', 'w') as file:
        game_state = {
            'player': {
                'name': player.name,
                'hp': player.hp,
                'attack': player.attack,
                'defense': player.defense,
                'level': player.level,
                'experience': player.experience
            },
            'inventory': [item.__dict__ for item in inventory.items],
            'player_pos': game_map.player_pos,
            'quests': [{'description': quest.description, 'completed': quest.completed, 'reward': quest.reward} for quest in quests]
        }
        # we will serialize python object into JSON formata
        # and write them to the file
        json.dump(game_state, file)
    print("Game saved.")

"""
If we choose to load a new game instead of start a new One
We have to load previously saved game
"""

def load_game():
    try:
        # we open the json file we saved the game state
        with open('save_game.json', 'r') as file:
            game_state = json.load(file)
            player_data = game_state['player']
            player = Character(player_data['name'], player_data['hp'], player_data['attack'], player_data['defense'], player_data['level'])
            player.experience = player_data['experience']
            
            # we will get the inventory
            inventory = Inventory()
            for item_data in game_state['inventory']:
                inventory.add_item(Item(item_data['name'], item_data['item_type'], item_data['effect']))
            
            # get plays movements from map
            game_map = Map(5)
            game_map.player_pos = game_state['player_pos']
            
            # get the quests
            quests = []
            for quest_data in game_state['quests']:
                quest = Quest(quest_data['description'], quest_data['reward'])
                quest.completed = quest_data['completed']
                quests.append(quest)
            
            # and also the Non-Player Character Interactions
            npcs = [NPC("Old Man", "Welcome to our village! We need your help.", quests[0])]
            
            while player.is_alive():
                print("\nGame Menu:")
                print("1. Explore")
                print("2. Check Inventory")
                print("3. View Quests")
                print("4. Save Game")
                print("5. Quit")
                choice = input("Choose an option: ")

                if choice == '1':
                    event = game_map.move_player(random.choice(['north', 'south', 'east', 'west']))
                    if event == 'enemy':
                        enemy = Warrior("Goblin")
                        print("An enemy appears!")
                        battle(player, enemy)
                    elif event == 'treasure':
                        print("You found a treasure!")
                        inventory.add_item(Item("Gold", "treasure", 0))
                    elif event == 'npc':
                        npc = random.choice(npcs)
                        print(f"You meet {npc.name}.")
                        quest = npc.interact(player)
                        if quest:
                            quests.append(quest)
                    else:
                        print("Nothing happens.")
                elif choice == '2':
                    print(f"Inventory: {[item.name for item in inventory.items]}")
                    item_choice = input("Enter item name to use or 'back' to return: ")
                    if item_choice != 'back':
                        inventory.use_item(item_choice, player)
                elif choice == '3':
                    print("Quests:")
                    for quest in quests:
                        status = "Completed" if quest.completed else "Incomplete"
                        print(f"- {quest.description} [{status}]")
                elif choice == '4':
                    save_game(player, inventory, game_map, quests)
                elif choice == '5':
                    break
                else:
                    print("Invalid choice, please try again.")
    except FileNotFoundError:
        # if no game was saved then we will start a new game
        print("No saved game found. Starting a new game.")
        start_new_game()

if __name__ == "__main__":
    main()

