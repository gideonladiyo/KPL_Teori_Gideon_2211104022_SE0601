from enum import Enum

class JenisKelamin(Enum):
    PRIA = 1
    WANITA = 2

patients = []

def add_patient(name: str, gender: JenisKelamin):
    if not isinstance(gender, JenisKelamin):
        raise ValueError("Jenis kelamin harus pria atau wanita")
    patients.append(
        {
            "name": name,
            "gender": gender.name
        }
    )
    print(f"pasien {name} dengan jenis kelamin {gender.name} berhasil ditambahkan")

try:
    add_patient("wahyu", JenisKelamin.PRIA)
    add_patient("dapin", JenisKelamin.TRANSGENDER)
except:
    print("error")