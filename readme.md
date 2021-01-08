# wapisteal
Steal credentials on Windows by hooking several Windows API functions!

# how it works
- hooks `CreateProcessWithLogonW`, `CredIsMarshaledCredentialW` and `CredReadW` from `Advapi32.dll`
- waits for new calls
- prints the parameters 
- continues with execution 

# how to use 

`python main.py PROCESS_ID_OR_NAME`

# examples

`python main.py 6789`

`python main.py powershell.exe`

# demo

1. Create a new powershell instance
2. Type `python main.py powershell.exe` in a separate powershell window (or cmd)
3. use `Start-Process notepad.exe -Credential YourUsername`
4. input password
5. you will get the password
