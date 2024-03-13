clues = [
    "There is a faded newspaper article about a major fire in the city many years ago.",
    "There is an old diary describing a secret love affair.",
    "There is a worn-out children's book left open on a page with a scary story.",
    "There is a mysterious key with an engraved symbol that cannot be recognized.",
    "There is a dusty hat that seems to have belonged to a wealthy person.",
    "There is a shattered vase that seems to have been very valuable.",
    "There is an old photograph of a group of people looking very happy.",
    "There is a strange stone with an unusual pattern that doesn't look like anything from this world.",
    "There is an old medal for bravery in a war that has been forgotten by time.",
    "There is a cryptic note written in a language that is hard to decipher."
]

sense_exp = [
    "You see a flickering candle casting long, dancing shadows on the stone walls.",
    "You hear the distant echo of footsteps, but you can't tell where they're coming from.",
    "You smell the musty scent of old books and parchment.",
    "You touch the cold, rough stone of the castle walls, worn by time.",
    "You intuit a sense of unease, as if the castle itself is watching you.",
    "You see a grand tapestry, its colors faded but its story still vibrant.",
    "You hear the soft rustling of a curtain in the breeze, the sound strangely comforting.",
    "You smell the faint aroma of a meal cooked long ago, now just a ghost of a memory.",
    "You touch the worn wooden handle of a door, wondering who else has used it over the centuries.",
    "You intuit a sense of history, the weight of countless stories played out within these walls.",
    "You see the moonlight filtering through a cracked window, casting an eerie glow.",
    "You hear the distant hoot of an owl, the only sign of life in the silent night."
]

import random

class RandomItemSelector:
    def __init__(self, items):
        self.items = items
        self.used_items = []

    def add_item(self, item):
        self.items.append(item)

    def pull_random_item(self):
        if not self.items:
            return None
        if not set(self.items) - set(self.used_items):
            self.used_items = []
        item = random.choice(list(set(self.items) - set(self.used_items)))
        self.used_items.append(item)
        return item

    def reset(self):
        self.used_items = []

#from randomitemselector import RandomItemSelector
from enum import Enum

class SenseClueGenerator:
    _instance = None

    def __new__(cls, clues, sense_exp):
        if cls._instance is None:
            cls._instance = super(SenseClueGenerator, cls).__new__(cls)
            cls._instance.clue_selector = RandomItemSelector(clues)
            cls._instance.sense_selector = RandomItemSelector(sense_exp)
        return cls._instance

    def get_senseclue(self):
        clue = self.clue_selector.pull_random_item()
        sense = self.sense_selector.pull_random_item()
        return f"{clue} {sense}"

class encounter_outcome(Enum):
    CONTINUE = 1
    END = 2


from abc import ABC, abstractmethod

class Encounter(ABC):
    @abstractmethod
    def run_encounter(self):
        pass

class DefaultEncounter(Encounter):
    def __init__(self, clues, sense_exp):
        self.sense_clue_generator = SenseClueGenerator(clues, sense_exp)

    def run_encounter(self):
        sense_clue = self.sense_clue_generator.get_senseclue()
        print(sense_clue)
        return encounter_outcome.CONTINUE


class Room:
    def __init__(self, name, encounter):
        self.name = name
        self.encounter = encounter

    def visit_room(self):
        return self.encounter.run_encounter()
    

room_names = ["Throne Room", "Armory", "Library", "Dungeon", "Observatory", "Royal Chamber"]
rooms = [Room(name, DefaultEncounter(clues, sense_exp)) for name in room_names]

class TreasureEncounter(Encounter):
    def run_encounter(self):
        print("You found the treasure! You have won the game.")
        return encounter_outcome.END

# add a Treasure Room to the list of rooms
rooms.append(Room("Treasure Room", TreasureEncounter()))

class RedWizardEncounter(Encounter):
    def __init__(self):
        self.game_rules = {
            "Fireball": ["Ice Shard", "Lightning Bolt"],
            "Ice Shard": ["Wind Gust", "Earthquake"],
            "Wind Gust": ["Lightning Bolt", "Fireball"],
            "Lightning Bolt": ["Earthquake", "Ice Shard"],
            "Earthquake": ["Fireball", "Wind Gust"]
        }

    def run_encounter(self):
        choices = list(self.game_rules.keys())
        while True:
            wizard_choice = random.choice(choices)
            user_choice = input("Choose your spell (Fireball, Ice Shard, Wind Gust, Lightning Bolt, Earthquake): ")
            if user_choice not in choices:
                print("Invalid spell. Please choose again.")
                continue
            print(f"Red Wizard casts {wizard_choice}.")
            if user_choice == wizard_choice:
                print("It's a draw. The battle continues.")
            elif user_choice in self.game_rules[wizard_choice]:
                print("You have been vanquished from this castle.")
                return encounter_outcome.END
            else:
                print("You have vanquished the Red Wizard from this castle.")
                return encounter_outcome.CONTINUE
            
# create a room called “The Red Wizard’s Lair” with the Red Wizard Encounter and add it to the rooms list

rooms.append(Room("The Red Wizard's Lair", RedWizardEncounter()))

class BlueWizardEncounter(Encounter):
    def __init__(self):
        self.game_rules = {
            "fireball": ["ice shard"],
            "ice shard": ["wind gust"],
            "wind gust": ["fireball"],
            "lightning bolt": ["earthquake"],
            "earthquake": ["fireball"]
        }

    def run_encounter(self):
        choices = list(self.game_rules.keys())
        while True:
            wizard_choice = random.choice(choices)
            user_choice = input("Choose your spell (fireball, ice shard, wind gust, lightning bolt, earthquake): ")
            if user_choice not in choices:
                print("Invalid spell. Please choose again.")
                continue
            print(f"Blue Wizard casts {wizard_choice}.")
            if user_choice == wizard_choice:
                print("It's a draw. Play again.")
            elif user_choice in self.game_rules[wizard_choice]:
                print("You have been vanquished from this castle.")
                return encounter_outcome.END
            else:
                print("You have vanquished the Blue Wizard from this castle.")
                return encounter_outcome.CONTINUE

# create a room called “The Blue Wizard’s Lair” with the Blue Wizard Encounter and add it to the rooms list
rooms.append(Room("The Blue Wizard's Lair", BlueWizardEncounter()))





class Castle:
    def __init__(self, rooms):
        self.room_selector = RandomItemSelector(rooms)

    def select_door(self):
        door_count = random.randint(2, 4)
        print(f"There are {door_count} doors. Choose a door number between 1 and {door_count}.")

        while True:
            door_number = input("Enter door number: ")
            if door_number.isdigit() and 1 <= int(door_number) <= door_count:
                return int(door_number)
            else:
                print("Invalid input. Please enter a valid door number.")

    def next_room(self):
        self.select_door()
        room = self.room_selector.pull_random_item()
        print(f"You have entered the {room.name}.")
        return room.visit_room()

    def reset(self):
        self.room_selector.reset()


class Game:
    def __init__(self, rooms):
        self.castle = Castle(rooms)

    def play_game(self):
        print("Welcome to the Castle! Your objective is to navigate through the castle and find the treasure.")

        while True:
            outcome = self.castle.next_room()
            if outcome == encounter_outcome.END:
                self.castle.reset()
                print("Game Over. You have found the treasure!")
                play_again = input("Would you like to explore a different castle? (yes/no): ")
                if play_again.lower() != "yes":
                    break



game = Game(rooms)
game.play_game()

 