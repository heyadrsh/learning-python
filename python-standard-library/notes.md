# Python Standard Library Notes

## Working with Files and Data

### CSV Files (csv module)
- Reading and writing CSV files
- Using `csv.reader` and `csv.writer`
- Using `DictReader` and `DictWriter` for named columns
- Handling different delimiters and formats
- Best practices for CSV file handling

### JSON Files (json module)
- Converting Python objects to JSON strings
- Reading and writing JSON files
- Pretty printing JSON data
- Custom JSON encoders and decoders
- Handling complex data types
- Error handling in JSON operations

### SQLite Database (sqlite3 module)
- Creating and connecting to databases
- Creating tables and defining schemas
- CRUD operations (Create, Read, Update, Delete)
- Using parameterized queries for safety
- Transaction management
- Error handling and best practices
- Common SQLite operations

## Time and Date Operations

### Timestamps (time module)
- Getting current timestamp
- Converting between timestamps and strings
- Measuring execution time
- Sleep operations
- Time formatting and parsing
- Process time vs wall time

### DateTime Objects (datetime module)
- Creating datetime objects
- Accessing datetime components
- Converting between formats
- Formatting datetime strings
- Working with dates only
- Working with times only
- Timezone considerations

### Time Deltas (timedelta)
- Creating time intervals
- Adding/subtracting time
- Calculating time differences
- Working with days, hours, minutes, seconds
- Complex time calculations
- Best practices for time manipulation

## Utility Functions

### Random Values (random module)
- Generating random numbers
- Random selections from sequences
- Shuffling sequences
- Working with probability distributions
- Seeding for reproducibility
- Cryptographic vs pseudo-random numbers

### Browser Operations (webbrowser module)
- Opening URLs in browser
- Controlling browser behavior
- Opening new windows/tabs
- Browser selection
- Error handling
- Platform-specific considerations

### Email Operations (smtplib, email modules)
- Sending simple emails
- HTML emails
- Email attachments
- SMTP configuration
- Security considerations
- Error handling
- Best practices for email handling

### Templates (string.Template)
- Basic string templates
- Safe substitution
- Custom delimiters
- Working with dictionaries
- HTML templates
- Email templates
- Best practices for template usage

### Command Line Arguments (sys.argv, argparse)
- Basic argument handling with sys.argv
- Advanced argument parsing with argparse
- Required vs optional arguments
- Argument types and validation
- Help message generation
- Subcommands and complex CLIs
- Best practices for CLI design

### Running External Programs (subprocess)
- Running system commands
- Capturing output and errors
- Working with pipes
- Process management
- Timeout handling
- Security considerations
- Cross-platform compatibility

## Best Practices

1. File Operations
   - Always use context managers (with statements)
   - Handle encoding explicitly
   - Implement proper error handling
   - Clean up resources properly

2. Data Handling
   - Validate data before processing
   - Use appropriate data types
   - Implement proper error checking
   - Handle edge cases

3. Time and Date
   - Use appropriate time zones
   - Handle DST transitions
   - Use ISO format when possible
   - Consider international date formats

4. Security
   - Never trust user input
   - Use parameterized queries
   - Handle sensitive data properly
   - Implement proper access controls

5. Error Handling
   - Use specific exceptions
   - Implement proper logging
   - Provide meaningful error messages
   - Clean up resources in error cases

## Common Patterns

1. File Processing
   ```python
   with open('file.txt') as f:
       for line in f:
           process(line)
   ```

2. Database Operations
   ```python
   with sqlite3.connect('db.sqlite3') as conn:
       try:
           conn.execute('INSERT INTO ...')
           conn.commit()
       except sqlite3.Error:
           conn.rollback()
   ```

3. Time Calculations
   ```python
   start = time.time()
   process()
   duration = time.time() - start
   ```

## Security Considerations

1. File Operations
   - Validate file paths
   - Check file permissions
   - Handle temporary files securely

2. Database
   - Use parameterized queries
   - Implement proper access control
   - Secure connection strings

3. External Programs
   - Validate command inputs
   - Handle output securely
   - Consider security implications

4. Network Operations
   - Use secure protocols
   - Validate certificates
   - Handle sensitive data properly

## Additional Resources

1. Official Documentation
   - [Python Standard Library](https://docs.python.org/3/library/)
   - [Python Tutorial](https://docs.python.org/3/tutorial/)

2. Best Practices
   - [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
   - [Python Packaging Guide](https://packaging.python.org/) 