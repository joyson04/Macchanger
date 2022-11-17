import subprocess as sub
import optparse
import re
import sys
import os
import time


blue = "\033[94m1"
red =  "\033[91m" 
green = "\033[92m" 
yellow = "\u001b[33m"
White = "\u001b[37m"
magenta = "\u001b[35m"


def banner(value):
   
        sys.stdout.write(value)
        sys.stdout.flush()
        time.sleep(0.2 / 100)
banner(blue + "[+]+++++++++++++++++++++++  Starting +++++++++++++++++++++++++++++++++++++++++[+]")
time.sleep(5)
os.system('clear')


banner(green+ '''                                                                                                                                                                                                                               
          ____                                  ,---,                                                           
        ,'  , `.                              ,--.' |                                                           
     ,-+-,.' _ |                              |  |  :                      ,---,                        __  ,-. 
  ,-+-. ;   , ||                              :  :  :                  ,-+-. /  |  ,----._,.          ,' ,'/ /| 
 ,--.'|'   |  || ,--.--.     ,---.     ,---.  :  |  |,--.  ,--.--.    ,--.'|'   | /   /  ' /   ,---.  '  | |' | 
|   |  ,', |  |,/       \   /     \   /     \ |  :  '   | /       \  |   |  ,"' ||   :     |  /     \ |  |   ,' 
|   | /  | |--'.--.  .-. | /    / '  /    / ' |  |   /' :.--.  .-. | |   | /  | ||   | .\  . /    /  |'  :  /   
|   : |  | ,    \__\/: . ..    ' /  .    ' /  '  :  | | | \__\/: . . |   | |  | |.   ; ';  |.    ' / ||  | '    
|   : |  |/     ," .--.; |'   ; :__ '   ; :__ |  |  ' | : ," .--.; | |   | |  |/ '   .   . |'   ;   /|;  : |    
|   | |`-'     /  /  ,.  |'   | '.'|'   | '.'||  :  :_:,'/  /  ,.  | |   | |--'   `---`-'| |'   |  / ||  , ;    
|   ;/        ;  :   .'   \   :    :|   :    :|  | ,'   ;  :   .'   \|   |/       .'__/\_: ||   :    | ---'     
'---'         |  ,     .-./\   \  /  \   \  / `--''     |  ,     .-./'---'        |   :    : \   \  /           
               `--`---'     `----'    `----'             `--`---'                  \   \  /   `----'            
                                                                                    `--`-'                       
\n''')
print( "\n education purpose only\n")
print("\n https://www.instagram.com/arav.indh7393/?igshid=YmMyMTA2M2Y\n")
print("python2 macchanger.py -i eth0 -m 60:44:57:99:33:22")


def get_args():
  parser = optparse.OptionParser()
  req_args = parser.add_option_group("Required Arguments")
  req_args.add_option('-i', '--interface', dest = 'interface', help = 'Interface name whose MAC is to be changed')
  req_args.add_option('-m', '--mac', dest = 'new_mac', help = 'New MAC Address')
  (option, arguments) = parser.parse_args()
  if not option.interface:
    parser.error(red  +  '[-] Please specify an interface in the arguments, use --help for more info.') 
  elif not option.new_mac:
    parser.error(red  +  '[-] Please specify a new MAC Address, use --help for more info.')
  else:
    return option



def change_mac(interface, new_mac):
  
  if len(new_mac) != 17:
    print(red + '[-] Please enter a valid MAC Address')
    quit()
  
  print(green + '\n[+] Changing the MAC Address to', new_mac)
  sub.call(['sudo', 'ifconfig', interface, 'down'])
  sub.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
  sub.call(['sudo', 'ifconfig', interface, 'up'])
  
  
  
def get_current_mac(interface):
  output = sub.check_output(['ifconfig', interface], universal_newlines = True)
  search_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
  if search_mac:
    return search_mac.group(0)
  else:
    print(red +  '[-] Could not read the MAC Address')
    
    
command_args = get_args()

prev_mac = get_current_mac(command_args.interface)
print(magenta +  '\n[+] MAC Address before change -> {}'.format(prev_mac))

change_mac(command_args.interface, command_args.new_mac)

changed_mac = get_current_mac(command_args.interface)
print(White +  '\n[+] MAC Address after change -> {}'.format(changed_mac))

if changed_mac == command_args.new_mac:
  print(yellow +  '\n[+] MAC Adress was successfully changed from {} to {}'.format(prev_mac, changed_mac))
else:
  print(red +  '\n[-] Could not change the MAC Address')