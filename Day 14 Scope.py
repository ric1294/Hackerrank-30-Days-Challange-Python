
def computeDifference(self):
    result = []
    for i in range(len(self.__elements)):
        for j in range(len(self.__elements)):

            diff = abs(self.__elements[i] - self.__elements[j])
            result.append(diff)
        
    self.maximumDifference = max(result)    
        # print(result)