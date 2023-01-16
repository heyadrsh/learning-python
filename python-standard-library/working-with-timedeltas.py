from datetime import datetime, timedelta

dt1 = datetime(2023, 1, 16)
dt2 = datetime.now()

duration = dt2 - dt1
print(f"Duration: {duration}")
print(f"Days: {duration.days}")
print(f"Seconds: {duration.seconds}")
print(f"Total seconds: {duration.total_seconds()}")

dt3 = dt1 + timedelta(days=1, seconds=1000)
print(f"dt3: {dt3}")

dt4 = dt1 + timedelta(weeks=1)
print(f"dt4: {dt4}")

dt5 = datetime.now() + timedelta(days=1, minutes=5)
print(f"dt5: {dt5}")

dt6 = datetime.now() - timedelta(days=1, hours=2, minutes=30)
print(f"dt6: {dt6}")

duration = timedelta(days=2, hours=3)
print(f"Duration in seconds: {duration.total_seconds()}") 