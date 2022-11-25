no1 = int(input('Masukkan nilai soal 1: '))
no2 = int(input('Masukkan nilai soal 2: '))
no3 = int(input('Masukkan nilai soal 3: '))
Umur = int(input('Masukkan umur anda: '))
poin1 = (no1*50/100)
poin2 = (no2*30/100)
poin3 = (no3*20/100)
ratarata = (poin1+poin2+poin3)
print("Rata-rata nilai anda: "+str(ratarata))
if Umur<=25:
    if ratarata>=80:
        print("Selamat anda lulus!")
    else :
        print("Coba lagi tahun depan!")
else :
    if ratarata>=90:
        print("Selamat anda lulus!")
    else :
        print("Coba lagi tahun depan!")