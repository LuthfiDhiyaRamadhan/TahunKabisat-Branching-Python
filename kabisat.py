tahun= int(input("Tahun :"))
if (tahun%100!=0) and (tahun%4==0) or \
        (tahun%100==0) and (tahun%400==0):
    print(f"Tahun{tahun} adalah tahun Kabisat")
else:
    print(f"Tahun{tahun} adalah bukan tahun Kabisat")