def pref_search(pattern):
    p = [0] * len(pattern)
    j = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            p[i] = j
            i += 1
        else:
            if j != 0:
                j = p[j - 1]
            else:
                p[i] = 0
                i += 1

    return p


def kmp_search(needle, haystack):
    result = []

    if not needle or not haystack:
        return result

    n = len(haystack)
    m = len(needle)

    p = pref_search(needle)

    i = 0
    j = 0

    while i < n:
        if needle[j] == haystack[i]:
            i += 1
            j += 1

            if j == m:
                result.append((i - j, i - 1))
                j = p[j - 1]

        else:
            if j != 0:
                j = p[j - 1]
            else:
                i += 1

    return result if result else "Підстроку не знайдено"


if __name__ == "__main__":
    print("Перший варіант:")
    print(kmp_search("ліліло", "лілілось лілілось"))
    print("Дргуий варіант:")
    print(kmp_search("лох", "лілілохсь лілілохсь"))
    print("Третій варіант:")
    print(kmp_search("ліліла", "лілілось лілілось"))
