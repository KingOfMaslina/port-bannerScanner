import socket #библиотека для взаимодействия с компами через TCP и UDP

def scan(target,ports):
    print('\n' + 'Scanning '+ str(target))
    for port in range(1,ports):
        scan_port(target,port)


def scan_port(ip,port):
    try:
        sock = socket.socket()
        sock.connect((ip,port))
        banner = sock.recv(1024).decode()
        print("Port Opened" + str(port) + "with port" + banner)
        sock.close()
    except:
        pass

targets = input("Enter targets to scan(split by ,): ")
ports = int(input("How many ports? "))
if ',' in targets:
    print("Scanning multiple targets")
    for ip in targets.split(','):
        scan(ip.strip(' '), ports)
else:
    scan(targets,ports)