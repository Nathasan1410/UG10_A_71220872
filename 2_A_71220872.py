print("===== Selamat datang di Toko Andi Tersenyum, selamat belanja! =====")
Total = int(input('Total belanja :Rp. '))
if Total>=1000000 :
    a = Total-(Total*10/100)
    print("Biaya yang Harus Anda bayar setelah diskon adalah :Rp."+str(a))
elif Total>=500000:
    a=Total-(Total*5/100)
    print("Biaya yang Harus Anda bayar setelah diskon adalah :Rp."+str(a))
elif Total>=100000:
    a=Total-(Total*2/100)
    print("Biaya yang Harus Anda bayar setelah diskon adalah :Rp."+str(a))
else :
    print("Tidak ada diskon! Maka yang Anda bayarkan adalah :Rp."+str(Total))