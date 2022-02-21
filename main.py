# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# My solution (divide, conquer & crossOver), more efficient but not 100% correct
def crossRes(l, r, first, last, s, res, fix):
    while l >= first and r <= last and s[l] == s[r]:
        if not (fix and (l == r or r - l == 1)):
            res.append(s[l:r + 1:])
        l -= 1
        r += 1


def recursiveDiv(first, last, s, res):
    median = int((first + last)/2)
    if last == first:
        return res.append(s[first])
    if last - first == 1:
        res.append(s[first])
        res.append(s[last])
        if s[first] == s[last]:
            res.append(s[first] + s[last])
        return
    temp = recursiveDiv(first, median - 1, s, res)
    if temp:
        res += temp
    temp = recursiveDiv(median + 1, last, s, res)
    if temp:
        res += temp
    crossRes(median, median, first, last, s, res, False)
    crossRes(median, median + 1, first, last, s, res, False)
    crossRes(median - 1, median, first, last, s, res, False)
    crossRes(median + 1, median + 1, first, last, s, res, True)
    crossRes(median - 1, median - 1, first, last, s, res, True)
    if len(s) % 2 == 0:
        crossRes(median + 1, median + 2, first, last, s, res, True)


# correct solution
def countPali(s, l, r):
    res = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
        res += 1
    return res


class Solution:
    def countSubstrings(self, s: str) -> int:
        """result = []
        temp = recursiveDiv(0, len(s) - 1, s, result)
        if temp:
            result.append(temp)
        print(result)
        return len(result)"""
        res = 0
        for i in range(0, len(s)):
            res += countPali(s, i, i)
            res += countPali(s, i, i + 1)
        return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.countSubstrings("bbccaacacdbdbcbcbbbcbadcbdddbabaddbcadb"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
