#!/usr/bin/python
# -*- coding: utf-8 -*-

import humanfriendly

class IECUnit(object):
    def __init__(self, value):
        if isinstance(value, str):
            self.value = humanfriendly.parse_size(value, binary=True)
        elif isinstance(value, (int, float)):
            self.value = value
        else:
            raise TypeError()

    def __str__(self):
        return humanfriendly.format_size(self.value, binary=True)

    def __cmp__(self, other):
        if isinstance(other, IECUnit):
            return self.value - other.value
        else:
            return self.value - other

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __ge__(self, other):
        return self > other or self == other

    def __add__(self, other):
        if not isinstance(other, IECUnit):
            other = IECUnit(other)
        return IECUnit(self.value + other.value)

    def __sub__(self, other):
        if not isinstance(other, IECUnit):
            other = IECUnit(other)
        return IECUnit(self.value - other.value)

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError()
        return IECUnit(self.value * other)

    def __div__(self, other):
        if not isinstance(other, (int, float)):
            raise TypeError()
        return IECUnit(self.value / other)
    
    def __truediv__(self, other):
        return self.__div__(other)

class Bandwidth(IECUnit):
    pass

class Size(IECUnit):
    pass

class VolumeSize(IECUnit):
    pass

def main():
    print(Bandwidth('10M') * 1024)
    print(Bandwidth('100M') < Bandwidth('1G'))
    print(Bandwidth('10M') + Bandwidth('10M'))
    print(Bandwidth('30M') / 2)

if __name__ == '__main__':
    main()
