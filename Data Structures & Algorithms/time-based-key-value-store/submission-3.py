class TimeMap:

    def __init__(self):
        self.hashMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        hashMap = self.hashMap
        hashMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        hashMap = self.hashMap

        l, r = 0, len(hashMap[key]) - 1

        while l <= r:
            mid = (l + r) // 2

            t = hashMap[key][mid][0]

            if timestamp > t:
                l = mid + 1
            elif timestamp < t:
                r = mid - 1
            else:
                return hashMap[key][mid][1]
        
        return hashMap[key][r][1] if r >= 0 else ""
        
