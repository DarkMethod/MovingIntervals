def overlaps_exists(child):
    for l in range(len(child)):
        min_idx = l
        for m in range(l+1,len(child)):
            if child[min_idx][0] > child[m][0]:
                 min_idx = m
        child[l], child[min_idx] = child[min_idx], child[l]
    overlaps = 0
    num_of_overlaps = 0
    for n in range(len(child)-1):
        if child[n][1] >= child[n+1][0]:
            overlaps = 1
    return overlaps, num_of_overlaps

T = int(raw_input("No. of testcases: "))
output = []
for i in range(0,T):
    C, N, K = raw_input("No. of Cakes, Children and K in "+str(i+1)+" testcase: ").split()
    C, N, K = int(C), int(N), int(K)
    child = []
    for j in range(0,N):
        c = [int(x) for x in raw_input("Start pos, End pos for "+str(j+1)+" child: ").split()]
        child.append(c)
    if K == 0:
        if N > C:
            output.append("BAD")
        else:
            overlaps, num_of_overlaps = 0,0
            overlaps, num_of_overlaps = overlaps_exists(child)
            if overlaps == 0:
                output.append("GOOD")
            elif overlaps == 1:
            elif K == 1:
                output.append("BAD")
        if N > C:
            output.append("BAD")
        else:
            overlaps, num_of_overlaps = 0,0
            overlaps, num_of_overlaps = overlaps_exists(child)
            if overlaps == 0:
                output.append("GOOD")
            elif overlaps == 1:
                if num_of_overlaps > 1:
                    output.append("BAD")
                else:
                        

for o in range(len(output)):
    print output[o]
