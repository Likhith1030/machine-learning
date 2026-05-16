from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        words = [beginWord] + wordList[:]

        graph = defaultdict(list)

        def check(word1, word2):

            diff = 0

            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1

            return diff == 1

        for i in range(len(words)):
            for j in range(i + 1, len(words)):

                if check(words[i], words[j]):

                    graph[words[i]].append(words[j])
                    graph[words[j]].append(words[i])

        q = deque([[beginWord, 1]])
        visited = set([beginWord])

        while q:

            word, steps = q.popleft()

            if word == endWord:
                return steps

            for nei in graph[word]:

                if nei not in visited:
                    visited.add(nei)
                    q.append([nei, steps + 1])

        return 0