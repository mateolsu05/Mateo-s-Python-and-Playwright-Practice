'''
Hello, to demonstrate my understanding of this week's topics, I asked ChatGPT to
give me a mini project to test my understanding of the following topics.:
Strings, Variables, Input, Output, Type Conversions, and Arithmetic Operations.


ChatGPT Challenge:
My Challenge for You
I'd actually combine a couple of these ideas into a Character Sheet Generator. It gives you a chance to practice every concept you've learned without introducing anything new.
Here's a possible spec:
User inputs:
Character name
Race
Class
Weapon
Age
Strength
Dexterity
Intelligence
Calculations:
Power = Strength × 2
Magic = Intelligence × 3
Speed = Dexterity × 2
Overall Rating = Power + Magic + Speed
Output:
Print a polished character sheet with all the information.
✨ Bonus (without new concepts)
Experiment with string formatting to make the output look nice. For example:
=============================
      CHARACTER SHEET
=============================

Name:        Aria
Race:        Elf
Class:       Mage
Weapon:      Oak Staff

Power:       18
Magic:       36
Speed:       20

Overall:     74
=============================
'''

CharacterName = input("What is your Character's Name? ")
CharacterRace = input("What is your Character's Race? ")
CharacterClass = input("What is your Character's Class? ")
CharacterWeapon = input("What is your Character's Weapon? ")

CharacterAge = int(input("How old is your Character? "))
CharacterStrength = int(input("What is your Character's Strength? "))
CharacterDexterity = int(input("What is your Character's Dexterity? "))
CharacterIntelligence = int(input("What is your Character's Intelligence? "))

Power = CharacterStrength * 2
Magic = CharacterIntelligence * 3
Speed = CharacterDexterity * 2
OverallRating = Power + Magic + Speed

print("=============================")
print("      CHARACTER SHEET")
print("=============================")
print(f"Name: {CharacterName}")
print(f"Race: {CharacterRace}")
print(f"Class: {CharacterClass}")
print(f"Weapon: {CharacterWeapon}")
print(f"CharacterAge: {CharacterAge}")
print(" ")
print(f"Power: {Power}")
print(f"Magic: {Magic}")
print(f"Speed: {Speed}")
print(" ")
print(f"Overall Rating: {OverallRating}")

