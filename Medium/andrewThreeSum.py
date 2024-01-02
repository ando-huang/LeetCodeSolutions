'''
    Finds unique trios that sum up to 0

    first nested loop populates a dictionary named pairs
        key: sum
        value: list of tuples of indices where nums[i] + nums[j] = sum

    second nested loop gets all solution indices
    for each num, check pairs for a matching sum
    if the sum exists, get pairs[complement] and add trios where the current
    index is not in a pair.

    convert the solutions to a set to eliminate repeats
'''
def threeSum(self, nums: List[int]) -> List[List[int]]:
    pairs = {}
    for i in range(len(nums) - 1):
        for j in range(i +1, len(nums)):
            pairSum = nums[i] + nums[j]
            if pairSum in pairs:
                pairs[pairSum] += [[i, j]]
            else:
                pairs[pairSum] = [[i, j]]
    print(pairs)
    sols = []
    for i in range(len(nums)):
        if (0 - nums[i]) in pairs.keys():
            eligiblePairs = pairs[(0 - nums[i])]
            for pair in eligiblePairs:
                if i not in pair:
                    trio = sorted([nums[i], pair[0], pair[1]])
                    sols.append(trio)
    sols = list(set(tuple(i) for i in sols))
    return sols
