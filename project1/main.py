#!/usr/bin/env python3

import sys
import crypt
import itertools
from multiprocessing import Pool, cpu_count
import time

# from passlib.hash import md5_crypt
teamName = input("Enter a team number: ")
file = sys.argv[1]
input = open(file)

# print(teamName)

for line in input: #getting the team number that you want (team 11)
    # print(line)
    teamNum = line.split(':')[0]
    #print(teamNum)
    if teamNum == teamName:
        print(line)
        total = line
        
total = total.replace(teamName, "")
total = total.replace(":", "", 1)
print(total)

#SXA89G4E
salt = total.split('$', 4)[:3]
salt = '$'.join(salt)
salt += '$'
print("Salt:", salt) 


#pZ1EOTFJ14m7TihlI8SrW.
total = total[11:60]
passHash = total.split(":")[0]
passHash = passHash[1:] 
print("passHash", passHash)

chars = 'abcdefghijklmnopqrstuvwxyz'
    
def cracking(password):
    print(f'Starting Cracking on: {password}*****')
    for password in itertools.product(chars, repeat=5):
        pwd = ''.join(password)
        if(crypt.crypt(pwd, salt)) == passHash:
            print('\nPASSWORD CRACKED! ~ SUCCESS! :', pwd)
            return pwd
    
print("\nCracking Password...")

start = time.time()

alpha = 'abcdefghijklmnopqrstuvwxyz'
pool = Pool(cpu_count())
with Pool(processes=26) as pool:
    password = pool.map(cracking, alpha)

    for p in password:
        if p:
            print("Password for", teamName, ":", p)
            end = time.time()
            print(f"Elapsed time: {end - start} seconds\n")
 
        
  

    
    

    
    



