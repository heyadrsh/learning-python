# Python Standard Library Notes

## Working with Files and Data

### CSV Files
- Use `csv` module for reading/writing CSV files
- `csv.reader()` and `csv.writer()` for basic operations
- `csv.DictReader()` and `csv.DictWriter()` for dictionary-based operations
- Always use `newline=''` when opening files for writing

### JSON Files
- `json` module for JSON operations
- `json.dumps()` converts Python to JSON string
- `json.loads()` parses JSON string to Python
- `json.dump()` writes to file
- `json.load()` reads from file
- Supports basic Python types: dict, list, str, int, float, bool, None

### SQLite Database
- Built-in SQL database with `sqlite3` module
- Connection management with context managers
- Supports parameterized queries for safety
- Basic operations: CREATE, INSERT, SELECT, UPDATE, DELETE
- Use cursor for executing queries and fetching results

## Time and Date Operations

### Timestamps
- `time` module for time-related operations
- `time.time()` for Unix timestamp
- `time.ctime()` for readable time string
- `time.sleep()` for pausing execution
- Performance measurement with `time.time()`

### DateTime Objects
- `datetime` module for date and time manipulation
- `datetime.now()` for current date/time
- `datetime.strptime()` for parsing strings
- `datetime.strftime()` for formatting
- Access individual components (year, month, day, etc.)

### Time Deltas
- `timedelta` for duration calculations
- Add/subtract from datetime objects
- Get days, seconds, microseconds
- Calculate time differences
- Useful for date arithmetic

## Utility Functions

### Random Values
- `random` module for random number generation
- `random.random()` for float between 0 and 1
- `random.randint()` for integers
- `random.choice()` for sequence selection
- `random.shuffle()` for list randomization

### Browser Operations
- `webbrowser` module for browser control
- Open URLs in default browser
- Open in new window or tab
- Simple way to launch web pages

### Email Operations
- `email` package for email composition
- `smtplib` for sending emails
- Support for attachments
- MIME message composition
- SSL/TLS support

### Templates
- `string.Template` for simple templating
- Safe substitution of variables
- Dollar-sign notation
- Support for dictionaries
- Error handling with safe_substitute

### Command Line
- `sys.argv` for basic argument access
- `argparse` for advanced argument parsing
- Help message generation
- Type conversion
- Optional and positional arguments

### External Programs
- `subprocess` module for external commands
- Capture output and errors
- Handle return codes
- Shell command execution
- Error handling with CalledProcessError

## Best Practices
1. Always use context managers with files
2. Handle exceptions appropriately
3. Use parameterized queries with SQLite
4. Be careful with time zones in datetime
5. Use secure methods for sensitive operations
6. Validate command line inputs
7. Check return codes from external programs

## Common Patterns
1. File processing with context managers
2. Database operations with connections
3. Time calculations with timedelta
4. Command line interface with argparse
5. Template-based text processing
6. External program execution with error handling

## Security Considerations
1. SQL injection prevention
2. Safe file handling
3. Secure email credentials
4. Input validation
5. Safe external program execution
6. Template escape handling

Remember: The Python Standard Library provides a rich set of tools for common programming tasks. Understanding these modules helps write more efficient and maintainable code. 