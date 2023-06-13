import threading
import time

def calcSq(num, results ):
    print('---', num)
    results[num]=num**2

results = {}
threads = [ threading.Thread(target=calcSq, args=(n,results)) for n in range (1,11) ]

[t.start() for t in threads]
[t.join() for t in threads]

print('results: ', results)
