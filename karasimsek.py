import time
ledler = [29, 31, 33, 35, 37]

while True:
    for i in range(5):
        print(i)
        time.sleep(1)
    for i in range(4, -1, -1):
        print(i)
        time.sleep(1)
