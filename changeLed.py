import pygatt

adapter = pygatt.GATTToolBackend()
adapter.start()
mac = "24:35:CC:0C:B1:4F"
uuid_handle = "0000fff1-0000-1000-8000-00805f9b34fb"

ALWAYS_ON = "0501020340"
RESET_STATE = "0501020300"
FAST_TWINKLE = "0501020320"
WAVE = "0501020301"

def writeCode(hexString):
    d = adapter.connect(mac)
    d.char_write(uuid_handle, bytes.fromhex(hexString))
    d.disconnect()

writeCode(RESET_STATE)
#writeCode(ALWAYS_ON)
writeCode(WAVE)
