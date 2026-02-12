from picamzero import Camera
from time import sleep, time
from astro_pi_orbit import ISS
import math

# --- setup ---
camera = Camera()
iss = ISS()

# --- scatta foto ---
for i in range(5):
    camera.take_photo(f'image_{i:03d}.jpg')
    sleep(2)

# --- coordinate ISS ---
def get_gps_coordinates():
    point = iss.coordinates()
    return (point.latitude.degrees, point.longitude.degrees)

# --- distanza ---
def calculate_distance_km(coord1, coord2):
    R = 6371.0

    lat1 = math.radians(coord1[0])
    lon1 = math.radians(coord1[1])
    lat2 = math.radians(coord2[0])
    lon2 = math.radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c

# --- durata totale ---
DURATA = 600  # 10 minuti

start_time = time()
speeds = []

while time() - start_time < DURATA:
    t1 = time()
    coord1 = get_gps_coordinates()

    sleep(5)

    coord2 = get_gps_coordinates()
    t2 = time()

    distance_km = calculate_distance_km(coord1, coord2)
    dt = t2 - t1

    if dt > 0:
        speeds.append(distance_km / dt)

# --- media velocità ---
if speeds:
    speed_km_s = sum(speeds) / len(speeds)
else:
    speed_km_s = 0

# --- salva risultato ---
with open("result.txt", "w") as f:
    f.write(f"{speed_km_s:.4f}")
