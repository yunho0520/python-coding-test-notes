# programmers


# 55 score (of 100)
def solution1(words, queries):
    answer = [0] * len(queries)
    for idx, query in enumerate(queries):
        find_len = len(query)
        find_word = query.replace('?', '')
        find_word_len = len(find_word)
        for word in words:
            word_len = len(word)
            if query[0] == '?':
                if word_len == find_len and word[word_len-find_word_len:find_len] == find_word:
                    answer[idx] = answer[idx] + 1
            else:
                if word_len == find_len and word[0:find_word_len] == find_word:
                    answer[idx] = answer[idx] + 1
    return answer


class Node(object):
    def __init__(self, length = None):
        self.total_children = {}
        if length != None:
            self.total_children[length] = 1
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, s):
        curr_node = self.head
        if len(s) not in curr_node.total_children:
            curr_node.total_children[len(s)] = 1
        else:
            count = curr_node.total_children[len(s)]
            curr_node.total_children[len(s)] = count + 1

        for i in range(0, len(s)):
            suffix_length = len(s) - i - 1
            if s[i] not in curr_node.children:
                curr_node.children[s[i]] = Node(suffix_length)
                curr_node = curr_node.children[s[i]]
            else:
                curr_node = curr_node.children[s[i]]
                if suffix_length not in curr_node.total_children:
                    curr_node.total_children[suffix_length] = 1
                else:
                    count = curr_node.total_children[suffix_length]
                    curr_node.total_children[suffix_length] = count + 1

    def get_count_prefix(self, prefix, count_wildcard):
        curr_node = self.head
        for c in prefix:
            if c not in curr_node.children:
                return 0
            curr_node = curr_node.children[c]

        if count_wildcard not in curr_node.total_children:
            return 0
        else:
            return curr_node.total_children[count_wildcard]


# 100 score (of 100)
def solution2(words, queries):
    answer = []

    # Make trie
    forward_trie = Trie()
    reverse_trie = Trie()
    for word in words:
        forward_trie.insert(word)
        reverse_trie.insert(word[::-1])

    for query in queries:
        if query[-1] == '?':
            count_wildcard = len(query) - query.find('?')
            answer.append(forward_trie.get_count_prefix(query[:-count_wildcard], count_wildcard))
        else:
            count_wildcard = query.rfind('?') + 1
            answer.append(reverse_trie.get_count_prefix(query[count_wildcard:][::-1], count_wildcard))

    return answer


# 100 score (of 100)
def solution3(words, queries):
    answer = []

    fow_trie = {}

    for word in words:
        tmp_trie = fow_trie

        if 'count' not in tmp_trie:
            tmp_trie['count'] = {}

        if len(word) not in tmp_trie['count']:
            tmp_trie['count'][len(word)] = 1
        else:
            tmp_trie['count'][len(word)] += 1

        for i, c in enumerate(word, 1):
            if c not in tmp_trie:
                tmp_trie[c] = {}
            tmp_trie = tmp_trie[c]

            if 'count' not in tmp_trie:
                tmp_trie['count'] = {}

            if (len(word) - i) not in tmp_trie['count']:
                tmp_trie['count'][len(word) - i] = 1
            else:
                tmp_trie['count'][len(word) - i] += 1

            if i == len(word):
                tmp_trie['@@@'] = word

    rev_trie = {}

    for word in words:
        tmp_trie = rev_trie
        word = word[::-1]

        if 'count' not in tmp_trie:
            tmp_trie['count'] = {}

        if len(word) not in tmp_trie['count']:
            tmp_trie['count'][len(word)] = 1
        else:
            tmp_trie['count'][len(word)] += 1

        for i, c in enumerate(word, 1):
            if c not in tmp_trie:
                tmp_trie[c] = {}
            tmp_trie = tmp_trie[c]

            if 'count' not in tmp_trie:
                tmp_trie['count'] = {}

            if (len(word) - i) not in tmp_trie['count']:
                tmp_trie['count'][len(word) - i] = 1
            else:
                tmp_trie['count'][len(word) - i] += 1

            if i == len(word):
                tmp_trie['@@@'] = word

    for query in queries:

        if query[0] == '?':
            query = query[::-1]
            tmp_trie = rev_trie
        else:
            tmp_trie = fow_trie

        cnt = 0
        for i, c in enumerate(query):
            if c == '?':
                if 'count' in tmp_trie:
                    cnt = tmp_trie['count'].get(len(query) - i, 0)
                break

            if c not in tmp_trie:
                break
            tmp_trie = tmp_trie[c]

        answer.append(cnt)

    return answer


# 100 score (of 100)
def solution4(words, queries):
    tree_front = {}
    tree_rear = {}
    for word in words:
        size = len(word)
        tree_front[size] = tree_front.get(size, {})
        curr = tree_front[size]
        for ch in word:
            curr['count'] = curr.get('count', 0) + 1
            curr[ch] = curr.get(ch, {})
            curr = curr[ch]
        tree_rear[size] = tree_rear.get(size, {})
        curr = tree_rear[size]
        for ch in word[::-1]:
            curr['count'] = curr.get('count', 0) + 1
            curr[ch] = curr.get(ch, {})
            curr = curr[ch]
    answer = []
    for query in queries:
        size = len(query)
        answer.append(0)
        if query[0] != '?':
            if size in tree_front:
                curr = tree_front[size]
                for ch in query:
                    if ch == '?':
                        answer[-1] = curr['count']
                        break
                    if ch not in curr:
                        break
                    curr = curr[ch]
        else:
            if size in tree_rear:
                curr = tree_rear[size]
                for ch in query[::-1]:
                    if ch == '?':
                        answer[-1] = curr['count']
                        break
                    if ch not in curr:
                        break
                    curr = curr[ch]
    return answer
