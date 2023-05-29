import numpy
i=[]
while True:
    i=float(input("N="))
    i+=1
    cetak=input("apakah anda ingin input lagi (Y/N)")
    if cetak=='Y':
        i=float(input("N="))
    if cetak=='N':
        for x,val in enumerate([i]):
            print("data index ke-{}={}".format(x,i))

            