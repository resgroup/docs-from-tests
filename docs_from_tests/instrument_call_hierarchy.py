from typing import List
import functools
import types
import inspect
import pkgutil
import importlib
from docs_from_tests.call_hierarchy import CallHierarchy

_root_call = CallHierarchy('root', '')
_call_hierarchy_stack = [_root_call]
_wrapped_functions = dict()


def instrument_and_import_package(package_path, prefix):
    for (_, module_name, _) in pkgutil.iter_modules([package_path]):
        module = importlib.import_module(f"{prefix}.{module_name}")
        instrument_module(module)


# module_name is the same as an absolute import of it I think
def instrument_and_import_module(module_name): 
    module = importlib.import_module(module_name)
    instrument_module(module)
        

def instrument_module(module):
    #print(module.__name__)
    for function_name, function_object in vars(module).items():
        if isinstance(function_object, types.FunctionType):
            #print(function_name)
            vars(module)[function_name] = _document_function_calls(function_name, function_object)
    for class_name, class_object in inspect.getmembers(module):
            if inspect.isclass(class_object):
                if class_object.__module__ == module.__name__:
                    #print(class_name)
                    for method_name, method in inspect.getmembers(class_object):
                        if inspect.ismethod(method) or inspect.isfunction(method):
                            #print(f'{class_name}.{method_name}')
                            setattr(class_object, method_name, _document_function_calls(f'{class_name}.{method_name}', method))


def initialise_call_hierarchy(_root_call_name: str):
    global _root_call
    _root_call = CallHierarchy(_root_call_name, '')
    global _call_hierarchy_stack
    _call_hierarchy_stack = [_root_call]


def finalise_call_hierarchy() -> CallHierarchy:
    global _root_call
    return _root_call


def _document_function_calls(function_name, function_object):
    @functools.wraps(function_object)
    def wrapper(*args, **kwargs):
        return_annotation = inspect.signature(function_object).return_annotation
        if return_annotation == inspect.Signature.empty:
            return_value = ''
        elif return_annotation == None:
            return_value = ''
        else:
            try:
                return_value = return_annotation.__name__
            except AttributeError:
                return_value = str(return_annotation)

        global _call_hierarchy_stack
        parent_call_hierarchy = _call_hierarchy_stack[-1] # this is equivalent to peeking top value in a stack

        call_hierarchy = CallHierarchy(function_name, return_value)
        parent_call_hierarchy.add_called_function(call_hierarchy)
        _call_hierarchy_stack.append(call_hierarchy)

        result = function_object(*args, **kwargs)

        _call_hierarchy_stack.pop()

        return result

    if function_name in _wrapped_functions:
        return function_object
    else:
        _wrapped_functions[function_name] = function_object
        return wrapper


