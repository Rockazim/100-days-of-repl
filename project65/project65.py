"""Day 65 Challenge
Today is a project day! You're going to use what you've learned about OOP (on Day 64) to store characters for my video game.

My game needs to have a character with a name, health and magic points.
It needs these values setup when it is initialized.
It needs a method to output this data.
There should be a sub-class 'player' which inherits from character and also has a number of lives.
Player should also have an 'am I alive?' method which checks the player status and reports back yes or no.
There should also be an 'enemy' sub-class with additional 'type' and 'strength'.
'enemy' should have two sub-classes:
'orc' with a 'speed' attribute.
'vampire' with a 'day/night' tracker
Instantiate one player, two vampires and three orcs. You choose their names.
Print out their values."""


class character:
    name = None
    health = None
    magic_points = None
    def __init__(self, name, health, magic_points):
        self.name = name
        self.health = health
        self.magic_points = magic_points

    def print(self):
        print(f"{self.name}\nHealth: {self.health}\nMagic Points: {self.magic_points}")

class player(character):

    nickname = None
    lives = None
    health = None
    magic_points = None

    def __init__(self, nickname, health, magic_points, lives):
        self.name = "Player"
        self.nickname = nickname
        self.health = health
        self.magic_points = magic_points
        self.lives = lives

    def alive(self):
        if self.lives > 0:
            return True
        else:
            return False

    def print(self):
        print(f"{self.name}\nName: {self.nickname}\nHealth: {self.health}\nMagic Points: {self.magic_points}\nLives: {self.lives}")
        if player.alive(self) == True:
            print("Alive?: True")
        else:
            print("Alive?: False")

class enemy(character):

    name = None
    type = None
    strength = None
    health = None
    magic_points = None

    def __init__(self, name, type, strength, health, magic_points):
        self.name = name
        self.type = type
        self.type = strength
        self.health = health
        self.magic_points = magic_points

class orc(enemy):

    name = None
    strength = None
    health = None
    magic_points = None
    speed = None

    def __init__(self, name, strength, health, magic_points, speed):
        self.name = name
        self.type = "Orc"
        self.strength = strength
        self.health = health
        self.magic_points = magic_points
        self.speed = speed
    
    def print(self):
        print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magic_points}\nType: {self.type}\nStrength: {self.strength}\nSpeed: {self.speed}")


class vampire(enemy):

    name = None
    type = None
    strength = None
    health = None
    magic_points = None
    day = None

    def __init__(self, name, strength, health, magic_points, day):
        self.name = name
        self.type = "Vampire"
        self.strength = strength
        self.health = health
        self.magic_points = magic_points
        self.day = day
    
    def print(self):
        print(f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magic_points}\nType: {self.type}\nStrength: {self.strength}\nDay/Night?: {self.day}")



my_boy = player("John", 69, 100, 3)
my_boy.print()
print()
vampire1 = vampire("Timothy", 10, 69, 2, True)
vampire1.print()
print()
vampire2 = vampire("Jimmy", 1, 9, 5, False)
vampire2.print()
print()
orc1 = orc("Zim", 10, 69, 2, 1000)
orc1.print()
print()
orc2 = orc("zimbo", 100, 6, 23, -3)
orc2.print()
print()
orc3 = orc("jimbo", 1, 9, 14, 21)
orc3.print()
