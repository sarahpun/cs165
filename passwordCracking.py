#!/usr/bin/env python3
import platform
import sys
import crypt
from multiprocessing import Pool, cpu_count
import itertools
import time

def locateTeamCrack(name, bank):
    for x in bank:
        if x[0] == name:
            return x[1]

# def generatePasswords():
#     alpha = 'abcdefghijklmnopqrstuvwxyz'
#     passes = itertools.product(alpha, repeat=6)
    
#     passList = []
#     for p in passes:
#         passList.append(''.join(p))
#     return passList

#---------------------------------
fileName = sys.argv[1]
inputShadow = open(fileName)

passBank = []
for line in inputShadow:
    line = line.strip()
    if(line):
        passBank.append(line.split(":"))
#---------------------------------
        
# for x in passBank:
#     print(x)

#---------------------------------
desiredCrack = input("Enter team user you want to Crack: ")
mashLocated = locateTeamCrack(desiredCrack, passBank)

# print(mashLocated)
passValue = mashLocated
mashLocated = mashLocated.split("$")
# print(passValue)

saltValue = '$' + mashLocated[1] + '$' + mashLocated[2] + '$'
# passValue = mashLocated[3]
# print("Hash Value:", hashValue)
# print("Salt Value:", saltValue)
# print("Pass Value:", passValue)
#---------------------------------

#---------------------------------
# print("\nGenerating Passwords...")
# start = time.time()
# all_Passwords = generatePasswords()
# end = time.time()
# print(f"Elapsed time: {end - start} seconds\n")
#---------------------------------

# print(len(all_Passwords)) Size : 308915776

#---------------------------------
def crackTheCode(passLetter):
    start = time.time()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    combination = itertools.product(alpha, repeat=5)
    print(f'Starting Cracking on: {passLetter}*****')
    passChecks = 0
    for c in combination:
        passes = passLetter + ''.join(c)
        passChecks += 1
        if crypt.crypt(passes, saltValue) == passValue:
            print('\nPASSWORD CRACKED! ~ SUCCESS! :', passes)
            
            num_processes = cpu_count()
            print(f"\nNumber of Processes/Threads: {num_processes}")

            cpu_model = platform.processor()
            print(f"CPU Model: {cpu_model}")

            # print("\nSource Code:")
            # with open(__file__, 'r') as f:
            #     print(f.read())
            
            print(f"Number of Checks: {passChecks}")
            
            end = time.time()
            seconds = end - start
            throughput = passChecks / float(seconds)
            
            print(f"Throughput: {throughput}")
            
            print(f"\nTime to Crack: {seconds} seconds\n")
            
            
            
            return passes
    # print('FAILED CRACK!')
    return None
#---------------------------------

#---------------------------------
print("\nCracking Password...")

alpha = 'abcdefghijklmnopqrstuvwxyz'
pool = Pool(cpu_count())
with Pool(processes=26) as pool:
    password = pool.map(crackTheCode, alpha)

    # for p in password:
    #     if p:
    #         print("Password for", desiredCrack, ":", p)
#---------------------------------

#'team11', '$1$SXA89G4E$pZ1EOTFJ14m7TihlI8SrW.', '16653', '0', '99999', '7'       
# Team 11 Password : dcacgx  
