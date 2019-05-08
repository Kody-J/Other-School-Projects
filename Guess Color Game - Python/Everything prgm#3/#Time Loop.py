## Time Module
import time

cnt_dwn = time.time()
for i in range(5 ,0, -1):
    time.sleep(1)
    print(i)





start = time.time()
questions_remaining = 0
for questions_remainig in range(usr_input):
    end = time.time()
    print("The program slept for", end - start, "seconds")
