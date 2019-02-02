import pyttsx3
import random

boardSize = 5
speech = pyttsx3.init()


def generateName():
    letters = "etaoinabcdefghijklmnopqrstuvwxyz"
    vowels = "aeiouetaoin"
    name = ""
    for _ in range(random.randint(1, 4)):
        name += random.choice(letters)
        name += random.choice(vowels)
    if bool(random.randint(0, 1)):
        name += random.choice(letters)
    return name


def pickRandom(choice1, choice2, choice2Chance):
    if not bool(random.randint(0, choice2Chance)):
        return choice2()
    return choice1()


class scenery:
    names = [generateName() for _ in range(3)]
    types = [generateName() for _ in range(3)]

    sceneries = []

    def __init__(self):
        self.genNameAndType()
        while self.searchByNameAndType(self.name, self.type):
            self.genNameAndType()

        scenery.sceneries.append(self)

    def searchByNameAndType(self, name, type):
        for scene in scenery.sceneries:
            if scene.name == name and scene.type == type:
                return True
        return False

    def say(self):
        statement = f"{self.type}, {self.name}."
        print(statement)
        speech.say(statement)
        speech.runAndWait()

    def genNameAndType(self):
        newWordChance = 5

        if not bool(random.randint(0, newWordChance)):
            self.name = generateName()
            scenery.names.append(self.name)
        else:
            self.name = random.choice(scenery.names)

        if not bool(random.randint(0, newWordChance)):
            self.type = generateName()
            scenery.types.append(self.type)
        else:
            self.type = random.choice(scenery.types)


class mineClass:
    def __init__(self):
        self.name = generateName()

    def say(self):
        statement = "It is a mine."
        print(statement)
        speech.say(statement)
        speech.runAndWait()


class playerClass:
    startCoordinate = int(boardSize / 2)

    def __init__(self):
        self.inventory = []
        self.x = playerClass.startCoordinate
        self.y = playerClass.startCoordinate
        self.z = playerClass.startCoordinate
        board[playerClass.startCoordinate][playerClass.startCoordinate][playerClass.startCoordinate] = self

    def describeSurroundings(self):
        adjacents = [-1, 1]
        for x in adjacents:
            print(self.x + x, self.y, self.z)
            board[self.x + x][self.y][self.z].say()
        for y in adjacents:
            print(self.x, self.y + y, self.z)
            board[self.x][self.y + y][self.z].say()
        for z in adjacents:
            print(self.x, self.y, self.z + z)
            board[self.x][self.y][self.z + z].say()


board = [[[pickRandom(scenery, mineClass, 3) for _ in range(boardSize)] for _ in range(boardSize)] for _ in
         range(boardSize)]
player = playerClass()

player.describeSurroundings()

while 1:
    action = input("direction?")
    if action == "u":
        board[player.x][player.y][player.z] = mineClass()
        board[player.x][player.y + 1][player.z] = player
        player.y += 1
