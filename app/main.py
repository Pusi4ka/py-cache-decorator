from typing import Callable, Any

store_data = {}
cache_data = {}


def cache(func: Callable) -> Callable:

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func, args, tuple(sorted(kwargs.items())))
        if key in store_data:
            print("Getting from cache")
            return store_data[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        store_data[key] = result
        return result

    return wrapper
