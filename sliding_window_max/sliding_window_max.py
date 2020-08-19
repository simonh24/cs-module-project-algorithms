'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    ind = 0
    output = []
    while not ind == len(nums) - k + 1:
        new_list = nums[ind:ind+k]
        new_list_max = new_list[0]
        for i in new_list:
            if new_list_max < i:
                new_list_max = i
        output.append(new_list_max)
        ind += 1
    return output


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
