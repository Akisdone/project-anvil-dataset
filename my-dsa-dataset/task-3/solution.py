def get_deep_value(data, path, default=None):
    if not path:
        return default
    
    keys = path.split('.')
    current = data
    
    try:
        for key in keys:
            # Check if we are dealing with a list index
            if isinstance(current, list) and key.isdigit():
                current = current[int(key)]
            else:
                current = current[key]
        return current
    except (KeyError, IndexError, TypeError, AttributeError):
        return default