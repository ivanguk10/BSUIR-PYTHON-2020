class Cache_results:
    """
    Class for caching previously calculated results.

    Class has methods to cache calculated results or return cached data.

    Attributes:
        _results_dict(dict): dict to save data
    """

    def __init__(self):
        """Constructor

        Constructor sets initial data.
        """
        self._results_dict = {}

    def __call__(self, func):
        """
            Cache decorator saves params into dictionary.

            Decorator for function's memoization
            Return value of function. If function with current arguments was invoked
            before, than returned cached value. Otherwise compute value of function.
            Args:
                func: function to decorate
            Returns:
                cached_decorator: decorated function
            """

        def cache_decorator(*args, **kwargs):

            memory_key = self.__to_hash(args, kwargs)

            if memory_key not in self._results_dict:

                result = func(*args, **kwargs)
                self.__update_key(memory_key, result)

            else:
                print('Your args and kwargs were in!')
                print(str(args) + str(kwargs))
            return self._results_dict[memory_key]

        return cache_decorator

    def __update_key(self, key, value):
        """
        The function updates cache dictionary.

        Arguments:
            key: Key to update cache dictionary.
            value: Value to update cache dictionary.
        """
        self._results_dict[key] = value

    @staticmethod
    def __to_hash(args, kwargs):
        """
        The function hashes args and kwargs.

        Arguments:
            args: The variable arguments are used for hashing.
            kwargs: The keyword arguments are used for hashing.

        Return:
            Hashed args and kwargs.
        """
        return hash(str(args) + str(kwargs))


@Cache_results()
def cat_potato(ho, str_):

    return ho + str_

