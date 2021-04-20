import socket
import threading
import termcolor


open_ports=[]
hostname=input(termcolor.colored("[*] Please Enter IP address to scan : ", 'blue'))
host=socket.gethostbyname(hostname)
start_port=int(input(termcolor.colored("[*] Please Enter Port to begin scanning :  ", 'blue')))
end_port=int(input(termcolor.colored("[*] Please Enter Port to end scanning  :  ", 'blue')))

print('[*]Scan Result')
print('Host: %s'%(hostname))
print('IP ADDRESS: %s \n'%(host))
print('{*} Scanning..')
           # print(termcolor.colored('Port %d ---> Open ' %(ports), 'green'))




def banner(host,open_ports):
    
    for ports in open_ports:  
        try: 
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.connect((host,ports))
            banna=sock.recv(4096)
            banna=banna.decode()
            service=socket.getservbyport(ports)
            print('*'*50)
            print('Port ---> %d'%(ports))
            print('Service ---> %s'%(service))
            print('Banner ---> %s'%(banna))
            print('*'*50)
            sock.close()
        except:
            print('Unable to Connect')
            print(host)
def scan(host,start_port,end_port):
    socket.setdefaulttimeout(5)
    for ports in range(start_port, end_port):
        try:
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result=s.connect((host,ports))
            service=socket.getservbyport(ports)
            print('*'*40)
            print(termcolor.colored('Port %d ---> Open ' %(ports), 'green'))
            print(termcolor.colored('Service ---> %s ' %(service), 'green'))
            print('*'*40)
            open_ports.append(ports)
            s.close()
        except:
            pass
            #            print(termcolor.colored('Port %d ---> Closed ' %(ports), 'red'))
    banner_info=input('[*] Enter 1 to view open port banner: ')
    if banner_info=='1':
        banner(host,open_ports)
    else:
        pass

scan(host,start_port,end_port)
