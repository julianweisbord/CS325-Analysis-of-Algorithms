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

        out = merge_sort(list_to_sort)

        inp[list_count] = out
        list_count += 1

    with open("./mergesort.out", 'w') as fpout:
        for arr in inp:
            print arr
            out = " ".join(map(str, arr))
            fpout.write(out + '\n')

if __name__ == '__main__':
    main()
