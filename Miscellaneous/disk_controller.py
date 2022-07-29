# programmers
import heapq
from collections import deque


def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    heap = []
    heapq.heappush(heap, tasks.popleft())
    curr_time, total_time = 0, 0
    while len(heap) > 0:
        dur, req = heapq.heappop(heap)
        curr_time = max(curr_time + dur, req + dur)
        total_time += curr_time - req
        while len(tasks) > 0 and tasks[0][1] <= curr_time:
            heapq.heappush(heap, tasks.popleft())
        if len(tasks) > 0 and len(heap) == 0:
            heapq.heappush(heap, tasks.popleft())
    return total_time // len(jobs)
