from rda5807 import RDA5807

radio = RDA5807()

radio.set_volume(10)
radio.tune(99.5)

print("Tuned to:", radio.read_status()["freq_mhz"], "MHz")

found = radio.seek(up=True)

if found is not None:
    print("Found station at", found, "MHz")
else:
    print("No station found")

radio.set_volume(15)
radio.set_mono(True)

status = radio.read_status()
print(
    status["freq_mhz"],
    "MHz, RSSI:",
    status["rssi"],
    "Stereo:",
    status["stereo"]
)