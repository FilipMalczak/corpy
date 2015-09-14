from collections import namedtuple
import os
import importlib

import corpy

#todo: add package-specific logging
#todo: os.walk has onerror, use it to conditionally log problems

CUT_RECURSION = object()

def visit_file(package, filename, callback, *callback_args, **callback_kwargs):
    if filename.endswith(".py"):
        modulename = filename[:-(len(".py"))]
        full_modulename =  package if modulename=="__init__" else package+"."+modulename
        imported = importlib.import_module(full_modulename)
        callback(imported, *callback_args, **callback_kwargs)

_entry = namedtuple("_entry", "dirpath dirnames filenames")

#def order_filenames(files):
#    files = list(files)
#    out = []
#    def move_forward(name):
#        if name in files:
#            out.append(name)
#            files.remove(name)
#    for to_handle in ["__init__.py", "__main__.py"]:
#        move_forward(to_handle)
#    out += files
#    return out

def pkg_name(current_dir, base_dir, base_pkg):
    rel = os.path.relpath(current_dir, base_dir)
    parts = [base_pkg] + list(rel.split(os.sep))
    assert not ".." in parts
    if "." in parts:
        parts.remove(".")
    return ".".join(parts)
#    while "/" in out:
#        out = out.replace("/", ".")
#    return out
        
def visit_package(package_name, callback, *callback_args, **callback_kwargs):
    package = importlib.import_module(package_name)
    pkg_init_file = package.__file__
    assert os.path.split(pkg_init_file)[1] == "__init__.py" #todo: exception
    package_dir = os.path.dirname(package.__file__)
    for _ in os.walk(package_dir):
        entry = _entry(*_)
        if not "__pycache__" in entry.dirpath.split(os.sep):
            current_pkg_name = pkg_name(entry.dirpath, package_dir, package_name)
            current_pkg = importlib.import_module(current_pkg_name)
            callback(current_pkg, *callback_args, **callback_kwargs)
            files = list(entry.filenames)
            if "__init__.py" in files:
                files.remove("__init__.py")
            if "__main__.py" in files:
                files.remove("__main__.py")
    #        files = order_filenames(entry.filenames)
            for filename in files:
                visit_file(current_pkg_name, filename, callback, *callback_args, **callback_kwargs)
        
