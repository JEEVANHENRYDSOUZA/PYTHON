nes (7 sloc)  416 Bytes


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = -1 # we will start iterating from the back that is last                     element of the array
                #the last element of the array will always be the element which is the greatest present on the right side
        for i in range(len(arr)-1, -1, -1):
            arr[i], mx = mx, max(arr[i], mx)
        return arr
© 2022 GitHub, Inc.
Terms
