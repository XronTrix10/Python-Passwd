import shutil, os

# source_dir = os.getcwd()
source_dir = os.path.dirname(os.path.realpath(__file__))
destination_dir = r"C:\Program Files\Python-Passwd"


source_dir = os.path.join(source_dir, "scripts")
print(source_dir)


# shutil.copytree(source_dir, destination_dir)

# shutil.copytree(source_dir, destination_dir, symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=False)

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)


# install_and_import('cryptography')