from timeit import default_timer as timer

startTime = timer()

for _ in range(100000):
    print(_)
    
endTime = timer()

print(endTime - startTime, ' s')