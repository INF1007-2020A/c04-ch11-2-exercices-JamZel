"""
Chapitre 11.3
"""


import math
from inspect import *

from game import *


def simulate_battle():
	c1 = Character("Hermione", 500, 150, 70, 70)
	c2 = Character("Ron", 550, 100, 120, 60)
	c3 = Magician("Voldemort", 800, 100, 50, 150, 50, 65)

	c1.weapon = Weapon("Axe", 100, 69)
	c2.weapon = Weapon("Nivea", 120, 1)
	c3.spell = Spell("AVADA KEDAVRA", 100, 35, 50)
	c3.weapon = Weapon("Dagger", 80, 20)
	c3.using_magic = True

	turns = run_battle(c3, c1)
	print(f"The battle ended in {turns} turns.")


def main():
	simulate_battle()

if __name__ == "__main__":
	main()

