from __future__ import print_function
import frida
import sys
from parseData import parseData

def on_message(message, data):
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
    if len(sys.argv) != 2:
        print("Usage: %s <process name or PID>" % __file__)
        sys.exit(1)

    try:
        target_process = int(sys.argv[1])
    except ValueError:
        target_process = sys.argv[1]
    main(target_process)