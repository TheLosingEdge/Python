import nmap
import sys

target = str(sys.argv[1])
ports = [21,22,23,25,80,139,389,443,445,3389,5900,8080,8081,8443]

scan_v = nmap.PortScanner()

print("Scanning",target,"for ports 21,22,23,25,80,139,389,443,445,3389,5900,8080,8081,8443 ...\n")

for port in ports:
    portscan = scan_v.scan(target,str(port))
    print("Port",port,"is",portscan['scan'][target]['tcp'][port]['state'])

print("\nHost",target,"is",portscan['scan'][target]['status']['state'])