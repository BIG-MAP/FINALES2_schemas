from importlib import import_module
from pathlib import Path
from glob import glob

parent_path = Path(__file__).parent

# Getting the path required for the import of the modules dynamically for more flexibility
# and to avoid errors due to a lack of manual maintenance of this file

# The path relative to which the packages shall be imported, needs to be assembled
package_path = []
path = Path(__file__)
# Starting from the parent of this __init__.py file, this searches the parents until it
# reaches the level below src, from where the modules can be imported. Each level is
# added to the package path, which is used for the import
while path.parent.name != "src":
    package_path.append(path.parent.name)
    path = Path(path.parent)
# The sequence of the levels needs to be inverted to obtain a valid path starting from
# the FINALES2 level
package_path = list(reversed(package_path))

# This iterates over all the directories within the parent directory of this __init__.py
# file and imports the modules.
for dir in glob(f"{parent_path}/*"):
    if Path(dir).is_dir():
        import_module(f".{Path(dir).name}", package=".".join(package_path))