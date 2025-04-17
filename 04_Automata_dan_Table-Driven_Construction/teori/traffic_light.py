from enum import Enum
import time

class TrafficState(Enum):
    MERAH = "Merah"
    HIJAU = "Hijau"
    KUNING = "Kuning"

state_transition = {
    TrafficState.MERAH: TrafficState.HIJAU,
    TrafficState.HIJAU: TrafficState.KUNING,
    TrafficState.KUNING: TrafficState.MERAH
}

state_duration = {
    TrafficState.MERAH: 4,
    TrafficState.HIJAU: 6,
    TrafficState.KUNING: 2
}

current_state = TrafficState.MERAH

while True:
    print(f"Sedang lampu {current_state.value}, dengan waktu {state_duration[current_state]} detik")
    time.sleep(state_duration[current_state])
    current_state = state_transition[current_state]