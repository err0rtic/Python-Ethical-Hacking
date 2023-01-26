from multiprocessing import Process
import socket


def port_scan(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((target, port))
        print(target, 'Port :', port, "is open.")
    except socket.error:
        pass
    finally:
        s.close()


if __name__ == "__main__":
    url = input('Enter website address: ')
    for port in range(65536):
        mult = Process(target=port_scan, args=(url, port))
        mult.start()
        mult.join()
