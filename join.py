from srtt import TRADDIR,LF,PATH,FINAL_PATH
from subs import getsubs,getsub
import os

def search(key,value,d: list[dict]) -> list[dict]:
    r = []
    for i,e in enumerate(d):
        if e[key] == value:
            r.append((i,e))
    return r

def displaysub(sub: dict):
    print(sub["n"].decode(),sub["timing"].decode(),sep="\n")
    for l in sub["sub"]: print(l.decode())

subs = []
for file in os.listdir(TRADDIR):
    p = os.path.join(TRADDIR,file)
    subs += getsubs(p,LF)
subs.sort(key=lambda k: int(k["n"]))

subids: list[int] = []
conflicts: list[int] = []
for k in subs:
    k_n = int(k["n"])
    if k_n not in subids:
        subids.append(k_n)
    else:
        conflicts.append(k_n)

    # print(k["n"],k["timing"],len(k["sub"]))

delIds = []
print(f"WARNING: Found {len(conflicts)} conflicts.\n")
# for i in conflicts:
#     conflict = search("n",str(i).encode(),subs)
#     # if len(conflict) != 2: continue # conflict with more that 2 element are not available
#     aId,conflictA = conflict[0]
#     bId,conflictB = conflict[1]

#     if conflictA["sub"] == conflictB["sub"]:
#         delIds.append(bId) # The 2 are the same, so choose the A one it doesn't matter
#         continue

#     print("====================")
#     print("ORIGINAL:")
#     ogsub = getsub(i,PATH,LF)
#     displaysub(ogsub)
#     print("--------------------")
#     print("CHOICE A:")
#     displaysub(conflictA)
#     print("--------------------")
#     print("CHOICE B:")
#     displaysub(conflictB)
#     print()
#     print("Wich one to keep ? (A/B)")
#     resp = input(" >> ").upper()
    
#     if resp=="A":
#         delIds.append(bId)
#     elif resp=="B":
#         delIds.append(aId)

delIds = [
    36,
    38,
    39,
    41,
    80,
    82,
    83,
    86,
    123,
    126,
    127,
    130,
    168,
    170,
    172,
    174,
    212,
    214,
    216,
    218,
    256,
    258,
    260,
    262,
    300,
    302,
    304,
    306,
    344,
    345,
    348,
    349,
    388,
    390,
    392,
    394,
    432,
    434,
    436,
    438,
    475,
    478,
    480,
    482,
    519,
    522,
    524,
    526,
    563,
    566,
    567,
    570,
    607,
    610,
    612,
    614,
    652,
    654,
    656,
    658,
    696,
    697,
    699,
    702,
    740,
    742,
    744,
    783,
    785,
    787,
    788
]
print(delIds,len(delIds))

subs_wo_conflicts: list[dict] = []
for i,sub in enumerate(subs):
    if i in delIds:
        continue # deletes it
    subs_wo_conflicts.append(sub)

print(f"Writing '{FINAL_PATH}'...")
with open(file=FINAL_PATH,mode="wb") as fstream:
    for sub in subs_wo_conflicts:
        fstream.write(sub["n"]+LF)
        fstream.write(sub["timing"]+LF)
        for subline in sub["sub"]:
            fstream.write(subline+LF)
        fstream.write(LF)

print("done!")
