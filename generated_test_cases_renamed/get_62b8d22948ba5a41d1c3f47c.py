from collections.abc import MutableMapping


class _DefaultSize(object):

    __slots__ = ()

    def __getitem__(self, _):
        return 1

    def __setitem__(self, _, value):
        assert value == 1

    def pop(self, _):
        return 1


class Cache(MutableMapping):
    """Mutable mapping to serve as a simple cache or cache base class."""

    __marker = object()

    __size = _DefaultSize()

    def __init__(self, maxsize, getsizeof=None):
        if getsizeof:
            self.getsizeof = getsizeof
        if self.getsizeof is not Cache.getsizeof:
            self.__size = dict()
        self.__data = dict()
        self.__currsize = 0
        self.__maxsize = maxsize

    def __repr__(self):
        return '%s(%r, maxsize=%r, currsize=%r)' % (
            self.__class__.__name__,
            list(self.__data.items()),
            self.__maxsize,
            self.__currsize,
        )

    def __getitem__(self, key):
        try:
            return self.__data[key]
        except KeyError:
            return self.__missing__(key)

    def __setitem__(self, key, value):
        maxsize = self.__maxsize
        size = self.getsizeof(value)
        if size > maxsize:
            raise ValueError('value too large')
        if key not in self.__data or self.__size[key] < size:
            while self.__currsize + size > maxsize:
                self.popitem()
        if key in self.__data:
            diffsize = size - self.__size[key]
        else:
            diffsize = size
        self.__data[key] = value
        self.__size[key] = size
        self.__currsize += diffsize

    def __delitem__(self, key):
        size = self.__size.pop(key)
        del self.__data[key]
        self.__currsize -= size

    def __contains__(self, key):
        return key in self.__data

    def __missing__(self, key):
        raise KeyError(key)

    def __iter__(self):
        return iter(self.__data)

    def __len__(self):
        return len(self.__data)

<insert generated code here>

    def pop(self, key, default=__marker):
        if key in self:
            value = self[key]
            del self[key]
        elif default is self.__marker:
            raise KeyError(key)
        else:
            value = default
        return value

    def setdefault(self, key, default=None):
        if key in self:
            value = self[key]
        else:
            self[key] = value = default
        return value

    @property
    def maxsize(self):
        """The maximum size of the cache."""
        return self.__maxsize

    @property
    def currsize(self):
        """The current size of the cache."""
        return self.__currsize

    @staticmethod
    def getsizeof(value):
        """Return the size of a cache element's value."""
        return 1

if __name__ == "__main__":
    isT = True
    test_cases = dict()
    try:

        cache=Cache(10000)
        cache.__setitem__(4, 10)
        cache.__setitem__(5, "five")
        cache.__setitem__(6, 600)
        try:
            test_cases['test1']=cache.get(4,None)
        except Exception as error:
            test_cases['test1'] = type(error).__name__
        try:
            test_cases['test2']=cache.get(5, None)
        except Exception as error:
            test_cases['test2'] = type(error).__name__
        try:
            test_cases['test3']=cache.get(5, 25)
        except Exception as error:
            test_cases['test3'] = type(error).__name__
        try:
            test_cases['test4']=cache.get(6, 10)
        except Exception as error:
            test_cases['test4'] = type(error).__name__
        try:
            test_cases['test5']=cache.get(7, 11)
        except Exception as error:
            test_cases['test5'] = type(error).__name__
        try:
            test_cases['test6']=cache.get(8, 20)
        except Exception as error:
            test_cases['test6'] = type(error).__name__

        print(test_cases)
    except Exception as error:
        print(test_cases)

    # for l in os.listdir(
    #         "C:\\Users\yh199\Downloads\\repos1\\repos\pexip---os-python-cachetools\\data_passk_platform1/62b8d22948ba5a41d1c3f47c/"):
    #     f = open(
    #         "C:\\Users\yh199\Downloads\\repos1\\repos\pexip---os-python-cachetools/data_passk_platform1/62b8d22948ba5a41d1c3f47c/" + l,
    #         "rb")
    #     content = dill.load(f)
    #     f.close()
    #     if isinstance(content["input"]["args"][1]["bytes"], bytes):
    #         args1 = dill.loads(content["input"]["args"][1]["bytes"])
    #     else:
    #         args1 = content["input"]["args"][1]["bytes"]
    #     if isinstance(content["input"]["args"][2]["bytes"], bytes):
    #         args2 = dill.loads(content["input"]["args"][2]["bytes"])
    #     else:
    #         args2 = content["input"]["args"][2]["bytes"]
    #     print(args1)
    #     print(args2)
    #     print("---------")
    #     # object_class = dill.loads(content["input"]["args"][0]["bytes"])
    #     # temp_class = Cache(10000)
    #     # temp_class.__dict__.update(object_class)
    #     # res0 = temp_class.get(args1, args2)
    #     # if not ( dill.dumps(res0)== dill.dumps(content["output"][0])):
    #     #     isT=False
    #     #     break




