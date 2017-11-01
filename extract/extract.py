#!/usr/bin/env python3

from glob import iglob
import os
import os.path
import sys
import subprocess
import shutil


def main():
    possible_commands = ["tomitaparser"]
    if sys.platform.startswith("linux"):
        possible_commands += ["tomita-linux32", "tomita-linux64"]
    elif sys.platform.startswith("freebsd"):
        possible_commands += ["tomita-freebsd64"]
    elif sys.platform.startswith("darwin"):
        possible_commands += ["tomita-mac"]
    elif sys.platform.startswith("win"):
        possible_commands += ["tomita-win32"]

    program_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(program_dir)
    try:
        cmd = next(
            x for x in possible_commands
            if shutil.which(x)
        )
    except StopIteration:
        print("Error: tomita parser not found!")
        exit(1)

    mpath = os.path.join(program_dir, "..", "test", "data")

    all_flag = False
    range_of_files = []
    for i in sys.argv[1:]:
        if i[0] == '*':
            all_flag = True
            break
        else:
            range_of_files.append(i)

    config_path = os.path.join(program_dir, "config", "config.proto")
    input_path = os.path.join(mpath, "input", '{}.txt')
    facts_path = os.path.join(mpath, "facts", '{}.xml')

    if not range_of_files:
        if all_flag:
            range_of_files = iglob(os.path.join(mpath, "input", "*.txt"))
        else:
            print("Error: no files listed (nor used -a option)!")
            exit(4)

    for file in range_of_files:
        print("Processing", file, "file", file=sys.stderr)
        file_base_name = os.path.splitext(os.path.basename(file))[0]
        with open(input_path.format(file_base_name)) as input_file:
            ext_proc = subprocess.Popen(
                [cmd, config_path],
                stdin=input_file,
                stdout=subprocess.PIPE
            )
            with open(facts_path.format(file_base_name), 'w') as output_file:
                subprocess.check_call(
                    [sys.executable, 'normalize.py'],
                    stdin=ext_proc.stdout,
                    stdout=output_file
                )

        print("Processed", file, "file", end="\n\n", file=sys.stderr)

if __name__ == '__main__':
    main()
