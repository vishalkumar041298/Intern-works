"""office task at advarisk to convert the csv given and with the two columns name matches or approzimate matches get the name its estid and cin so i converted the csv to dictionaries and used fuzzywuzzy to check teh matches""" 
import csv
from fuzzywuzzy import fuzz
import pandas as pd

with open('ltdmatch.csv', mode='r') as infile:
    reader = csv.reader(infile)
   
    masterdata = {rows[1]:rows[2] for rows in reader }
with open('ltdmatch.csv', mode='r') as infile:
    reader = csv.reader(infile)
   
    estdata = {rows[0]:rows[3] for rows in reader } 
print(len(estdata))     
masterllp=dict()
masterltd=dict()
for key,val in masterdata.items():
    
    if (" LLP" in val or "LIMITED LIABILITY PARTNERSHIP" in val or "LIABILITY" in val):
        masterllp.update({key:val})
    else:
        masterltd.update({key:val})
estllp=dict()
estltd=dict()
for key,val in estdata.items():
    if ("LLP" in val or "LIMITED LIABILITY PARTNERSHIP" in val or "LIABILITY" in val):
        estllp.update({key:val})
    else:
        estltd.update({key:val})
def nametrim(str,llp=False):
    a=[" LIMITED"," LLP"] if llp else ["PRIVATE","P LTD"," PVT","(P","[P"," P LIMITED"," LIMITED","LTD"]
    
    for i in a:
        if i in str:
            n = str.split(i)
            name,value=n[0],n[1]
            
            break
        else:
            name=str
            continue
    return name.strip() 

cin=[]
estid=[]
masternamee=[]
estnamee=[]
i=0
for key1,val1 in estltd.items():
    print(i)
    i=i+1
    for key2,val2 in masterltd.items():
        if fuzz.ratio(nametrim(val1),nametrim(val2))>=93:
            print(val1)
            print(val2)

            cin.append(key2)
            estid.append(key1)
            masternamee.append(val2)
            estnamee.append(val1) 

df = pd.DataFrame(list(zip(estid,cin,masternamee,estnamee)), columns =['estid', 'cin','matername','estname']) 
df.to_csv("ltdmatch100.csv",index=False)                                    
