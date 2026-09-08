class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))
        
        pos_speed.sort(reverse=True)

        fleets = len(pos_speed)
        max_tta = 0 # time to arrive

        for c in pos_speed:
            tta = (target - c[0]) / c[1] # calculate time to arrive

            if tta > max_tta:
                max_tta = tta
            elif tta <= max_tta:
                fleets -= 1

        return fleets
