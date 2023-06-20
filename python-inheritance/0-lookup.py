#!/usr/bin/python3
def lookup(obj):
    attrs = []
    methods = []
    for name in dir(obj):
        if not name.startswith('__'):
            attr = getattr(obj, name)
            if callable(attr):
                methods.append(name)
            else:
                attrs.append(name)
    return attrs + methods
