from os.path import dirname as dn, realpath as rp, join
from os import getcwd, chdir

cname = dn(rp(__file__))
typesfilename = join(cname, "..", "compile", "types.py")

with open(typesfilename) as tf:
    types = eval(tf.read())

__all__ = [i for i in types if i.istitle()]
