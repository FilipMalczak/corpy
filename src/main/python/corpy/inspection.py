def get_dict(obj):
    if hasattr(obj, "__slots__"):
        out = {}
        for k in obj.__slots__:
            try:
                out[k] = getattr(obj, k)
            except AttributeError:
                out[k] = None
        return out
    return dict(obj.__dict__)

def isoftype(obj, class_or_tuple):
    if isinstance(class_or_tuple, tuple):
        return any(map(lambda x: isoftype(obj, x), class_or_tuple))
    return type(obj) == class_or_tuple

def search_dict_for_class(obj, class_or_tuple, include_subclasses=True):
    checker = (lambda x: isinstance(x, class_or_tuple)) if include_subclasses else (lambda x: isoftype(x, class_or_tuple))
    return { k: v for k, v in get_dict(obj).items() if checker(v) }
