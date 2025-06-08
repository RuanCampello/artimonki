from collections import deque
from typing import List


def reverseWords(s: str) -> str:
    words: List[str] = list(filter(lambda x: x.strip() != "", s.split(" ")))
    reversedWords = deque()
    for word in words:
        reversedWords.appendleft(word)

    return " ".join(reversedWords)


print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))
print(reverseWords("a good   example"))
