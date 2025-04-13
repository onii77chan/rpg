from hero import Freid, Aurora
from mob import Goblin, Slime
from boss import TheBoss

# heroe's
Freid = Freid()
Aurora = Aurora()

# bosse's
Gatot = TheBoss()

# mob's
Goblin = Goblin()
Slime = Slime()

# npc's
enemies_list = [Gatot, Goblin, Slime]

print(Freid.__str__(), Gatot.__str__())
Freid.attack(Gatot, enemies_list)
Freid.attack(Gatot, enemies_list)
Freid.attack(Gatot, enemies_list)
print(Freid.__str__(), Gatot.__str__())
