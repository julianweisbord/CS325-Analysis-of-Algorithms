import time
import random
import sys
sys.setrecursionlimit(50000)
def main():
    start_time = time.time()

    inp = random.sample(xrange(10000), 8000)
    size = len(inp)

    for i in range(1, size):
        j = i
        while j > 0 and inp[j] < inp[j-1]:
            temp = inp[j]
            inp[j] = inp[j-1]
            inp[j-1] = temp
            j -= 1

    execution_time = time.time() - start_time
    print execution_time

if __name__ == '__main__':
    main()
