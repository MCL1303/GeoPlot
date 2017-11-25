class _geomobj:
    @classmethod
    def add(cls, identifier, *args):
        try:
            return cls.instances[identifier]
        except KeyError:
            obj = cls(identifier, *args)
            cls.instances[identifier] = obj
            return obj

    def draw(self, drawer):
        self.render(drawer)
        self.draw = lambda x: None

    @staticmethod
    def load(dictionary):
        raise NotImplementedError

    def render(self, drawer):
        raise NotImplementedError

    @classmethod
    def draw_all(cls, drawer):
        for i in cls.instances.values():
            i.draw(drawer)
