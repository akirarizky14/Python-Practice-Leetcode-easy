
def twoSum(s,target):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            sum = s[i] + s[j]
            if sum == target:
                return [i,j]
print(twoSum([1,2,3,3],5))