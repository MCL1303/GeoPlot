import sys, os
from glob import iglob
from os.path import basename as bn, split as sp, dirname as dn, realpath as rp, join, splitext as spe

lst = ["tomitaparser"]
def findc(cmd):
    return os.system("command -v " + cmd) == 0
if sys.platform.startswith("linux"):
    lst += ["tomita-linux32", "tomita-linux64"]
elif sys.platform.startswith("freebsd"):
    lst += ["tomita-freebsd64"]
elif sys.platform.startswith("darwin"):
    lst += ["tomita-mac"]
elif sys.platform.startswith("win"):
    lst += ["tomita-win32"]
    def _findc(cmd):
        return os.system("where /q " + cmd) == 0
    findc = _findc

try:
    cmd = next(x for x in lst if findc(x))
except StopIteration:
    print("Error: tomita parser not found!")
    exit(1)

dnrp = dn(rp(__file__))
mpath = join(dnrp, "..", "test", "data")

mall = False
norm = False
mran = []
for i in sys.argv[1:]:
    if i[0] == '-':
        if i.find('a') != -1: mall = True
        if i.find('n') != -1: norm = True
    else: mran.append(i)

def _ext(file):
    outname = join(mpath, "intermediate_output", spe(bn(file))[0] + ".xml")
    if os.system(cmd + " " +\
        join("config", "config.proto") +\
        " <" + join(mpath, "input", file) +\
        " >" + outname) != 0:
        print("Error: failed while extracting file " + file + "!")
        exit(2)
    return outname
proc = _ext

if norm:
    def _proc(file):
        file = _ext(file)
        if os.system("python " + join(dnrp, "normalize.py") +\
            " " + file + " " + join(mpath, "normalized_output", bn(file))) != 0:
            print("Error: failed while normalizing file " + file + "!")
            exit(3)
    if not mran:
        if mall: mran = iglob(join(mpath, "input", "*.txt"))
        else:
            mran = iglob(join(mpath, "intermediate_output", "*.xml"))
            def _2proc(file):
                if os.system("python " + join(dnrp, "normalize.py") +\
                    " " + file + " " + join(mpath, "normalized_output", spe(bn(file))[0] + ".xml")) != 0:
                    print("Error: failed while normalizing file " + file + "!")
                    exit(3)
            _proc = _2proc
    proc = _proc
elif not mran:
    if mall: mran = iglob(join(mpath, "input", "*.txt"))
    else:
        print("Error: no files listed (nor used -a nor -n options)!")
        exit(4)


for f in mran:
    proc(f)
