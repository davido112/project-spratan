import serial

config_file = open("config.cisco", "r").readlines()

ser = serial.Serial()
ser.baudrate = 9600
ser.port = input("Add meg, hogy melyik Serial porton szeretnél csatlakozni! ")
try:
    ser.open()
    for config in config_file:
        if "#" in config[0]:
            pass
        else:
            ser.write(config.encode("utf-8"))

    ser.write(b"\ndo copy run start\n")
    ser.write(b"\n")
    ser.close()
    print("A konfiguráció feltöltése sikeresen végbement!")
except:
    print("A konfiguráció nem ment végbe! Feltehetőleg megnyitva maradt egy csatlakozás az eszközhöz.")