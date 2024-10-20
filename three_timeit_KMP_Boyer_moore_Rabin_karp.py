import timeit

### Алгоритм Боєра-Мура

class BoyerMoore:
    def __init__(self, pattern):
        self.pattern = pattern
        self.bad_char = self._bad_character_heuristic()

    def _bad_character_heuristic(self):
        bad_char = {}
        for i in range(len(self.pattern)):
            bad_char[self.pattern[i]] = i
        return bad_char

    def search(self, text):
        m = len(self.pattern)
        n = len(text)
        s = 0
        results = []

        while s <= n - m:
            j = m - 1

            while j >= 0 and self.pattern[j] == text[s + j]:
                j -= 1

            if j < 0:
                results.append(s)
                s += (s + m < n) and m - self.bad_char.get(text[s + m], -1) or 1
            else:
                s += max(1, j - self.bad_char.get(text[s + j], -1))
        
        return results


### Алгоритм Кнута-Морріса-Пратта

class KMP:
    def _compute_lps(self, pattern):
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def search(self, text, pattern):
        m = len(pattern)
        n = len(text)
        lps = self._compute_lps(pattern)
        i = j = 0
        results = []

        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1
            
            if j == m:
                results.append(i - j)
                j = lps[j - 1]
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return results

### Алгоритм Рабіна-Карпа

class RabinKarp:
    def search(self, text, pattern):
        d = 256
        q = 101  # a prime number
        m = len(pattern)
        n = len(text)
        p = 0  # hash value for pattern
        t = 0  # hash value for text
        h = 1
        results = []

        for i in range(m - 1):
            h = (h * d) % q

        for i in range(m):
            p = (d * p + ord(pattern[i])) % q
            t = (d * t + ord(text[i])) % q

        for i in range(n - m + 1):
            if p == t:
                if text[i:i + m] == pattern:
                    results.append(i)

            if i < n - m:
                t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
                if t < 0:
                    t += q
        
        return results

### Вимірювання часу виконання

text1 = "https://drive.google.com/file/d/18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh/view"
text2 = "https://drive.google.com/file/d/18BfXyQcmuinEI_8KDSnQm4bLx6yIFS_w/view"

patterns = ["комп'ютерних", "дослідження", "мили_миломруки"]

# Створимо екземпляри алгоритмів
bm = BoyerMoore(patterns[0])
kmp = KMP()
rk = RabinKarp()

# Функція для вимірювання
def measure_time(algorithm, text, pattern):
    start_time = timeit.default_timer()
    if isinstance(algorithm, BoyerMoore):
        algorithm.search(text)
    elif isinstance(algorithm, KMP):
        algorithm.search(text, pattern)
    else:
        algorithm.search(text, pattern)
    return timeit.default_timer() - start_time

# Вимірювання
for pattern in patterns:
    print(f"Підрядок: {pattern}")
    print("Алгоритм Боєра-Мура:", measure_time(bm, text1, pattern))
    print("Алгоритм Кнута-Морріса-Пратта:", measure_time(kmp, text1, pattern))
    print("Алгоритм Рабіна-Карпа:", measure_time(rk, text1, pattern))
    print()