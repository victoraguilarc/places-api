import importlib


def recover_class(module_name: str, class_name: str):
    module = importlib.import_module(module_name)
    return getattr(module, class_name)
