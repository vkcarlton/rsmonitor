import pygatt

# Replace with your Govee light's MAC address
DEVICE_ADDRESS = "83:CF:C3:30:38:35:4D:92"  # Example MAC address

def discover_and_connect():
    adapter = pygatt.GATTToolBackend()

    try:
        adapter.start()
        print("Scanning for devices...")
        devices = adapter.scan(timeout=5)

        for device in devices:
            if device["address"] == DEVICE_ADDRESS:
                print(f"Found device: {device['name']} ({device['address']})")
                print("Connecting...")
                light = adapter.connect(device["address"])
                print("Connected!")

                # Now you can interact with the light, e.g., turn it on/off, change colors, etc.
                # Example commands:
                # light.char_write_handle(0x0011, b'\x01\x00')  # Example command, replace with your desired actions

                break
        else:
            print(f"Device with address {DEVICE_ADDRESS} not found.")
    finally:
        adapter.stop()

if __name__ == "__main__":
    discover_and_connect()
