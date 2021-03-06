from glob import iglob
from os.path import realpath, dirname, join, basename, splitext

__all__ = [
    splitext(i)[0] for i in map(
        basename,
        iglob(join(dirname(realpath(__file__)), '*.py'))
    )
    if not i.startswith('_')
]
__all__ += ["classes", "resolve_all", "as_json"]

__classes = None


def classes():
    global __classes
    if __classes is not None:
        return __classes
    __classes = {i.__name__: i for i in _geomobj._geomobj.__subclasses__()}
    return __classes


def as_json(obj):
    if isinstance(obj, frozenset):
        return list(obj)
    elif isinstance(obj, type):
        return obj.static_as_json()
    return obj.as_json()


def resolve_all():
    for k, cls in sorted(classes().items()):
        cls.resolve()
