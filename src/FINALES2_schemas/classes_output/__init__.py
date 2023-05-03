from importlib import import_module
from pathlib import Path
from glob import glob

parent_path = Path(__file__).parent

# Getting the path required for the import of the modules dynamically for more flexibility
package_path = []
path = Path(__file__)
while path.parent.name != "src":
    package_path.append(path.parent.name)
    path = Path(path.parent)
package_path = list(reversed(package_path))

for dir in glob(f"{parent_path}/*"):
    if Path(dir).is_dir():
        import_module(f".{Path(dir).name}", package=".".join(package_path))