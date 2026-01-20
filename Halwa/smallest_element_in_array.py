class smallestElement:
    def findSmallestElement(self, arr: list[int]) -> int:
        lowest = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < lowest:
                lowest = arr[i]
        return lowest
obj1=smallestElement()
print(obj1.findSmallestElement([1,2,3,0,6,7]))