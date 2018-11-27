from time import ctime

print('***Welcome to MetaClasses!***')
print('\tMetaClass declaration first!')


class MetaC(type):
    def __init__(cls, name, bases, attrd):
        super(MetaC, cls).__init__(name, bases, attrd)
        print('***Created class %r at : %s***' %(name, ctime()))

    def __new__(cls, name, bases, attrs):
        print('***__new__ Created class %r at : %s***' % (name, ctime()))
        return type.__new__(cls, name, bases, attrs)
print('\tClass "Foo" declaration next.')


class Foo(object, metaclass=MetaC):
    #__metaclass__ = MetaC

    def __init__(self):
        print('*** Instantiated class %r at : %s ***' %(self.__class__.__name__, ctime()))


print('\tClass "Foo"  instantiation next.')
f = Foo()
print(dir(f))
print('\tDone')
