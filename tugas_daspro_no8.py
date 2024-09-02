def hitung_penghematan(jumlah_penduduk):
    a= 15  # penggunaan toilet perorang(versi lama)
    b= 2   # liter per penyiraman
    c = 14 #total setiap orang ke toilet
    d= 150  # biaya pengaadan toilet baru
    e = 3   #penggunaan per toilet oleh orang
    toilet = jumlah_penduduk / e
    air_dihemat = toilet * c* (a - b)
    biaya= toilet * d
    return air_dihemat, biaya

jumlah_penduduk = int(input("Masukkan jumlah penduduk: "))
air_dihemat, biaya, = hitung_penghematan(jumlah_penduduk)

print(f"Penghematan air: {air_dihemat:.2f} liter/hari")
print(f"Biaya penggantian toilet: {biaya:.2f}USD")