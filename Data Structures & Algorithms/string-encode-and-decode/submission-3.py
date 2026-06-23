class Solution:
    sep = '.|.'
    def encode(self, strs: List[str]) -> str:
        result = str(len(strs))
        for a in strs:
            result += self.sep + str(len(a)) + self.sep + a
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        stream = s.split(self.sep)
        if stream[0] == "0":
            return []
        result = []
        for i in range(1, len(stream),2):
            result.append(stream[i+1])
        return result
