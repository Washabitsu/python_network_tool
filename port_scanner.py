import socket

def PortScanner(ipAddress, ports):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    PortRange = ports.split('-')
    OpenPorts = []
    showEveryPort = True if input("Do you want to show the result for every port?(Y/N)").lower() == "y" else False
    for port in range(int(PortRange[0]),int(PortRange[1])+1):
        if s.connect_ex((ipAddress,port)) == 0:
            if showEveryPort:
                print("*** Port",port," - OPEN ***")
            OpenPorts.append(port)
        else:
            if showEveryPort:
                print("*** Port",port," - CLOSED ***")
    if not(showEveryPort):
        for port in OpenPorts:
            print("*** Port",port," - OPEN ***")

PortRange = input("Enter the port : ")
ipAddress = input("Enter the target_ip : ")

PortScanner(ipAddress,PortRange)






