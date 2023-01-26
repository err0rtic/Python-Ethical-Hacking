import socket


def addres(num, host):
    if num != 10:
        host = input('Enter host: ')
    if '://' in host:
        host = host.split('://')[1]
    host = host.replace("/", '')
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror as e:
        print(f'Invalid hostname, error raised is {e}')
    except socket.error as e:
        print("Couldnt connect with the socket-server: %s\n terminating program" % e)
    except SyntaxError as e:
        print("Syntax Error: %s\n terminating program" % e)
    else:
        if remote_ip == [] or remote_ip == '0.0.0.0' :
            pass
        else:
            print(f"{'IP Address of '}{host}{' is '}{remote_ip}")
        return remote_ip, host
