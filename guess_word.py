class Solution(object):
    def findSecretWord(self, wordlist, master):
        candidates = wordlist[:]
        while candidates:
            try_index = 0
            min_max_size = len(candidates)
            for i in range(len(candidates)):
                groups = [0] * 7
                for s in candidates:
                    m = self._matches(candidates[i], s)
                    groups[m] += 1
                max_size = 0
                for val in groups:
                    if val > max_size:
                        max_size = val
                if max_size < min_max_size:
                    min_max_size = max_size
                    try_index = i
            guess_word = candidates[try_index]
            similarity_score = master.guess(guess_word)
            if similarity_score == 6:
                return
            next_round = []
            for s in candidates:
                if self._matches(s, guess_word) == similarity_score:
                    next_round.append(s)
            candidates = next_round
    def _matches(self, a, b):
        count = 0
        for i in range(len(a)):
            if a[i] == b[i]:
                count += 1
        return count
