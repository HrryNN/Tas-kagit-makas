from random import randint
list=["Taş","Kağıt","Makas"]
while True:
    userVeri=input("Taş kağıt makas tan birini seciniz:")
    print("siz:",userVeri,"bilgisayar:",list[randint(0,len(list)-1)])
