import time

print(time.time())

def send_emails():
    for i in range(10000):
        pass

start = time.time()
send_emails()
end = time.time()
duration = end - start
print(f"Duration: {duration}")

time.sleep(1)

print(time.ctime())

print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

time_string = "2023-01-16"
time_object = time.strptime(time_string, "%Y-%m-%d")
print(time_object) 