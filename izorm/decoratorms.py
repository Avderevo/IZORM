
class classproperty(property):

    def __get__(self, instance, cls):
        return self.fget(cls)

