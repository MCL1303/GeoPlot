import sys
from os.path import basename as bn, splitext as sp, dirname as dn, realpath as rp, join

typesfilename = join(dn(rp(__file__)), "types.py")
with open(typesfilename) as tf:
    types = eval(tf.read())

# sys.argv[1] -- input file name
# sys.argv[2] -- output .proto file name
# sys.argv[3] (optional) -- output .py file name

f = open(sys.argv[1])
g = open(sys.argv[2], 'w')

name = sp(bn(f.name))[0]
g.write('import "base.proto";\nimport "facttypes_base.proto";\n\nmessage ' + name + ' : NFactType.TFact {\n')

pywrite = lambda x: None
pyclose = lambda: None
regex = None
if len(sys.argv) > 3:
    h = open(sys.argv[3], "w")
    pywrite = lambda x: h.write(x)
    pyclose = lambda: h.close()
    h.write("import Geometry\nimport re\n\nclass " + name + ":\n    def __init__(self, el):")

k = 1
for i in f:
    rtype = [] # read type
    wtype = False # wait for type
    braces = False
    cmds = i.split()
    j = 0
    while j < len(cmds):
        if cmds[j] == "&":
            if wtype: raise Exception("Type expected!" if j == 0 else ("Expected type after '" + cmds[j - 1] + "'!"))
            elif braces: raise Exception("Unexpected & in braces!")
            wtype = True
        elif cmds[j] == "(":
            if wtype: raise Exception("Type expected, not '('!")
            braces = True
        elif cmds[j].startswith('('):
            if wtype: raise Exception("Type expected, not '('!")
            cmds[j] = cmds[j][1:]
            braces = True
            continue
        elif cmds[j] == ")":
            if not braces: raise Exception("Close braces before open!")
            braces = False
        elif cmds[j].endswith(')'):
            if not braces: raise Exception("Close braces before open!")
            rtype[-1][1].append(cmds[j][0:-1])
            braces = False
        elif braces:
            rtype[-1][1].append(cmds[j])
        elif cmds[j] in types:
            rtype.append([cmds[j], []]) # [] -- addons
            wtype = False
        else: break
        j += 1

    g.write('    optional ')

    method = None
    # type of field
    if len(rtype) == 1:
        if rtype[0][0] == 'float':
            g.write("string /* " + rtype[0][1][0] + ' */ ')
            method = "\n        self." + rtype[0][1][0] + " = float(el.find('{}').get('val'))"
        else:
            g.write(rtype[0][0] + ' /* ' + rtype[0][1][0] + ' */ ')
            method = "\n        self." + rtype[0][1][0]
            if rtype[0][0] == "string":
                method += " = el.find('{}').get('val')"
                if len(rtype[0][1]) > 1:
                    regex = rtype[0][1][1].strip('/')
                    if regex != rtype[0][1][1][1:-1]: regex = None
            else:
                method += " = bool(el.find('{}').get('val').capitalize())"
    else:
        g.write('string /* ' + ' and '.join(i[0] for i in rtype) + ' */ ')
        method = "\n        " + ', '.join("self.{}".format(i[1][0]) for i in rtype) +\
            " = re.match('" + "".join("(' + {} + ')".format("Geometry." + i[0] + ".regex") for i in rtype) +\
            "', el.find('{}').get('val')).group(" + ", ".join(str(i) for i in range(1, len(rtype) + 1)) +\
            ")\n        Geometry.addpoints(" + ', '.join("self.{}".format(i[1][0]) for i in rtype) + ")"
    pywrite(method.format(cmds[j]))

    g.write(cmds[j] + ' = ' + str(k)) # name and pos of field
    j += 1

    if j < len(cmds) and cmds[j] == '=':
        j += 1
        g.write(' [ default = ' + cmds[j] + ' ]')

    g.write(';\n')
    k += 1

g.writelines('}\n')
f.close()
g.close()

if regex is not None:
    pywrite('\n\n    regex = "' + regex + '"')
pywrite('\n')
pyclose()

types.add(name)
with open(typesfilename, 'w') as tf:
    tf.write(repr(types))

if name.istitle():
    with open('facttypes.proto', 'r+') as f:
        myline = "import \"" + bn(g.name) + "\";\n"
        for line in f:
            if line == myline:
                myline = None
                break
        if myline is not None: f.write()
