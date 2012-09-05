class DictWithMagicProperties(dict):
    """dict object which keys can be accessed as properties"""

    def __getattribute__(self, attribute):
        try:
            v = super(DictWithMagicProperties, self).__getattribute__(attribute)
            return v
        except AttributeError:
            return self.__getitem__(attribute)


class TwoWayDict(dict):

    def __setitem__(self, key, value):
        super(TwoWayDict, self).__setitem__(key, value)
        super(TwoWayDict, self).__setitem__(value, key)


class ReversibleDict(dict):

    def reverse(self):
        d = dict()
        for k, v in self.iteritems():
            d[v] = k
        return d


class DictList(dict):

    def __setitem__(self, key, value):
        try:
            l = self[key]
        except:
            l = []
            super(DictList, self).__setitem__(key, l)
        finally:
            l.append(value)
