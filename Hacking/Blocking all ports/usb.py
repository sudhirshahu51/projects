# To Block or Unblock all the usb ports that are unused
import winreg

try:
    key = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, "System\\CurrentControlSet\\Services\\USBSTOR",
                             reserved=0, access=winreg.KEY_ALL_ACCESS)  # Creating a key object
    ans = input('To block all usb ports enter B\n To unblock all usb ports enter U\n To exit the GUI enter Q\n')
    while ans != 'Q':
        if ans == 'B':
            winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 4)		# To block all ports
            print('All usb ports blocked')
        elif ans == 'U':
            winreg.SetValueEx(key, 'Start', 0, winreg.REG_DWORD, 3)		# To unblock all ports
            print('All usb ports unblocked')
        else:
            print('''You've Entered WRONG value, Please try again''')
        ans = input('Enter the new decision\n')
    winreg.CloseKey(key)
except :
    print('''You've run into some problem,, Please contact the author for further instructions''')