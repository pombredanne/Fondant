def import_object(class_path):
    components = class_path.split('.')
    module_path = '.'.join(components[:-1])
    mod = __import__(module_path, {}, {}, [])
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod
