def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


def find_max(nums):
    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num
    return largest
