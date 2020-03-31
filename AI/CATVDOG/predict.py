import time

x = []

for i in range(1024*4*5000):
    x.append(i)

print("Lefoglalva valamennyi...")
time.sleep(5)
del x
print("Törölve valamennyi...")

time.sleep(5)
