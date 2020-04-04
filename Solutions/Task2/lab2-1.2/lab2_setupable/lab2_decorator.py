class CacheDecorator:

    _func_values_ = dict()

    def cache(function):
        def wrapper(*args, **kwargs):
            if CacheDecorator._func_values_.get(function.__name__):
                if CacheDecorator._func_values_[function.__name__][0] == args and \
                        CacheDecorator._func_values_[function.__name__][1] == kwargs:
                    print("Decorator works!")
                    return CacheDecorator._func_values_[function.__name__][2]
            result = function(*args, **kwargs)
            CacheDecorator._func_values_[function.__name__] = (args, kwargs, result)
            return result
        return wrapper

