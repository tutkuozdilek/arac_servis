import random
import time
import datetime
import string

root_path = "C:\\Users\\Tutku\\Desktop\\Python\\"

dummy_name = root_path+"dummyDataSet"+time.strftime("%Y-%m-%d_%H%M%S")+".csv"

header="id,tarih,plaka,marka,model,uretim_tarihi,km,parca_fiyat,iscilik_fiyat"






markalar=["FIAT", "MERCEDES", "BMW", "AUDI", "TOFAS", "FORD", "TESLA", "SAAB",\
         "VOLVO", "VOLKSWAGEN"]

markalar.append("PEUGEOT")

modeller = {"FIAT": ["EGEA","500L","500","DOBLO"],
         "MERCEDES": ["C180","E200","S600","S350"],
         "BMW": ["X3","X5","X7"],
         "AUDI": ["Q3","Q5","Q7","A6"],
         "TOFAS": ["SAHIN","DOGAN","KARTAL"],
         "FORD": ["FOCUS","FIESTA","KA"],
         "TESLA": ["T1","T2","T3","T4"],
         "SAAB": ["S1","S2","S3","S4"],
         "VOLVO": ["V1","V2","V3","V4"],
         "VOLKSWAGEN": ["PASSAT","JETTA","POLO"],
         "PEUGEOT": ["206","306","407"]        
         }

dosya = open(dummy_name,"w", encoding="UTF-8")
dosya.write(header+"\n")

def gelisTarihi():  
    start = datetime.datetime.now().replace(day=1, month=1, year=2018).toordinal()
    end = datetime.datetime.now().replace(day=1, month=1, year=2020).toordinal()
    pred = datetime.date.fromordinal((random.randint(start,end)))
    return pred



for x in range (24000):

    a = random.randint(1,81)
    if a < 10:
        a = "0"+str(a)
    b = random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+\
        random.choice(string.ascii_uppercase)
    c = random.randint(10,9999)


    
    tarih = gelisTarihi()
    plaka = str(a)+"-"+str(b)+"-"+str(c)
    uretim_tarihi = random.randint(2000,2017)
    km = random.randint(1000,200000)
    parca_fiyat = random.randint(50,10000)
    iscilik_fiyat = random.randint(250,2000)
    marka=random.choice(markalar)
    model=random.choice(modeller[marka])
    dosya.write(str(x)+","+str(tarih)+","+str(plaka)+","+str(marka)+","+str(model)+","+str(uretim_tarihi)+","\
                +str(km)+","+str(parca_fiyat)+","+str(iscilik_fiyat)+"\n")


dosya.close()

