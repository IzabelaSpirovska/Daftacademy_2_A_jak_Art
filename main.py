#--- TASK 1 -----------------------------------------------------------

from functools import wraps
def wraps(*args, **kwargs):
    def wrap(to_be_decorated):
        def wrapper(*args, **kwargs):
            wrapper.__name__ = to_be_decorated.__name__
            wrapper.__module__ = to_be_decorated.__module__
            wrapper.__doc__ = to_be_decorated.__doc__
            wrapper.__qualname__ = to_be_decorated.__qualname__
            wrapper.__annotations__ = to_be_decorated.__annotations__
            return to_be_decorated(*args, **kwargs)
        return wrapper
    return wrap(*args)
 
@wraps
def example():
    """EXAMPLE"""
    return "PYTHON"
 
print(example())
 
assert example.__doc__ == """EXAMPLE"""

#--- TASK 2 -----------------------------------------------------------

def is_correct(*check):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            func_return = func()
            if type(func_return) != type(dict()):
                raise TypeError
 
            IsKeyInDecorArgs = True
            for key in check:
                if not key in func_return:
                    IsKeyInDecorArgs = False
            if IsKeyInDecorArgs == True:
                return func()
            else:
                return None
        return wrapper
    return real_decorator
 
if __name__ == "__main__":
 
    @is_correct('first_name', 'last_name','email')
    def get_data():
        return {'first_name': 'Jan',
                'last_name': 'Kowalski',
                'email': 'jan@kowalski.com'}
 

    @is_correct('first_name', 'last_name', 'email')
    def get_other_data():
        return {'first_name': 'Jan', 'email': 'jan@kowalski.com'}
 

    assert get_data() == {'first_name': 'Jan', 'last_name': 'Kowalski', 'email': 'jan@kowalski.com'}
    assert get_other_data() is None
    
#--- TASK 3 -----------------------------------------------------------

import datetime
 
def add_date(format):
    def decorator(func):
        def wrapper(*args, **kwargs):
            dic = dict(func(*args,**kwargs))
            dic['date']=datetime.datetime.now().strftime(format)
            return dic
        return wrapper
    return decorator
 
 
if __name__ == "__main__":
 
    @add_date('%B %Y')
    def get_data(a):
        return {1: a, 'name': 'Jan'}

 
    assert get_data(2) == {1: 2, 'name': 'Jan', 'date': 'April 2020'}
