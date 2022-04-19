import collections
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        paragraph = paragraph.lower().split()
        frequency =collections.Counter(paragraph)
        print(frequency.most_common(1))
        for word, count in frequency.most_common():
            if word in banned:
                continue
            else:
                return word
    
    def mostCommonWord2(self, paragraph: str, banned: List[str]) -> str:
        banned_words = set(banned)
        ans = ""
        max_count = 0
        word_count = collections.defaultdict(int)
        word_buffer = []
        print("banned_words"," : ",banned_words)
        for p, char in enumerate(paragraph):
            #1). consume the characters in a word
            if char.isalnum():
                word_buffer.append(char.lower())
                if p != len(paragraph)-1:
                    continue

            #2). at the end of one word or at the end of paragraph
            if len(word_buffer) > 0:
                word = "".join(word_buffer)
                print("word_buffer" ," :",word_buffer)
                
                if word not in banned_words:
                    word_count[word] +=1
                    if word_count[word] > max_count:
                        max_count = word_count[word]
                        ans = word
                # reset the buffer for the next word
                word_buffer = []
            
        return ans
    
print(Solution().mostCommonWord2("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))