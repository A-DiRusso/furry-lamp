from Zombie_Attack import Character
from Zombie_Attack import Hero
from Zombie_Attack import Goblin




test = Character("test")
test_Hero = Hero("Hero", 10, 5)
test_Goblin = Goblin("Goblin", 6, 2)

print(test.name)
print(test_Hero.name)
print("The hero has %d, health." % (test_Hero.health))
print("The hero does %d damage in attack." % (test_Hero.power))
print(test_Goblin.name)
print("The goblin has %d, health." % (test_Goblin.health))
print("The goblin does %d damage, in attack." % (test_Goblin.power))

print(test_Hero.attack())
print(test_Goblin.attack())