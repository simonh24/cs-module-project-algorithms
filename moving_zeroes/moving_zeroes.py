'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # New method does not require using new space
    if arr is None:
        return
    for i in arr:
        if i == 0:
            arr.remove(0)
            arr.append(0)
    return arr
    # ind = 0
    # out = []
    # while not ind == len(arr):
    #     if arr[ind] == 0:
    #         zeros = arr.pop(ind)
    #         out.append(zeros)
    #     else:
    #         ind += 1
    # for i in out:
    #     arr.append(i)
    # return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")