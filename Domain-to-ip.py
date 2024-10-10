import socket
import pyfiglet
from termcolor import colored

#Banner name and color section
banner =  colored (pyfiglet.figlet_format("Domain to IP"), 'red')
print("#########  Created by : Md. Rayhanul Islam  #########")
print(banner)



#Domain to ip section
domain_name = input("Enter your target website name:")
ip = socket.gethostbyname(domain_name)
print("IP of {} : {}" .format(domain_name, ip))
