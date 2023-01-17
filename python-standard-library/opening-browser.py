import webbrowser
import time

# Open URL in default browser
url = "https://python.org"
webbrowser.open(url)

# Wait a bit before next operation
time.sleep(2)

# Open URL in a new window
webbrowser.open_new(url)

time.sleep(2)

# Open URL in a new tab
webbrowser.open_new_tab(url)

# Open multiple URLs
urls = [
    "https://docs.python.org",
    "https://pypi.org",
    "https://github.com/python"
]

for url in urls:
    webbrowser.open_new_tab(url)
    time.sleep(1)  # Wait a bit between openings

# Get the browser controller
controller = webbrowser.get()  # Get default browser
print(f"Default browser controller: {controller.name}")

try:
    # Try to use specific browsers (may not work if browser isn't installed)
    chrome = webbrowser.get('chrome')
    chrome.open_new_tab("https://python.org")
except webbrowser.Error:
    print("Chrome browser not found")

try:
    firefox = webbrowser.get('firefox')
    firefox.open_new_tab("https://python.org")
except webbrowser.Error:
    print("Firefox browser not found")

# Open local HTML file
try:
    webbrowser.open('file:///path/to/local/file.html')
except:
    print("Could not open local file")

# Open with specific URL parameters
search_url = "https://www.google.com/search?q=python+programming"
webbrowser.open(search_url) 