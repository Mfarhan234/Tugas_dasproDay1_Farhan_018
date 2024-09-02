grade_nilai= input("masukkan grade yang anda ingin capai : ")
minimal_nilai = float(input("rata rata minimum yang diperlukan : "))
rata_rata_saat_ini = float(input("berapa rata rata nilai anda saat ini: "))
final_exam_persentase = float(input("berapa persentase ujian akhir: " ))

nilai = (minimal_nilai - rata_rata_saat_ini * (100/100 - final_exam_persentase / 100)) / (final_exam_persentase / 100)

print(f"Nilai ujian akhir yang diperlukan adalah: {nilai:,.2f} untuk mendapatkan nilai {grade_nilai}.")