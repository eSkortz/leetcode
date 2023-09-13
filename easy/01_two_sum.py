def twoSum(nums: list[int], target: int) -> list[int]:
    matches = {}
    for number_index in range(len(nums)):
        match = target - nums[number_index]
        if match in matches:
            return [matches[match], number_index]
        else:
            matches[nums[number_index]] = number_index
    return []