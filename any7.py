def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE
    for num in nums:
        if num == 7:
            return True

    return False


print("Should be true:", any7([1, 2, 7, 4, 5]))
print("Should be false:", any7([1, 2, 4, 5]))
