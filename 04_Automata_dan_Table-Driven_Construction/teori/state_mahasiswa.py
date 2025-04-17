from enum import Enum

class MahasiswaState(Enum):
    TERDAFTAR = "Terdaftar"
    AKTIF = "Aktif"
    CUTI = "Cuti"
    LULUS = "Lulus"

class StateTrigger(Enum):
    CETAK_KSM = "Cetak KSM"
    MENGAJUKAN_CUTI = "Mengajukan Cuti"
    LULUS = "Lulus"
    MENYELESAIKAN_CUTI = "Menyelesaikan Cuti"

state_transition = {
    MahasiswaState.TERDAFTAR: {
        StateTrigger.CETAK_KSM: MahasiswaState.AKTIF,
        StateTrigger.MENGAJUKAN_CUTI: MahasiswaState.CUTI
    },
    MahasiswaState.AKTIF: {
        StateTrigger.MENGAJUKAN_CUTI: MahasiswaState.CUTI,
        StateTrigger.LULUS: MahasiswaState.LULUS
    },
    MahasiswaState.CUTI: {
        StateTrigger.MENYELESAIKAN_CUTI: MahasiswaState.TERDAFTAR
    }
}

def change_state(current_state, trigger_input):
    if current_state in state_transition and trigger_input in state_transition[current_state]:
        return state_transition[current_state][trigger_input]
    
    return "transisi salah"

current_state = MahasiswaState.TERDAFTAR
next_state = change_state(current_state, StateTrigger.LULUS)
print(next_state)