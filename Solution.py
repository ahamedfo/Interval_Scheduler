class Solution:

    def __init__(self, listOfRallies):
        self.rallies = listOfRallies

    def sorted_key(self, tuple):
        return tuple[1]

    def getSchedule(self):
        ################# YOUR CODE GOES HERE ##################
        # print(self.rallies)
        map = {}
        i = 0
        for value in self.rallies:
            map[value] = i
            i += 1
        S = []
        Serena_Rallies = sorted(self.rallies, key=self.sorted_key)
        length_rally = len(Serena_Rallies)
        next_startTime = 0
        while len(Serena_Rallies) != 0:
            S.append((map[Serena_Rallies[0]], next_startTime))
            next_startTime += Serena_Rallies[0][0]
            Serena_Rallies.remove(Serena_Rallies[0])
            for requests in Serena_Rallies:
                #print(requests)
                if next_startTime > requests[1]:
                    Serena_Rallies.remove(requests)
                elif next_startTime < requests[1]:
                    break
        #print(S)
        #print(next_startTime)
        if len(S) != length_rally:
            return []
        return S