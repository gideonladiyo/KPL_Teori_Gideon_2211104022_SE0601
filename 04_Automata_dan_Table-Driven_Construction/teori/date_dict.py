days_in_months = {
    "Januari": 31,
    "Februari": 28,
    "Maret": 31,
    "April": 30,
    "Mei": 31,
    "Juni": 30,
    "Juli": 31,
    "Agustus": 31,
    "September": 30,
    "Oktober": 31,
    "November": 30,
    "Desember": 31
}

bulan = input("Masukkan bulan: ")
hari = days_in_months.get(bulan, "Bulan tidak valid")
print(hari)