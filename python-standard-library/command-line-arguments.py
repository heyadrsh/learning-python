import sys
import argparse
from pathlib import Path

# Basic argument handling with sys.argv
print("Arguments passed:", sys.argv)
print("Script name:", sys.argv[0])

if len(sys.argv) > 1:
    print("First argument:", sys.argv[1])

# Simple argument checking
def check_password():
    if len(sys.argv) != 2:
        print("Usage: python script.py <password>")
        sys.exit(1)
    
    password = sys.argv[1]
    if len(password) < 8:
        print("Password must be at least 8 characters long")
        sys.exit(1)
    
    print("Password is valid:", password)

# Advanced argument parsing with argparse
def process_files():
    parser = argparse.ArgumentParser(
        description='Process files with various options.',
        epilog='Example: script.py -i input.txt -o output.txt --verbose'
    )

    # Required arguments
    parser.add_argument('source', help='Source file to process')
    
    # Optional arguments
    parser.add_argument('-o', '--output', help='Output file (default: output.txt)',
                       default='output.txt')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Increase output verbosity')
    parser.add_argument('-n', '--number', type=int, default=10,
                       help='Number of lines to process (default: 10)')
    parser.add_argument('-m', '--mode', choices=['read', 'write', 'append'],
                       default='read', help='File operation mode')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Use the arguments
    if args.verbose:
        print(f"Processing {args.source}")
        print(f"Output will be written to {args.output}")
        print(f"Processing {args.number} lines in {args.mode} mode")
    
    # Check if source file exists
    if not Path(args.source).exists():
        parser.error(f"Source file {args.source} does not exist")

# Calculator example with argparse
def calculator():
    parser = argparse.ArgumentParser(description='Command line calculator')
    
    # Add arguments
    parser.add_argument('operation',
                       choices=['add', 'subtract', 'multiply', 'divide'],
                       help='Operation to perform')
    parser.add_argument('numbers', type=float, nargs='+',
                       help='Numbers to operate on')
    parser.add_argument('--round', type=int,
                       help='Round result to specified decimal places')
    
    args = parser.parse_args()
    
    # Perform calculation
    result = args.numbers[0]
    for num in args.numbers[1:]:
        if args.operation == 'add':
            result += num
        elif args.operation == 'subtract':
            result -= num
        elif args.operation == 'multiply':
            result *= num
        elif args.operation == 'divide':
            if num == 0:
                parser.error("Division by zero!")
            result /= num
    
    # Round if specified
    if args.round is not None:
        result = round(result, args.round)
    
    print(f"Result: {result}")

if __name__ == "__main__":
    # Uncomment the function you want to run
    # check_password()
    # process_files()
    # calculator()
    
    # Example command lines:
    # python script.py password123
    # python script.py input.txt -o output.txt --verbose
    # python script.py add 5 3 2 --round 2
    pass 