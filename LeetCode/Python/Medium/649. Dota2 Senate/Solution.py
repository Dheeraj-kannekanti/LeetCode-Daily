from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        self.radiant = deque()
        self.dire = deque()
        for i in range(len(senate)):
            if senate[i] == "R":
                self.radiant.append(i)
            else:
                self.dire.append(i)
        while self.radiant and self.dire:
            r = self.radiant.popleft()
            d = self.dire.popleft()
            if r<d:
                self.radiant.append(r+len(senate))
            elif d<r:
                self.dire.append(d+len(senate))
        if self.radiant:
            return "Radiant"
        return "Dire"