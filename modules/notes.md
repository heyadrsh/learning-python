# Python Modules and Packages - Learning Notes

## Project Structure
```
modules/
├── example/
│   ├── app.py                  # Main application entry point
│   └── ecommerce/             # Ecommerce package
│       ├── __init__.py        # Makes ecommerce a package
│       ├── sales.py           # Sales-related functionality
│       └── shopping/          # Shopping-related subpackage
```

## Key Concepts

### 1. Modules
- A module is a file containing Python code
- Used to break down large programs into small manageable and organized files
- Can contain functions, classes, and variables
- Helps avoid naming conflicts through namespaces

### 2. Packages
- A package is a collection of Python modules
- Must contain an `__init__.py` file (can be empty)
- Provides a way to group related modules together
- Enables hierarchical structuring of modules

### 3. Project Components

#### Ecommerce Package (`example/ecommerce/`)
- **Purpose**: Handles e-commerce related functionality
- **Components**:
  - `sales.py`: Contains pricing calculations
    - `calc_tax()`: Calculates tax based on amount and rate
    - `calc_shipping()`: Calculates shipping cost based on weight
  - `shopping/`: Subpackage for shopping-related features

#### Main Application (`example/app.py`)
- Entry point for the application
- Imports and uses functionality from the ecommerce package

### 4. Best Practices
1. **Package Structure**
   - Use clear, descriptive names for modules and packages
   - Keep related functionality together
   - Use `__init__.py` to control package exports

2. **Imports**
   - Use absolute imports when possible
   - Follow the format: `from package.module import function`
   - Avoid circular imports

3. **Module Organization**
   - One class per module when possible
   - Group related functions together
   - Keep modules focused and single-purpose

### 5. Common Operations
```python
# Importing a module
import module_name

# Importing specific items
from module_name import function_name

# Importing with alias
import module_name as alias

# Importing from packages
from package.subpackage.module import function
```

### 6. Current Implementation
Our ecommerce package implements:
- Tax calculation with configurable tax rate
- Weight-based shipping cost calculation
- Modular structure for easy expansion

### 7. Future Enhancements
- Add inventory management
- Implement order processing
- Add user authentication
- Integrate payment processing

## Tips and Tricks
1. Use `dir()` to inspect module contents
2. Keep modules small and focused
3. Document using docstrings
4. Use relative imports for package-internal references
5. Follow PEP 8 naming conventions 