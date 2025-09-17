import time

sec = time.time()

hours = int(sec // 3600)
minutes = int((sec % 3600) // 60)

print("Time since epoch:")
print(hours, "hours and", minutes, "minutes")
