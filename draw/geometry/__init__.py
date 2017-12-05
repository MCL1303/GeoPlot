from glob import iglob
from os.path import realpath, dirname, join, basename, splitext

__all__ = [
    splitext(basename(i))[0] for i in
    iglob(join(dirname(realpath(__file__)), '*.py'))
    if not i.startswith('_')
]
__all__ += ["classes", "draw_all"]

__classes = None


def classes():
    global __classes
    if __classes is not None:
        return __classes
    __classes = {i.__name__: i for i in _geomobj._geomobj.__subclasses__()}
    return __classes


def draw_all(drawer):
    for cls in _geomobj._geomobj.__subclasses__():
        cls.draw_all(drawer)
