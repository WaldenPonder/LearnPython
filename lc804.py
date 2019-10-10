class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        m = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        s = set()
        for cs in words:
            lst = []
            for c in cs:
                lst.append(m[ord(c) - ord('a')])
            s.add(''.join(lst))
        return len(s)


s = Solution()
b = s.uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"])
print(b)
