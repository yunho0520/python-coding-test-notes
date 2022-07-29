# programmers

from collections import deque


def get_adjacent(curr, words):
    for word in words:
        if len(curr) != len(word):
            continue

        count = 0
        for c, w in zip(curr, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution1(begin, target, words):
    dist = {begin: 0}
    _deque = deque([begin])

    while _deque:
        curr = _deque.popleft()

        for next in get_adjacent(curr, words):
            if next not in dist:
                dist[next] = dist[curr] + 1
                _deque.append(next)

    return dist.get(target, 0)


def solution2(begin, target, words):
    answer = 0
    _que = [begin]

    while True:
        temp_q = []
        for word_1 in _que:
            if word_1 == target:
                return answer
            for i in range(len(words)-1, -1, -1):
                word_2 = words[i]
                if sum([x != y for x, y in zip(word_1, word_2)]) == 1:
                    temp_q.append(words.pop(i))

        if not temp_q:
            return 0
        _que = temp_q
        answer += 1
