import functools

def no_none_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        if any(arg is None for arg in all_args):
            raise ValueError(f"None value detected in arguments to '{func.__name__}'")
        return func(*args, **kwargs)
    return wrapper
