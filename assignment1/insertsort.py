def main():
    print "hi"
    inp = []
    list_count = 0
    with open("./data.txt", 'r') as fp:
        print "opened data"
        for line in fp:
            line = line.split()
            if line:
                line = [int(i) for i in line]
                inp.append(line)

    for list_to_sort in inp:
        size = list_to_sort[0]
        list_to_sort = list_to_sort[1:]
        inp[list_count] = inp[list_count][1:]
        print inp[list_count]
        for i in range(1, size):
            j = i
            while j > 0 and list_to_sort[j] < list_to_sort[j-1]:
                temp = list_to_sort[j]
                list_to_sort[j] = list_to_sort[j-1]
                list_to_sort[j-1] = temp
                j -= 1
        inp[list_count] = list_to_sort
        list_count += 1

    with open("./insertsort.out", 'w') as fpout:
        print "make insertsort.out"
        # fpout.write(str(inp))
        print inp
        for arr in inp:
            out = " ".join(map(str, arr))
            fpout.write(out + '\n')

if __name__ == '__main__':
    main()
