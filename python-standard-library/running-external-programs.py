import subprocess
import sys
import time

# Simple command execution
print("Running 'dir' command:")
try:
    # Using shell=True for Windows commands
    completed = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
    print("Return code:", completed.returncode)
    print("Output:", completed.stdout)
    print("Errors:", completed.stderr)
except subprocess.CalledProcessError as e:
    print("Error running command:", e)

# Running Python script
print("\nRunning Python script:")
try:
    result = subprocess.run(
        ["python", "-c", "print('Hello from subprocess!')"],
        capture_output=True,
        text=True
    )
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Error:", e)

# Running command with input
print("\nRunning command with input:")
process = subprocess.Popen(
    ["python", "-c", "name = input('Enter name: '); print(f'Hello, {name}!')"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)
stdout, stderr = process.communicate("Alice\n")
print("Output:", stdout)

# Running command with timeout
print("\nRunning command with timeout:")
try:
    result = subprocess.run(
        ["ping", "google.com"],
        timeout=5,
        capture_output=True,
        text=True
    )
    print(result.stdout)
except subprocess.TimeoutExpired:
    print("Command timed out")

# Running multiple commands
print("\nRunning multiple commands:")
commands = [
    "echo First command",
    "echo Second command",
    "echo Third command"
]

for cmd in commands:
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(f"Command '{cmd}' output:", result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error running '{cmd}':", e)

# Running background process
print("\nRunning background process:")
process = subprocess.Popen(
    ["python", "-c", "import time; time.sleep(2); print('Background process completed')"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

print("Main program continues while background process runs...")
time.sleep(1)
print("Doing other work...")
time.sleep(1)

# Wait for background process to complete
stdout, stderr = process.communicate()
print("Background process output:", stdout)

# Running command and checking status
print("\nChecking command status:")
result = subprocess.run(["echo", "Hello World"], capture_output=True, text=True)
if result.returncode == 0:
    print("Command succeeded:", result.stdout)
else:
    print("Command failed:", result.stderr)

# Environment variables
print("\nRunning command with environment variables:")
try:
    result = subprocess.run(
        ["python", "-c", "import os; print(os.environ.get('TEST_VAR'))"],
        env={"TEST_VAR": "Hello from Python!"},
        capture_output=True,
        text=True
    )
    print("Output:", result.stdout)
except subprocess.CalledProcessError as e:
    print("Error:", e)

# Running shell commands safely
def run_command_safely(command, timeout=None):
    """Run a command safely and return the output."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        if result.returncode == 0:
            return True, result.stdout
        else:
            return False, result.stderr
    except subprocess.TimeoutExpired:
        return False, "Command timed out"
    except Exception as e:
        return False, str(e)

# Example usage of safe command execution
commands_to_try = [
    "echo Success!",
    "invalid_command",
    "python -c 'print(\"Python says hello!\")'",
]

print("\nTrying various commands safely:")
for cmd in commands_to_try:
    success, output = run_command_safely(cmd)
    print(f"\nCommand: {cmd}")
    print(f"Success: {success}")
    print(f"Output: {output}") 