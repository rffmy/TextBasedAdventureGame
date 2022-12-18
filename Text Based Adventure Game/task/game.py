# write your code here
import json
import re
import os
import sys
from termcolor import cprint


def get_top_menu_input():
    print("***Welcome to the Journey to Mount Qaf***\n")

    print("1- Press key '1' or type 'start' to start a new game")
    print("2- Press key '2' or type 'load' to load your progress")
    print("3- Press key '3' or type 'quit' to quit the game")

    return input()


def process_top_menu_input(top_menu_input):
    if top_menu_input == "1" or top_menu_input.lower() == "start":
        return 1
    elif top_menu_input == "2" or top_menu_input.lower() == "load":
        return 2
    elif top_menu_input == "3" or top_menu_input.lower() == "quit":
        return 3
    else:
        return -1


def set_difficulty():
    print("Choose your difficulty:\n1- Easy\n2- Medium\n3- Hard\n")

    diff = input().lower().capitalize()

    diff_dict = {"1": "Easy", "2": "Medium", "3": "Hard", "Easy": "Easy", "Medium": "Medium", "Hard": "Hard"}
    lives_dict = {"1": 5, "2": 3, "3": 1, "Easy": 5, "Medium": 3, "Hard": 1}

    if diff not in diff_dict:
        alert_unknown_input()
        diff_str, lives = set_difficulty()
    else:
        diff_str = diff_dict[diff]

    return diff_str, lives_dict[diff_str]


def prompt_user_input(story, level, scene):
    print("What will you do? Type the number of the option or type '/h' to show help.\n")

    choices = story['choices'][f'lvl{level}'][f'scene{scene}']

    choices_print = ""
    for choice in choices:
        choices_print += choice[-1] + '- ' + choices[choice]

    return input(choices_print)


def alert_unknown_input():
    print("Unknown input! Please enter a valid one.")


def prompt_to_quit_game():
    while True:
        quit_y_n = input("You sure you want to quit the game? Y/N\n")

        if quit_y_n.capitalize() == 'Y':
            print("Goodbye!")
            sys.exit()
        elif quit_y_n.capitalize() == "N":
            return
        else:
            alert_unknown_input()


def show_help():
    print('''Type the number of the option you want to choose.
Commands you can use:
/i => Shows inventory.
/q => Exits the game.
/c => Shows the character traits.
/h => Shows help.''')


def show_inventory(inv):
    print("Inventory:" + ",".join(inv) + "\n")


def show_character(char):
    print("Your character:", char["name"] + ",", char["species"] + ",", char["gender"])
    # print("Number of lives:", char["lives"], "\n")
    print("Lives remaining:", char["lives"], "\n")


def add_to_inventory(inv, item):
    inv.append(item)
    print("A new item has been added to your inventory: " + item + "\n")
    return inv


def remove_from_inventory(inv, item):
    if item in inv:
        inv.remove(item)
        print("An item has been removed from your inventory: " + item + "\n")
    else:
        print(item + " not in inventory!\n")
    return inv


def process_user_input(user_input, char, inv, story, level, scene):

    outcome_text, outcome_effects = None, None

    if user_input == "/i":
        show_inventory(inv)
    elif user_input == "/q":
        prompt_to_quit_game()
    elif user_input == "/c":
        show_character(char)
    elif user_input == "/h":
        show_help()
    elif user_input.isdigit():
        choices = story['choices'][f'lvl{level}'][f'scene{scene}']
        if 'choice' + user_input in choices:
            outcome = story['outcomes'][f'lvl{level}'][f'scene{scene}'][f'outcome{user_input}']

            if type(outcome) is dict:
                if level == 1 and scene == 2:
                    if "Key" in inv:
                        outcome = outcome['option1']
                    else:
                        outcome = outcome['option2']
                if level == 2 and scene == 2:
                    if 'Knife' in inv or 'Sword' in inv:
                        outcome = outcome['option1']  # Win!
                    else:
                        outcome = outcome['option2']

            outcome_text, outcome_effects = re.search(r'(.+)\((.+)\)', outcome).groups()
            outcome_effects = outcome_effects.split(' and ')

        else:
            alert_unknown_input()
    else:
        alert_unknown_input()

    return outcome_text, outcome_effects


def change_life_count(char, delta):
    char["lives"] += delta
    return char


def start_new_game():

    print("Starting a new game...")
    user_name = input("Enter a user name to save your progress or type '/b' to go back\n")

    if user_name == "/b":
        print("Going back to menu...")
        return

    char, inv = create_character(None)

    diff_str, char["lives"] = set_difficulty()

    print("Good luck on your journey!")

    print("Your character:", char["name"] + ",", char["species"] + ",", char["gender"])
    print(f"Your inventory: " + ", ".join(inv))
    print("Difficulty:", diff_str)
    print("Number of lives:", char["lives"], "\n")

    main_game_loop(char, user_name, diff_str, inv, 1, 1)


def save_game(user_name, char, diff_str, level):

    cprint("You've found a safe spot to rest. Saving your progress...", "green", "on_white")

    my_path = os.path.join('.', 'game/saves/', user_name + '.json')

    # https://hyperskill.org/projects/161/stages/837/implement#comment

    char_attrs = {
        "name": char["name"],
        "species": char["species"],
        "gender": char["gender"]
    }
    inventory = {
        "snack": char["snack"],
        "weapon": char["weapon"],
        "tool": char["tool"]
    }
    my_data = {
        "char_attrs": char_attrs,
        "inventory": inventory,
        "lives": char["lives"],
        "difficulty": diff_str,
        "level": level
    }

    with open(my_path, 'w') as f:
        json.dump(my_data, f, indent=4)


def create_character(saved_game):

    if saved_game is None:

        print("Create your character:")

        char = {"name": input("1- Name \n").capitalize(), "species": input("2- Species \n").capitalize(),
                "gender": input("3- Gender \n").capitalize()}

        print("Pack your bag for the journey:")

        inv = [None] * 3

        inv[0] = char["snack"] = input("1- Favourite Snack \n").capitalize()
        inv[1] = char["weapon"] = input("2- A weapon for the journey \n").capitalize()
        inv[2] = char["tool"] = input("3- A traversal tool \n").capitalize()

    else:

        char = {"name": saved_game['char_attrs']['name'], 'species': saved_game['char_attrs']['species'], 'gender': saved_game['char_attrs']['gender']}

        inv = [None] * 3

        inv[0] = char["snack"] = saved_game['inventory']['snack']
        inv[1] = char["weapon"] = saved_game['inventory']['weapon']
        inv[2] = char["tool"] = saved_game['inventory']['tool']

    return char, inv


def load_saved_game():
    # print("No save data found!")
    users, save_files = list_save_files()
    if save_files is None:
        print("No save data found!")
    else:
        print(f'Saved games for these users: {users}')
        user = input("Type your user name:\n")
        if user not in users:
            print("No save data found!")
        else:
            print(f"Loading game for user '{user}'")
            with open(os.path.join('.', 'game/saves/', user + '.json'), 'r') as save_file:
                saved_game = json.load(save_file)
                # print("Saved char name:" + saved_game['char_attrs']['name'])
                char, inv = create_character(saved_game)
                char["lives"] = saved_game['lives']
                main_game_loop(char, user, saved_game['difficulty'], inv, saved_game['level'], scene=1)


def list_save_files():
    # print(os.listdir())
    all_files = os.listdir('./game/saves')
    save_files = []
    users = []
    for f in all_files:
        user = re.search(r"^(.+)\.json$", f)
        if user is not None:
            user = user.group(1)
            users.append(user)
            save_files.append(f)
    return users, save_files


def main_game_loop(char, user_name, diff_str, inv, level, scene):

    my_path = os.path.join('.', 'story', 'story.json')

    with open(my_path) as story_file:
        story = json.load(story_file)

    while True:

        print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")

        print_red_on_cyan(story['story'][f'lvl{level}']['title'] + "\n")

        print(story['story'][f'lvl{level}']['scenes'][f'scene{scene}'] + "\n")

        user_input = prompt_user_input(story, level, scene)

        outcome_text, outcome_effects = \
            process_user_input(user_input, char, inv, story, level, scene)

        if outcome_text is not None:

            outcome_text = re.sub("{tool}", char["tool"], outcome_text)

            outcome_text = re.sub("{weapon}", char["weapon"], outcome_text)

            print_red_on_cyan(outcome_text)

        if outcome_effects is not None:

            for effect in outcome_effects:

                item_to_add = re.search(r"inventory\+'(.+)'", effect)
                if item_to_add is not None:
                    item_to_add = item_to_add.group(1).capitalize()
                    inv = add_to_inventory(inv, item_to_add)

                item_to_remove = re.search(r"inventory-'(.+)'", effect)
                if item_to_remove is not None:
                    item_to_remove = item_to_remove.group(1).capitalize()
                    inv = remove_from_inventory(inv, item_to_remove)

                if effect == 'repeat':
                    pass

                lives_to_add = re.search(r"life\+(.+)", effect)
                if lives_to_add is not None:
                    lives_to_add = lives_to_add.group(1)
                    char["lives"] += int(lives_to_add)
                    print_red_on_cyan("You gained an extra life! Lives remaining: %s\n" % char["lives"])

                lives_to_sub = re.search(r"life-(.+)", effect)
                if lives_to_sub is not None:
                    lives_to_sub = lives_to_sub.group(1)
                    char["lives"] -= int(lives_to_sub)
                    print_red_on_cyan("You died! Lives remaining: %s\n" % char["lives"])
                    if char["lives"] == 0:
                        print_red_on_cyan("You've run out of lives! Game over!")
                        return

                if effect == 'save':
                    save_game(user_name, char, diff_str, level)

                if effect == 'move':
                    scene += 1

                    if scene > 3:
                        level += 1
                        scene = 1

        if level == 2 and scene == 3:  # Move from Level 2, scene 2 --> End of game
            break

    if level == 2 and scene == 3:
        print_red_on_cyan("Congratulations! You beat the game!")
        sys.exit()


def top_menu():

    while True:
        top_menu_choice = process_top_menu_input(get_top_menu_input())

        if top_menu_choice == -1:
            alert_unknown_input()
        elif top_menu_choice == 3:
            # prompt_to_quit_game()
            print("Goodbye!")
            sys.exit()
        elif top_menu_choice == 2:
            load_saved_game()
        elif top_menu_choice == 1:
            start_new_game()


top_menu()
