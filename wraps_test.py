
#funtion을 데코레이션 @ 으로 받고 싶을때  
from functools import wraps

def without_wraps(func):
    def __wraper(*args, **kwargs):
        '''this is __warper'''
        return func(*args, **kwargs)
    return __wraper

@without_wraps
def func_1():
    '''this is Test!!!'''
    return "hello"

# words = without_wraps(func_1).__doc__
# print(words)

print(func_1.__doc__)
print(func_1.__name__)

#funtion을 데코레이션(@) 으로 받고 싶을때 로직
def with_wraps(func):
    @wraps(func)
    def __wraper(*args, **kwargs):
        '''this is __warper'''
        return func(*args, **kwargs)
    return __wraper

@with_wraps
def func_1():
    '''this is Test!!!'''
    return "hello"

print(func_1.__doc__)
print(func_1.__name__)

