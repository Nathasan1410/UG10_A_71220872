a = input('Masukkan nama mahasiswa: ')
b = input('Masukkan NIM-nya: ')
if ((int(str(b)[2:4]) == 20 or 21 or 22) and ((int(str(b)[:2]) == 71))):
    print(a+(" merupakan mahasiswa informatika angkatan 20 hingga 22"))
else :
    print(a+(" bukan mahasiswa informatika angkatan 20 hingga 22"))