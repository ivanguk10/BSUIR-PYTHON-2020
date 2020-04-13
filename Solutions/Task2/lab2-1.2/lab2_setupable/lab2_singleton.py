class Singleton(type):

    _objects_ = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._objects_:
            cls._objects_[cls] = super().__call__(*args, **kwargs)
        return cls._objects_[cls]
