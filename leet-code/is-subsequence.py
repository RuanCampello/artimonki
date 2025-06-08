def isSubsequence(s: str, t: str) -> bool:
    return not s or (s[0] in t and isSubsequence(s[1:], t[t.index(s[0]) + 1 :]))


print(isSubsequence("abc", "ahbgdc"))
print(isSubsequence("axc", "ahbgdc"))
print(isSubsequence("acb", "ahbgdc"))
