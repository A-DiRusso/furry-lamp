# my hand copied start to the RPG game.

# def main():
# hero_health = 10
# hero_power = 5
# goblin_health = 6
# goblin_power = 2
user_input = input("? ")

class Character():
    def __init__(self, new_name):
        self.name = new_name
        pass
# while Goblin.alive() and Hero.alive():

class Hero(Character):
    def __init__(self, new_name, hero_health, hero_power):
        # super() figure this shit out later??????
        self.name = new_name
        self.health = hero_health
        self.power = hero_power

    def attack(self, goblin_health, hero_power):
        if user_input == "1":
            print("Goblin Health")
        return goblin_health - hero_power
        # return "Hero has delt %d damage. \nGoblin has %d health." % (hero_power, goblin_health - hero_power)


class Goblin(Character):
    def __init__(self, new_name, goblin_health, goblin_power):
        self.name = new_name
        self.health = goblin_health
        self.power = goblin_power

    def attack(self, hero_health, goblin_power):
        print("Hero Health")
        return hero_health - goblin_power
        # return "Goblin has delt %d damage.\nThe hero has %d life." % (goblin_power, hero_health - goblin_power)
        
        


#     while goblin_health > 0 and hero_health > 0:
#         print("You have %d health and %d power." % (hero_health, hero_power))
#         print("The goblin has %d health and %d power." % (goblin_health, goblin_power))
#         print()
#         print("What do you want to do?")
#         print("1. fight goblin")
#         print("2. do nothing")
#         print("3. flee")
#         print("> ")
#         user_input = input()
#         if user_input == "1": #Hero attacks goblin
#             goblin_health -= hero_power
#             print("You do %d damage to the goblin." % hero_power)
#             if goblin_health <= 0:
#                 print("The goblin is dead.")
#         elif user_input == "2":
#             pass
#         elif user_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input %r" % user_input)

#         if goblin_health > 0: #Goblin attacks hero
#             hero_health -= goblin_power
#             print("The goblin does %d damage to you." % goblin_power)
#             if hero_health <= 0:
#                 print("You are dead.")


# main()