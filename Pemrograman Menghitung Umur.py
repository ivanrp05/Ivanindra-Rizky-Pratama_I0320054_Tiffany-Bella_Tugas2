print("----------------------------------------------------------------------------------")
print("                      PEMROGRAMAN KOMPUTER PENGHITUNG UMUR                        ")
print("----------------------------------------------------------------------------------")
print("By : Ivanrp05")

tanggal = int(input("Masukkan tanggal lahir  Anda (xx)         : "))
bulan = int(input("Masukkan bulan lahir Anda (yy)           : "))
tahun = int(input("Masukkan tahun lahir Anda (xxyy)         : "))
print("----------------------------------------------------------------------------------")
print("                     Tanggal lahir anda adalah", tanggal,"-", bulan, "-", tahun)
print("----------------------------------------------------------------------------------")
nowtanggal = int(input("Masukkan tanggal sekarang (contoh : xx)      : "))
nowbulan = int(input("Masukkan bulan sekarang (contoh : yy)         : "))
nowtahun = int(input("Masukkan tahun sekarang (contoh : xxyy)      : "))
date = abs(nowtanggal-tanggal)
month = abs(nowbulan-bulan)
year = abs(nowtahun-tahun)

if (bulan == 1,3,5,7,8,10,12):
    date = abs((31-tanggal) + nowtanggal)
if(2):
    date = abs((28-tanggal) + nowtanggal)
if(bulan == 4,6,9,11) :
    date = abs((30-tanggal) + nowtanggal)
if not nowbulan:
    pass
else:
    date = abs(tanggal-nowtanggal)
if(nowbulan<bulan):
    month = (12-(bulan-nowbulan))
    year = (nowtahun-tahun)
if(nowbulan>bulan):
    month = (nowbulan-bulan)
print("----------------------------------------------------------------------------------")
print("    Umur Anda Sekarang Adalah", year, "tahun", month, "bulan", date, "hari        ")
print("----------------------------------------------------------------------------------")

print("Pemrograman ini ditujukan untuk menghitung umur anda secara detail, hingga ke hari")
print("Jika anda mengetahui umur anda secara detail, diharapkan anda mengingat kematian sehingga anda bertaubat")
print("Developer memohon maaf sebesar besarnya apabila terjadi kesalahan, karena kesempurnaan hanya milik Tuhan semata")

input("Press any key to continue...")