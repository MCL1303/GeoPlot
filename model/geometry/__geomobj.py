class __geomobj:
    @classmethod
    def add(cls, identifier=None, *args):
        if identifier is not None:
            if identifier in cls.instances:
                return cls.instances[identifier].update(*args)
            else:
                obj = cls(identifier, *args)
                cls.instances[identifier] = obj
                return obj
        else:
            obj = cls(identifier, *args)
            cls.unnamed_instances.append(obj)
            return obj

    def __init__(self):
        self.__resolved = False

    def update(self):
        pass

    def resolve_one(self):
        if not self.__resolved:
            self.proceed()
            self.__resolved = True

    @classmethod
    def resolve(cls):
        for i in list(cls.instances.values()):
            i.resolve_one()
        for i in cls.unnamed_instances:
            i.resolve_one()
