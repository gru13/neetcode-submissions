class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        j = {}
        c = {0:0}
        mfq = 0
        for a in nums:
            if a not in j:
                j[a] = 1
                if mfq < 1:
                    mfq += 1
                    c[mfq] = []
                c[1].append(a)
            else:
                c[j[a]].remove(a)
                j[a] += 1
                if j[a] > mfq:
                    mfq += 1
                    c[mfq] = []
                c[j[a]].append(a)

        result = []
        print(j, c)
        while mfq > 0:
            result += c[mfq]
            if len(result) > k:
                result = result[:k]
                break
            mfq -= 1
        print(result)
        return result