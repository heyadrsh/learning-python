import time

# Get current timestamp (seconds since epoch)
print("Current timestamp:", time.time())

# Measure execution time
def send_emails():
    for i in range(1000000):
        pass

start = time.time()
send_emails()
end = time.time()
duration = end - start
print(f"Duration: {duration} seconds")

# Sleep for 3 seconds
print("Starting sleep...")
time.sleep(3)
print("Finished sleeping")

# Convert timestamp to string
current_time = time.time()
time_string = time.ctime(current_time)
print("Current time:", time_string)

# Get structured time
local_time = time.localtime()
print("\nLocal time attributes:")
print("Year:", local_time.tm_year)
print("Month:", local_time.tm_mon)
print("Day:", local_time.tm_mday)
print("Hour:", local_time.tm_hour)
print("Minute:", local_time.tm_min)
print("Second:", local_time.tm_sec)
print("Weekday:", local_time.tm_wday)  # 0 is Monday
print("Year day:", local_time.tm_yday)  # 1 is January 1st
print("DST:", local_time.tm_isdst)  # Daylight Saving Time

# Format time string
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("\nFormatted time:", formatted_time)

# Parse time string
time_string = "2023-01-17 15:30:00"
parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print("Parsed time:", parsed_time)

# Get process time (CPU time)
cpu_start = time.process_time()
send_emails()
cpu_end = time.process_time()
print(f"\nCPU time used: {cpu_end - cpu_start} seconds") 