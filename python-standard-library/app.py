from pathlib import Path
from time import ctime

# Get the current file's directory
current_dir = Path(__file__).parent

# Example 1: Working with paths
print("\n1. Basic Path Operations:")
path = current_dir / "ecommerce" / "__init__.py"
print(f"Exists: {path.exists()}")
print(f"Is File: {path.is_file()}")
print(f"Is Directory: {path.is_dir()}")
print(f"Name: {path.name}")
print(f"Stem: {path.stem}")
print(f"Suffix: {path.suffix}")
print(f"Parent: {path.parent}")

# Example 2: Directory operations
print("\n2. Directory Operations:")
dir_path = current_dir / "ecommerce"
print(f"Directory exists: {dir_path.exists()}")
print(f"Directory contents:")
for item in dir_path.iterdir():
    print(f"  - {item.name}")

# Example 3: Path modifications
print("\n3. Path Modifications:")
modified_path = path.with_suffix(".txt")
print(f"Original: {path}")
print(f"Modified: {modified_path}")

# Example 4: File stats
print("\n4. File Statistics:")
if path.exists():
    stats = path.stat()
    print(f"Size: {stats.st_size} bytes")
    print(f"Last modified: {ctime(stats.st_mtime)}")
    print(f"Created: {ctime(stats.st_ctime)}")

# Example 5: Additional Path Operations
print("\n5. Additional Path Operations:")
# Create a new directory
new_dir = current_dir / "test_dir"
if not new_dir.exists():
    new_dir.mkdir()
    print(f"Created directory: {new_dir}")

# List all Python files in a directory
print("\nPython files in directory:")
for py_file in dir_path.glob("*.py"):
    print(f"  - {py_file.name}")

# Get absolute path
print(f"\nAbsolute path: {path.absolute()}")

# Get home directory
print(f"Home directory: {Path.home()}")

# Reading and writing files
print("\nFile contents:")
print(path.read_text())
path.write_text("# This is a test file for path operations\nprint('Ecommerce package initialized')\n") 