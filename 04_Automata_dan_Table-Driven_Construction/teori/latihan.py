from enum import Enum
import random
import time

# state
class FsmState(Enum):
    IDLE = "Idle"
    MENUNGGU_PRODUK = "Menunggu Produk"
    MENGELUARKAN_PRODUK = "Mengeluarkan Produk"
    SELESAI = 'Selesai'
    EXIT = "Exit"

# class user
class User:
    balance = 0
    state = FsmState.IDLE
    def __init__(self, name):
        self.name = name
    def change_name(self, name):
        self.name = name
    def add_balance(self, jumlah: int):
        self.balance += jumlah
    def reduce_balance(self, jumlah: int):
        self.balance -+ jumlah

# mesin gacha
class Casino:
    pilihan = 1
    def pilih_gacha(self, pilihan):
        self.pilihan = pilihan
    def gacha(self):
        print("Mulai gacha...")
        time.sleep(3)
        angka1 = random.randint(1, 10)
        print(f"Angka pertama: {angka1}")
        time.sleep(3)
        angka2 = random.randint(1, 10)
        print(f"Angka kedua: {angka2}")
        time.sleep(3)
        angka3 = random.randrange(1, 10)
        print(f"Angka ketiga: {angka3}")
        if angka1 == angka2 == angka3:
            tambahan_dana = (daftar_menu.get(str(self.pilihan))) ** 2
            user.add_balance(tambahan_dana)
            print(f"Selamat anda mendapatkan saldo sebesar ${tambahan_dana}")
        else:
            print("Anda kurang beruntung")

# state trigger
class StateTrigger(Enum):
    MASUKKAN_UANG = "Masukkan Uang"
    PILIH_PRODUK = "Pilih Produk"
    KELUARKAN_PRODUK = "Keluarkan Produk"
    RESET = "Reset"
    EXIT = "Exit"

# transition
state_transition = {
    FsmState.IDLE: {
        StateTrigger.MASUKKAN_UANG: FsmState.MENUNGGU_PRODUK,
        StateTrigger.EXIT: FsmState.EXIT,
    },
    FsmState.MENUNGGU_PRODUK: {
        StateTrigger.PILIH_PRODUK: FsmState.MENGELUARKAN_PRODUK,
        StateTrigger.EXIT: FsmState.EXIT,
    },
    FsmState.MENGELUARKAN_PRODUK: {
        StateTrigger.KELUARKAN_PRODUK: FsmState.SELESAI,
        StateTrigger.EXIT: FsmState.EXIT,
    },
    FsmState.SELESAI: {
        StateTrigger.RESET: FsmState.IDLE,
        StateTrigger.EXIT: FsmState.EXIT,
    },
}
# change state
def change_state(current_state, trigger_input):
    if (current_state in state_transition
        and trigger_input in state_transition[current_state]):
        return state_transition[current_state][trigger_input]
    
    return "transisi salah"

# exit state
def exit_state(current_state):
    return change_state(current_state, trigger_input=StateTrigger.EXIT)

# user
user = User(name="Gideon")
casino = Casino()

# idle
def idle_menu():
    while True:
        print(f"\n==== SELAMAT DATANG {user.name}!")
        print("1. Cek saldo")
        print("2. Tambah saldo")
        print("3. Ganti nama")
        print("4. Masukkan uang")
        print("5. Exit")
        try:
            pilihan = int(input("Pilih pilihan anda(1/2/3/4/5): "))
            if pilihan == 1:
                print(f"Saldo anda ${user.balance}")
            elif pilihan == 2:
                try:
                    jumlah = int(input("Jumlah uang: "))
                    user.add_balance(jumlah)
                except:
                    print("Pilihan tidak valid")
            elif pilihan == 3:
                nama = input("Masukkan nama baru anda: ")
                user.change_name(nama)
            elif pilihan == 4:
                if user.balance < 100:
                    print("Saldo anda kurang dari $100, apakah anda ingin mengutang?")
                    while True:
                        pilihan_4 = input("ya/tidak: ")
                        if pilihan_4 == "ya":
                            user.state = change_state(user.state, StateTrigger.MASUKKAN_UANG)
                            break
                        elif pilihan_4 == "tidak":
                            user.state = main()
                            break
                        else:
                            print("Pilihan tidak valid")
                break
            elif pilihan == 5:
                user.state = exit_state(user.state)
                break
            else:
                print("Pilihan tidak valid")
        except :
            print("Pilihan tidak valid")
daftar_menu = {"1": 100, "2": 1000, "3": 1000000}
# menunggu produk
def menunggu_menu():
    while True:
        print("\nPilih uang yang ingin anda habiskan")
        print("1. $100")
        print("2. $1000")
        print("3. $1000000")
        print("4. Exit")
        try:
            pilihan = int(input("Pilihan anda(1/2/3/4): "))
            casino.pilih_gacha(pilihan)
            if pilihan == 4:
                user.state = change_state(user.state, StateTrigger.EXIT)
                break
            user.balance -= daftar_menu.get(str(pilihan), "err")
            user.state = change_state(user.state, StateTrigger.PILIH_PRODUK)
            break
        except:
            print("Input tidak valid")

# main
def main():
    while True:
        if user.state == FsmState.IDLE:
            idle_menu()
        elif user.state == FsmState.MENUNGGU_PRODUK:
            menunggu_menu()
        elif user.state == FsmState.MENGELUARKAN_PRODUK:
            casino.gacha()
            user.state = change_state(user.state, StateTrigger.KELUARKAN_PRODUK)
        elif user.state == FsmState.SELESAI:
            print("\nApakah anda ingin ulang atau keluar?")
            print("1. Ulang")
            print("2. Keluar")
            try:
                pilihan = int(input("Pilihan anda(1/2): "))
                if pilihan == 1:
                    user.state = change_state(user.state, StateTrigger.RESET)
                elif pilihan == 2:
                    exit_state(user.state)
            except:
                print("Pilihan tidak sesuai")
        elif user.state == FsmState.EXIT:
            print("Terimakasih telah menggunakan aplikasi ini!")
            break

main()
