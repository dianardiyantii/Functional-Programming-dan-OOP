#Nama : Dian Ardiyanti Saputri
#Npm  : G1A022084

'''
Perbedaan Functional Programming dan OOP
Functional programming adalah paradigma pemrograman yang berfokus pada fungsi sebagai unit dasar dari program. 
Dalam functional programming, fungsi dianggap sebagai nilai yang dapat diteruskan sebagai argumen ke fungsi lainnya 
dan dapat dikembalikan sebagai hasil dari fungsi tersebut. Pemrograman fungsional juga menekankan pada pemakaian 
fungsi yang tidak memiliki efek samping, artinya, fungsi hanya bergantung pada argumen yang diberikan dan 
tidak mengubah variabel global atau menghasilkan efek samping lainnya.

OOP adalah paradigma pemrograman yang berfokus pada objek sebagai unit dasar dari program. Dalam OOP, objek dapat 
memiliki properti atau data yang menyimpan informasi tentang objek tersebut dan juga memiliki metode atau fungsi yang 
memungkinkan objek untuk melakukan tindakan atau memproses informasi. OOP juga menekankan pada konsep pewarisan, 
di mana objek dapat mewarisi sifat atau perilaku dari objek lain dan dapat mengimplementasikan polimorfisme, artinya, 
objek dengan tipe yang berbeda dapat menggunakan metode dengan nama yang sama dan menghasilkan hasil yang berbeda.
'''
#CONTOH Functional Programming
# Fungsi untuk menghitung bilangan pangkat
def pangkat(basis, eksponen):
    if eksponen == 0:
        return 1
    else:
        return basis * pangkat(basis, eksponen - 1)
print(pangkat(2, 3)) # Output: 8

#CONTOH OOP
class Mahasiswa:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def introduce(self):
        print(f"Nama saya {self.nama} dan saya berumur {self.umur} tahun.")

mhs1 = Mahasiswa("Dian", 19)
mhs1.introduce()

#Perbedaan Signifikan dari FP dan OOP
'''
Pendekatan Dasar
Functional programming didasarkan pada penggunaan fungsi sebagai unit dasar program. Fungsi dalam pemrograman 
fungsional biasanya dianggap sebagai nilai yang dapat diteruskan sebagai argumen ke fungsi lainnya dan dapat 
dikembalikan sebagai hasil dari fungsi tersebut. Sedangkan dalam OOP, objek adalah unit dasar program. Objek dalam 
OOP memiliki properti atau data yang menyimpan informasi tentang objek tersebut dan juga memiliki metode atau fungsi 
yang memungkinkan objek untuk melakukan tindakan atau memproses informasi.

Penggunaan Variabel
Dalam functional programming, penggunaan variabel terbatas, dan variabel yang dideklarasikan biasanya tidak berubah. 
Sebaliknya, dalam OOP, penggunaan variabel lebih umum, dan variabel yang dideklarasikan dapat diubah melalui metode objek.

Efek Samping
Functional programming menekankan pada penggunaan fungsi yang tidak memiliki efek samping, artinya, fungsi hanya bergantung 
pada argumen yang diberikan dan tidak mengubah variabel global atau menghasilkan efek samping lainnya. Sementara itu, 
dalam OOP, objek dapat memiliki efek samping dan dapat memodifikasi properti objek atau variabel global lainnya.

Pewarisan
Pewarisan adalah konsep penting dalam OOP, di mana objek dapat mewarisi sifat atau perilaku dari objek lain dan dapat 
mengimplementasikan polimorfisme. Sedangkan dalam functional programming, pewarisan dilakukan melalui komposisi, 
di mana sebuah fungsi dapat menggunakan fungsi lain sebagai argumen dan membangun kompleksitas dengan menggabungkan 
fungsi-fungsi tersebut.

Kejelasan dan Kesederhanaan
Functional programming menekankan pada kejelasan dan kesederhanaan kode. Functional programming menghindari penggunaan 
state yang tersembunyi dan mengurangi kompleksitas dengan memisahkan data dan logika. Sebaliknya, OOP menekankan pada 
fleksibilitas dan skalabilitas kode, di mana objek dapat diubah untuk memenuhi kebutuhan yang berbeda.
'''