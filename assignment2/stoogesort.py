# special thanks to http://www.ispycode.com

import time
import random
import sys
sys.setrecursionlimit(50000)


def stooge_sort(inp, i=0, j=None):
  if j is None:
    j = len(inp) - 1
  if inp[j] < inp[i]:
    inp[i], inp[j] = inp[j], inp[i]
  if j - i > 1:
    t = (j - i + 1) // 3
    stooge_sort(inp, i  , j-t)
    stooge_sort(inp, i+t, j  )
    stooge_sort(inp, i  , j-t)
  return inp


def main():
    # start_time = time.time()
    # stooge_sort()
    # execution_time = time.time() - start_time
    # print execution_time
    inp = []
    list_count = 0
    with open("./data.txt", 'r') as fp:
        for line in fp:
            line = line.split()
            if line:
                line = [int(i) for i in line]
                inp.append(line)

    for list_to_sort in inp:
        size = list_to_sort[0]
        list_to_sort = list_to_sort[1:]
        inp[list_count] = inp[list_count][1:]

        for i in range(1, size):
            stooge_sort(list_to_sort)

        inp[list_count] = list_to_sort
        list_count += 1

    with open("./stoogesort.out", 'w') as fpout:
        for arr in inp:
            out = " ".join(map(str, arr))
            fpout.write(out + '\n')

if __name__ == '__main__':
    main()
