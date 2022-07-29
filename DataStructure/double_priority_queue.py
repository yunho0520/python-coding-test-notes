# programmers
import heapq


# 100 score (of 100)
def solution1(operations):
    heap = []
    max_heap = []
    for operation in operations:
        command, num = operation.split()
        num = int(num)
        if command == 'I':
            heapq.heappush(heap, num)
            heapq.heappush(max_heap, (num*-1, num))
        else:
            if len(heap) == 0:
                pass
            elif num == 1:
                max_val = heapq.heappop(max_heap)[1]
                heap.remove(max_val)
            elif num == -1:
                min_val = heapq.heappop(heap)
                max_heap.remove((min_val*-1, min_val))
    if heap:
        return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
    else:
        return [0, 0]


# 100 score (of 100)
def solution2(operations):
    heap = []

    for operation in operations:
        operator, operand = operation.split()
        operand = int(operand)

        if operator == 'I':
            heapq.heappush(heap, operand)
        elif heap:
            if operand < 0:
                heapq.heappop(heap)
            else:
                heap.remove(max(heap))
                heapq.heapify(heap)

    if not heap:
        return [0, 0]

    return [max(heap), heap[0]]
