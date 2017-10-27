#!/usr/bin/env python3

import sys, os
from glob import iglob
import os.path

def main():
    possible_commands = ["tomitaparser"]
    check_cmd = "which >/dev/null 2>&1 "
    if sys.platform.startswith("linux"):
        possible_commands += ["tomita-linux32", "tomita-linux64"]
    elif sys.platform.startswith("freebsd"):
        possible_commands += ["tomita-freebsd64"]
    elif sys.platform.startswith("darwin"):
        possible_commands += ["tomita-mac"]
    elif sys.platform.startswith("win"):
        possible_commands += ["tomita-win32"]
        check_cmd = "where /q >nul 2>&1 "

    try:
        cmd = next(x for x in possible_commands if os.system("where /q " + x) == 0)
    except StopIteration:
        print("Error: tomita parser not found!")
        exit(1)

    dnrp = os.path.dirname(os.path.realpath(__file__))
    mpath = os.path.join(dnrp, "..", "test", "data")

    all_flag = False
    range_of_files = []
    for i in sys.argv[1:]:
        if i[0] == '*':
            all_flag = True
            break
        else: range_of_files.append(i)

    ext_cmd = cmd + " " + os.path.join(dnrp, "config", "config.proto") +\
        " <\"" + os.path.join(mpath, "input", '') + "{0}.txt\" | \"" +\
        sys.executable + "\" normalize.py" +\
        " >\"" + os.path.join(mpath, "facts", '') + "{0}.xml\""

    if not range_of_files:
        if all_flag:
            range_of_files = iglob(os.path.join(mpath, "input", "*.txt"))
        else:
            print("Error: no files listed (nor used -a option)!")
            exit(4)

    for f in range_of_files:
        print("Processing", f, "file")
        bnf = os.path.splitext(os.path.basename(f))[0]
        os.system(ext_cmd.format(bnf))
        print("Processed", f, "file")
        print()

if __name__ == '__main__':
    main()
