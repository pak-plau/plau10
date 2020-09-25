import random

KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDIE', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}

def printRandomName():
    team = random.choice(tuple(KREWES.keys()))
    print("\n" + random.choice(KREWES[team]) + " of team " + team + "\n")

def printRandomNameOfChosenTeam():
    team = input("Please type in the name of the team you want to randomly select a person from.(orpheus, rex, or endymion)\n").lower()
    isTeamName = False
    while not isTeamName:
        if(team != "orpheus" and team != "rex" and team != "endymion"):
            team = input("Error, not a team name, please input a valid team name\n").lower()
        else:
            isTeamName = True
    print("\n" + random.choice(KREWES[team]) + " of team " + team + "\n")

def main():
    isAnswerPossible = False
    answer = None
    while not isAnswerPossible:
        answer = input("What would you like to do? (Input the number of your choice)\n0. Receive a random name from KREWES\n1. Choose a team to receive a random name from\n2. Exit\n")
        if(answer != "0" and answer != "1" and answer != "2"):
            print("Error, not a valid choice")
        elif(answer == "0"):
            printRandomName()
        elif(answer == "1"):
            printRandomNameOfChosenTeam()
        else:
            break


main()
