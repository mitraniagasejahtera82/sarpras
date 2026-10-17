import openpyxl

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "KIB B Test Import"

headers = ["kode_barang", "nama", "jumlah", "kondisi", "tahun_perolehan"]
ws.append(headers)

ws.append(["TEST-IMP-01", "Proyektor Uji Impor", 2, "Baik", 2021])
ws.append(["TEST-IMP-01", "Mikroskop Duplikat", 1, "Baik", 2022])
ws.append(["TEST-IMP-03", "Speaker Kondisi Aneh", 3, "Banjir", 2019])
ws.append(["TEST-IMP-04", None, 1, "Baik", 2020])

wb.save("test_import_kib_b.xlsx")
print("File test_import_kib_b.xlsx berhasil dibuat.")
