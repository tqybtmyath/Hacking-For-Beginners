import os
import subprocess
import webbrowser

def print_green(text):
    print("\033[92m" + text + "\033[0m")

def communication():
    if not 'SUDO_UID' in os.environ.keys():
        print("Try running this program with sudo.")
        exit()
    os.system('figlet Hacking For Beginners')
    print()
    print()
    print_green('[0] Launch And Clean Up Your System Completely')
    print_green('[1] Launch Nmap Port Scanner')
    print_green('[2] Launch Wifite (WPA-PSK Key Cracker)')
    print_green('[3] Launch Metasploit Framework')
    print_green('[4] Launch Social Engineering ToolKit')
    print_green('[5] Launch Ettercap Graphical (GUI)')
    print_green('[6] Launch And Install Python2')
    print_green('[7] Launch And Run Install Visual Studio Code Editor')
    print_green('[8] Launch Fern Wi-Fi Cracker Tool (GUI)')
    print_green('[9] Launch And Install Python')
    print_green('[10] Launch My GitHun Account')
    print_green('[11] Launch And Install Wifi-Phisher')
    print_green('[12] Launch And Ping A Website')
    print_green('[13] Launch And Install Bettercap')
    print()
    user_choose = input('root@kali:~# ')

    if user_choose == '0':
        subprocess.run(['sudo', 'apt', 'install', 'bleachbit'])
        subprocess.run(['bleachbit'])
    elif user_choose == '1':
        user_ip = input('Enter ip to scan: ')
        subprocess.run(['nmap', user_ip])
    elif user_choose == '2':
        subprocess.run(['wifite'])
    elif user_choose == '3':
        subprocess.run(['msfconsole'])
    elif user_choose == '4':
        subprocess.run(['setoolkit'])
    elif user_choose == '5':
        subprocess.run(['ettercap', '-G'])
    elif user_choose == '6':
        subprocess.run('sudo', 'apt', 'install', 'python2')
    elif user_choose == '7':
        subprocess.run(['sudo', 'apt', 'install', 'code'])
        subprocess.run(['code'])
    elif user_choose == '8':
        subprocess.run(['sudo', 'fern-wifi-cracker'])
    elif user_choose == '9':
        subprocess.run(['sudo', 'apt', 'install', 'python3'])
    elif user_choose == '10':
        webbrowser.open('https://github.com/tqybtmyath')
    elif user_choose == '11':
        subprocess.run(['sudo', 'apt', 'install', 'wifiphisher'])
        subprocess.run(['sudo', 'wifiphisher'])
    elif user_choose == '12':
        ip = input('Enter Website to Ping: ')
        subprocess.run(['ping', ip])
    elif user_choose == '13':
	    interface = input('Enter your kali linux interface: ')
	    subprocess.run(['sudo', 'apt', 'install', 'bettercap'])
	    subprocess.run(['bettercap', '-iface', interface])
    else:
        print('[-] Unknown Symbol.')

communication()
