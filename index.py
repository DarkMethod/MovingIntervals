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

T = int(raw_input())
output = []
for i in range(0,T):
    C, N, K = raw_input().split()
    C, N, K = int(C), int(N), int(K)
    child = []
    for j in range(0,N):
        c = [int(x) for x in raw_input().split()]
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
                output.append("BAD")
    elif K == 1:
        if N > C:
            output.append("BAD")
        else:
            demand = 0
            for i in child:
                demand += i[1]-i[0]+1
            if demand > C:
                output.append("BAD")
            else:
                overlaps, num_of_overlaps = 0,0
                overlaps, num_of_overlaps = overlaps_exists(child)
                if overlaps == 0:
                    output.append("GOOD")
                elif overlaps == 1:
                    num_overlaps = [0]*len(child)
                    max = 0
                    for i in range(len(child)):
                        for j in range(i+1, len(child)):
                            if child[i][1] >= child[j][0]:
                                num_overlaps[i] += 1
                                num_overlaps[j] += 1
                    for i in range(len(child)):
                        if num_overlaps[i] > num_overlaps[max]:
                            max = i
                    if (child[max][1]+child[max][0]-1) > (C-demand+child[max][0]+child[max][1]-1):
                        output.append("BAD")
                    else:
                        output.append("GOOD")

for o in range(len(output)):
    print output[o]
