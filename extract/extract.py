import sys, os
from glob import iglob
import os.path

list_of_possible_commands = ["tomitaparser"]
def findc(cmd):
    return os.system("command -v >/dev/null " + cmd) == 0
if sys.platform.startswith("linux"):
    list_of_possible_commands += ["tomita-linux32", "tomita-linux64"]
elif sys.platform.startswith("freebsd"):
    list_of_possible_commands += ["tomita-freebsd64"]
elif sys.platform.startswith("darwin"):
    list_of_possible_commands += ["tomita-mac"]
elif sys.platform.startswith("win"):
    list_of_possible_commands += ["tomita-win32"]
    def _findc(cmd):
        return os.system("where /q " + cmd) == 0
    findc = _findc

try:
    cmd = next(x for x in list_of_possible_commands if findc(x))
except StopIteration:
    print("Error: tomita parser not found!")
    exit(1)

dnrp = os.path.dirname(os.path.realpath(__file__))
mpath = os.path.join(dnrp, "..", "test", "data")

all_flag = False
normalize_flag = False
range_of_files = []
for i in sys.argv[1:]:
    if i[0] == '-':
        if i.find('a') != -1: all_flag = True
        if i.find('n') != -1: normalize_flag = True
    else: range_of_files.append(i)

def _ext(file):
    outname = os.path.join(mpath, "intermediate_output", os.path.splitext(os.path.basename(file))[0] + ".xml")
    if os.system(cmd + " " +\
        os.path.join("config", "config.proto") +\
        " <" + os.path.join(mpath, "input", file) +\
        " >" + outname) != 0:
        print("Error: failed while extracting file " + file + "!")
        exit(2)
    return outname
proc = _ext

if normalize_flag:
    def _proc(file):
        file = _ext(file)
        if os.system(sys.executable + " " + os.path.join(dnrp, "normalize.py") +\
            " " + file + " " + os.path.join(mpath, "normalized_output", os.path.basename(file))) != 0:
            print("Error: failed while normalizing file " + file + "!")
            exit(3)
    if not range_of_files:
        if all_flag: range_of_files = iglob(os.path.join(mpath, "input", "*.txt"))
        else:
            range_of_files = iglob(os.path.join(mpath, "intermediate_output", "*.xml"))
            def _2proc(file):
                if os.system("python " + os.path.join(dnrp, "normalize.py") +\
                    " " + file + " " + os.path.join(mpath, "normalized_output", os.path.splitext(os.path.basename(file))[0] + ".xml")) != 0:
                    print("Error: failed while normalizing file " + file + "!")
                    exit(3)
            _proc = _2proc
    proc = _proc
elif not range_of_files:
    if all_flag: range_of_files = iglob(os.path.join(mpath, "input", "*.txt"))
    else:
        print("Error: no files listed (nor used -a nor -n options)!")
        exit(4)


for f in range_of_files:
    proc(f)
