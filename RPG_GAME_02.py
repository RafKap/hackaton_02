"""
Historyjka a'la RPG:

    Konieczność użycia modułu random.
    Program wypisuje kolejne "przygody" bohatera.

    Przygody są zdefiniowanymi zdaniami, które będą losowo wypełniane odpowiednimi wyrazami,
    np: "(bohater) poszedł do (miejsce) aby (czasownik)."
    może stać się "Jouxdrien II Niemrawy poszedł do tawerny aby zasnąć."

    Historyjka ma mieć zadaną długość i ma być możliwie losowa.

"""

import random



#


def fight(hero_attack, hero_defense, hero_hp, enemy_attack, enemy_defense, enemy_hp):
    if hero_attack - enemy_defense == 0:
        hero_damage = 1
    else:
        hero_damage = hero_attack - enemy_defense

    if enemy_attack - hero_defense == 0:
        enemy_damage = 1
    else:
        enemy_damage = enemy_attack - hero_defense
    hit_to_kill_enemy = enemy_hp / hero_damage
    if hit_to_kill_enemy < 0:
        return False
    else:
        hit_to_kill_hero = hero_hp / enemy_damage
        if hit_to_kill_hero < hit_to_kill_enemy:
            return True
        else:
            return False


def cave(your_attack, your_defense, your_hp):
    print('You came to Cave\n'
          'You spotted Werewolf. You want to run or fight?')
    while True:
        response = input("Put R as Run, or F as Fight ").lower()
        if response == "r":
            print("You ran out of fight")
            break
        else:
            possible_locations.remove(cave)
            print("You fight with Werewolf")
            werewolf_atack = 2
            werewolf_defense = 0
            werewolf_hp = 50
            if fight(your_attack, your_defense, your_hp, werewolf_atack, werewolf_defense, werewolf_hp):
                print(f'You won'
                      f'\nWerewolf dropped Medium shield.')
                print(
                    f'Do you want to add Medium shield to Your inventory? '
                    f'{possible_defense_item.get("medium_shield")[0]} '
                    f'got {possible_defense_item.get("medium_shield")[1]} defence stat.')
                answer = input("Y as Yes, N as No ").lower()
                if answer == "y":
                    equipment.pop("defense")
                    equipment["defense"] = "medium_shield"
                    equipment_wear()
                else:
                    break
            else:
                print(f'You lose fight. You died.'
                      f'\n End of the game')
                exit()
            break


def forest(your_attack, your_defense, your_hp):
    print('You came to Forest\n'
          'You spotted Small pixie. You want to run or greet Small pixie?')
    while True:
        response = input("Put R as Run, or G as Greet ").lower()
        if response == "r":
            print("You ran out of fight ")
            break
        else:
            possible_locations.remove(forest)
            print("You greet Small Pixie")
            print('Pixie gave You Big shield')
            print(
                f'Do you want to add Big shield to Your inventory? {possible_defense_item.get("big_shield")[0]} '
                f'got {possible_defense_item.get("big_shield")[1]} defence stat.')
            answer = input("Y as Yes, N as No ").lower()
            if answer == "y":
                equipment.pop("defense")
                equipment["defense"] = "big_shield"
                equipment_wear()
                break
            else:
                break


def tavern(your_attack, your_defense, your_hp):
    print('You rest in Tavern.'
          '\nYour Max HP increased by 50.')
    equipment.pop("health_point")
    equipment["health_point"] = your_hp + 50
    possible_locations.remove(tavern)


def city_01(your_attack, your_defense, your_hp):
    print('You spotted Armored Dwarf in City. You want to run or fight?')
    while True:
        response = input("Put R as Run, or F as Fight ").lower()
        if response == "r":
            print("You ran out of fight")
            break
        else:
            possible_locations.remove(city_01)
            print("You fight with Armored Dwarf")
            enemy_attack = 10
            enemy_defense = 15
            enemy_hp = 100
            if fight(your_attack, your_defense, your_hp, enemy_attack, enemy_defense, enemy_hp):
                print(f'You won, You killed boss!')
            else:
                print(f'You lose fight. You died.'
                      f'\n End of the game.')
                exit()
            break


def equipment_wear():
    print(f'Your attack item: {possible_attack_item.get(equipment.get("damage"))[0]} got '
          f'{possible_attack_item.get(equipment.get("damage"))[1]} attack')

    print(f'Your defense item: {possible_defense_item.get(equipment.get("defense"))[0]} got '
          f'{possible_defense_item.get(equipment.get("defense"))[1]} defense')

    print(f'Your health point is {equipment.get("health_point")}')


def pyramid(your_attack, your_defense, your_hp):
    print('You came to Pyramid\n'
          'You spotted Mummy. You want to run or fight?')
    while True:
        response = input("Put R as Run, or F as Fight ").lower()
        if response == "r":
            print("You ran out of fight")
            break
        else:
            possible_locations.remove(pyramid)
            print("You fight with Mumy")
            enemy_attack = 10
            enemy_defense = 10
            enemy_hp = 75
            if fight(your_attack, your_defense, your_hp, enemy_attack, enemy_defense, enemy_hp):
                print(f'You won'
                      f'\nMummy dropped Big sword.')
                print(
                    f'Do you want to add Big sword to Your inventory? '
                    f'{possible_attack_item.get("big_sword")[0]} '
                    f'got {possible_attack_item.get("big_sword")[1]} attack stat.')
                answer = input("Y as Yes, N as No ").lower()
                if answer == "y":
                    equipment.pop("damage")
                    equipment["damage"] = "big_sword"
                    equipment_wear()
                else:
                    break
            else:
                print(f'You lose fight. You died.'
                      f'\n End of the game :(.')
                exit()
            break


#########################################################################################################
##dictionaries:
max_hp = 100
possible_attack_item = {
    "small_sword": ("Small sword", 10),
    "medium_sword": ("Medium sword", 20),
    "big_sword": ("Big sword", 30),
}

possible_defense_item = {
    "small_shield": ("Small shield", 5),
    "medium_shield": ("Medium shield", 10),
    "big_shield": ("Big shield", 15),
}

equipment = {
    "damage": "small_sword",
    "defense": "small_shield",
    "health_point": max_hp
}

## Hero
hero_name = input("Put name of Your hero: ")
# #print(hero_name)
wygrana = "start"


## Set current def and att
attack_current = possible_attack_item.get(equipment.get("damage"))[1]
defense_current = possible_defense_item.get(equipment.get("defense"))[1]
max_hp = equipment["health_point"]

print(f'Hero {hero_name} starts hes journey with:\n'
          f'{possible_attack_item.get(equipment.get("damage"))[0]} that got  '
          f'{possible_attack_item.get(equipment.get("damage"))[1]} attack\n'
          f'{possible_defense_item.get(equipment.get("defense"))[0]} that got '
          f'{possible_defense_item.get(equipment.get("defense"))[1]} defense\n'
          f'and {equipment["health_point"]} health point\n')

possible_locations = [forest, cave, tavern, city_01, pyramid]
print("Journey begin right now", "\n")
while True:
    if wygrana == "start":
        if len(possible_locations) == 0:
            print("You won game, congratulations!")
            break
        elif len(possible_locations) > 0:
            attack_current = possible_attack_item.get(equipment.get("damage"))[1]
            defense_current = possible_defense_item.get(equipment.get("defense"))[1]
            max_hp = equipment["health_point"]
            choice_random = random.choice(possible_locations)(attack_current, defense_current, max_hp)
    else:
        print('You are dead. End of the game')


