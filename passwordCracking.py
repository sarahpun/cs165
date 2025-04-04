#!/usr/bin/env python3
import sys

def locateTeamCrack(name, bank):
    for x in bank:
        if x[0] == name:
            return x[1]


fileName = sys.argv[1]
inputShadow = open(fileName)

passBank = []
for line in inputShadow:
    line = line.strip()
    if(line):
        passBank.append(line.split(":"))
    
# for x in passBank:
#     print(x)

desiredCrack = input("Enter team user you want to Crack: ")

mashLocated = locateTeamCrack(desiredCrack, passBank)

print(mashLocated)

mashLocated = mashLocated.split("$")

print(mashLocated)

hashValue = mashLocated[1]
saltValue = mashLocated[2]
passValue = mashLocated[3]

print("Hash Value:", hashValue)
print("Salt Value:", saltValue)
print("Pass Value:", passValue)

# 'team11', '$1$SXA89G4E$pZ1EOTFJ14m7TihlI8SrW.', '16653', '0', '99999', '7'