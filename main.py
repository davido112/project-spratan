import serial
from netmiko import ConnectHandler
import getpass

serial_or_ssh = input("Hogyan szeretnél csatlakozni az eszközhöz? (Serial, SSH)\n").lower()
config_file = open("config.cisco", "r").readlines()


if serial_or_ssh == "serial":
    ser = serial.Serial()

    ser.baudrate = 9600
    ser.port = input("Add meg, hogy melyik Serial porton szeretnél csatlakozni! ")
    ser.open()

    for config in config_file:
        if "#" in config[0]:
            pass
        else:
            ser.write(config.encode("utf-8"))

    ser.write(b"do copy run start\n")
    ser.close()
    print("A konfiguráció feltöltése sikeresen végbement!")

elif serial_or_ssh == "ssh":
    ip_address = input("Eszköz IP címe: ")
    ssh_user = input("SSH felhasználó neve: ")
    ssh_password = getpass.getpass("SSH felhasználó jelszava: ")
    connect = {
        'device_type': 'cisco_ios',
        'host': f'{ip_address}',
        'username': f'{ssh_user}',
        'password': f'{ssh_password}'
    }
    
    ssh = ConnectHandler(**connect)

    for config in config_file:
        if "#" in config[0]:
            pass
        else:
            output = ssh.send_command(config)

    print(output)
    ssh.disconnect()
else:
    print(f'Ilyen lehetőség nem elérhető, hogy "{serial_or_ssh}"')