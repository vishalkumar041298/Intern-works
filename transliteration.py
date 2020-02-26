"""transliterating the words in devanagiri(hindi) to english from sqlite3 db
   table and adding columns to the table which transliterated those words in english 
            using pandas and indic-transliteratio library"""  
import pandas as pd
import sqlite3
conn = sqlite3.connect("sro_vill_map.sqlite3")
df = pd.read_sql_query("select * from alphabet_index;", conn)
from indic_transliteration.sanscript import transliterate
from indic_transliteration import sanscript
def district(row):
    s=row['district_name']
    eng=transliterate(s, sanscript.DEVANAGARI, sanscript.HK)
    return eng
def sro(row):
    s=row['sro_name']
    eng=transliterate(s, sanscript.DEVANAGARI, sanscript.HK)
    return eng
def village(row):
    s=row['village_name']
    eng=transliterate(s, sanscript.DEVANAGARI, sanscript.HK)
    return eng        
df['district'] = df.apply (lambda row: district(row),axis=1)
df['sro'] = df.apply (lambda row: sro(row),axis=1)
df['village'] = df.apply (lambda row: village(row),axis=1)
print(df)
from sqlalchemy import create_engine
e = create_engine('sqlite:////home/mrinal/Desktop/newwwww/newwww/sro_vill_map.sqlite3')  # pass your db url

df.to_sql(name='tanslated', con=conn,index=False)
