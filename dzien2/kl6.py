class LongestKeyDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key

        return longest


art = LongestKeyDict()
art['tomasz'] = 12
art['abraham'] = 7
art['siedem'] = 9
art['zen'] = 1
print(art.longest_key())  # abraham
print(art)
# {'tomasz': 12, 'abraham': 7, 'siedem': 9, 'zen': 1}
