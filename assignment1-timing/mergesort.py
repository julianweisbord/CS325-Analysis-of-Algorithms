import time
import random

def merge_lists(list_a, list_b):
    if not list_a:
        return list_b
    if not list_b:
        return list_a

    if list_b[0] > list_a[0]:
        return [list_a[0]] + merge_lists(list_a[1:], list_b)
    return [list_b[0]] + merge_lists(list_a, list_b[1:])

def merge_sort(inp_list):
    if len(inp_list) <= 1:
        return inp_list
    mid = len(inp_list) / 2

    left = merge_sort(inp_list[:mid])
    right = merge_sort(inp_list[mid:])
    return merge_lists(left, right)

def main():
    start_time = time.time()
    inp = random.sample(xrange(10000), 1000)
    size = len(inp)

    out = merge_sort(inp)

    inp = out

    print "took seconds:",time.time() - start_time

if __name__ == '__main__':
    main()
