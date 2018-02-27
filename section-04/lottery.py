import random


def menu():
    player_numbers = get_player_numbers()
    lottery_numbers = create_lottery_numbers()
    matched_numbers = player_numbers.intersection(lottery_numbers)
    print("You matched {}, You won ${}".format(len(matched_numbers), 100 ** len(matched_numbers)))

def get_player_numbers():
    number_csv = input("Enter your 6 numbers, seperated by commas: ")
    number_list = number_csv.split(",")
    number_set = {int(number) for number in number_list}
    return number_set

def create_lottery_numbers():
    lottery_numbers = set()
    while len(lottery_numbers)<6:
        lottery_numbers.add(random.randint(1,20))
    return lottery_numbers

menu()

