import random


# TODO 1: Create the list of the Santas.
def input_name(msg):
    """Type a name for the Santas' list."""
    return input(msg).lower()


def decision_stop(group, entry):
    """If the user's input is 'stop', it checks if the number of members within the list is less than 3."""
    return entry == "stop" and len(group) < 3


def list_closed(name, participants_number):
    """Returns true if the user types stop and the number of the participants is equal or more than 3"""
    return name == "stop" and participants_number >= 3


def list_of_players():
    """Creates the list of people."""
    team = []
    name = input_name("Type a name or 'stop' if you completed the list: ")
    while not list_closed(name, len(team)):
        if name != "stop":
            team.append(name.title())
        if decision_stop(team, name):
            team.append(input_name("There should be at least 3 participants in the game. Add more: ").title())
        name = input_name("Type a name or 'stop' if you completed the list: ")

    print(team)
    return team


# TODO 2: Create pairs of 2 people (as sub-lists in the main list)
def create_pairs_of_2_players():
    """Creates sub-lists of 2 players, randomly chosen."""
    pair_sublist = []
    list_of_pairs = []
    players_list = list_of_players()
    shuffled_list = random.sample(players_list, len(players_list))

    for i in range(len(shuffled_list)):
        pair_sublist.append(shuffled_list[i - 1])
        pair_sublist.append(shuffled_list[i])
        list_of_pairs.append(pair_sublist)
        pair_sublist = []

    print(list_of_pairs)
    return list_of_pairs


# TODO 3: Print a message for each pair of players
def print_results():
    """Prints the results."""
    pairs_list = create_pairs_of_2_players()
    for i in range(len(pairs_list)):
        print(f"{pairs_list[i][0]} is Santa for {pairs_list[i][1]}")


print_results()
