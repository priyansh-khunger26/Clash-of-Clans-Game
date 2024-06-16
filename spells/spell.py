class Spell:
    def __init__(self, duration):
        self.duration = duration
        self.active = False

    def apply(self, troop):
        raise NotImplementedError("This method should be overridden by subclasses")

    def remove(self, troop):
        raise NotImplementedError("This method should be overridden by subclasses")