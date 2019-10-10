class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)

        i = 0
        j = len(lst)-1

        yy = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        while i < j and i < len(lst) and j >= 0:
            while i < len(lst) and lst[i] not in yy:
                i += 1

            while j >= 0 and lst[j] not in yy:
                j -= 1

            if i < j:
                lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

        return ''.join(lst)



lst = ['A', 'B', 'C', 'D']

print(''.join(lst))
print(','.join(lst))
print('.'.join(lst))