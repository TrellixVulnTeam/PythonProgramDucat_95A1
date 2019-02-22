# Python Program - Shutdown Computer
	
import os
check = input("Want to shutdown your computer ? (y/n): ");
if check == 'n':
    exit()
else:
    os.system("shutdown /s /t 1")
	
'''
output ===

Want to shutdown your computer ? (y/n): y
'shutdown' is not recognized as an internal or external command,
operable program or batch file.

your system has shutdown.
'''