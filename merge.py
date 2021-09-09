from numpy import add
import pandas as pd
import sys

path_stake = sys.argv[1]
path_dfy = sys.argv[2]



stake_data = pd.read_csv(path_stake, header=None)
dfy_data = pd.read_csv(path_dfy, header=None)
f = open("airdrop.sh", "w")

list_addr = stake_data.loc[:,0]
n = 0
added_addr_map = {} 
for i,r in stake_data.iterrows():
    addr = r[0]

    ammount = 1.5 * int(r[1])/10e12 + int(r[2])/10e12
    ammount = str(int(ammount))
    cmd = "digd add-genesis_account " + addr + " " + ammount + "udig\n"    
    added_addr_map[addr.lower()] = int(r[2])/10e12
    f.writelines(cmd)


# I use iterrows there's no need for speed
for i,r in dfy_data.iterrows():
    addr = r[0]
    ammount = int(r[1])/10e12

    if added_addr_map.get(addr) != None:
        if added_addr_map[addr] != ammount:
            print(addr, ammount, added_addr_map[addr])
    else :
        ammount = str(ammount)
        cmd = "digd add-genesis_account " + addr + " " + ammount + "udig\n"    
        f.writelines(cmd)

f.close()
     
