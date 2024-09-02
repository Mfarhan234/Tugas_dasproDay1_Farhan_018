kecepatan_takeoff = float(input("masukkan kecepatan jet saat take off :" ))
jarak_meter = float(input("masukkan jarak landasan : "))

time = 1000 / 3600  # 1 km/jam= 1000 m/3600 detik.

kecepatan_takeoff_ms = kecepatan_takeoff * time # Konversi dari km/jam ke m/detik v= a.t


percepatan = (kecepatan_takeoff_ms ** 2) / (2 * jarak_meter)  #mencari percepatan dengan rumus (a+v**2) / (2*s)

waktu = kecepatan_takeoff_ms / percepatan # menghitung waktu takeoff

print(f"Kecepatan take off jet fighter : {kecepatan_takeoff_ms:,.2f} m/s")
print(f"Percepatan: {percepatan:.2f} m/s²")
print(f"Waktu: {waktu:.2f} detik")