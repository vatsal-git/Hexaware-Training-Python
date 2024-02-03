print('\n')
print("="*10, "Question 1", "="*10)
def q1(arr = [1, 2, 3, 4, 5, 6], sum = 6):
    for i in range(0, len(arr) - 1):
        for j in range(1, len(arr)):
            curr_sum = arr[i] + arr[j]
            if curr_sum == sum:
                print("Sum vars =>", arr[i], arr[j])

q1()

print('\n')
print("="*10, "Question 2", "="*10)
def q2(arr = [1, 2, 3, 4, 5, 6]):
    res = arr.copy()

    for i in range(0, len(arr)):
        prod = 1
        for j in range(0, len(arr)):
            if i != j:
                prod = prod * arr[j]
        res[i] = prod

    print(res)

q2([2, 4, 6])


print('\n')
print("="*10, "Question 3", "="*10)
def q3(arr=[1, 2, -3, 3, -4, 5]):
    def kadane(arr):
        max_sum = float('-inf')
        curr_sum = 0

        for num in arr:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum

    total_sum = sum(arr)
    max_kadane = kadane(arr + [-num for num in arr])
    max_wrap = total_sum + kadane([-num for num in arr])

    print(max(max_kadane, max_wrap) if max_kadane > 0 else max_kadane)

q3([10, -3, -4, 7, 6, 5, -4, -1])


print('\n')
print("="*10, "Question 4", "="*10)
def q4(arr=[1, 2, 3, 4, 5, 6]):
    arr.sort()
    max_diff = arr[0] - arr[1]
    max_diff_ele = [arr[0], arr[1]]

    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if arr[i] - arr[j] > max_diff:
                max_diff = arr[i] - arr[j]
                max_diff_ele = [arr[i], arr[j]]

    print("Max Diff => {} - {} = {}".format(max_diff_ele[0], max_diff_ele[1], max_diff))

q4()


print('\n')
print("="*10, "Question 5", "="*10)
def q5(arr=[1, 2, 3, 4, 5, 6, 3]):
    non_repeating_list = []

    for i in range(0, len(arr)):
        count = 0
        for j in range(0, len(arr)):
            if arr[i] == arr[j]:
                count += 1
        if count == 1:
            non_repeating_list.append(arr[i])
    
    print(non_repeating_list[0])

q5([9, 4, 9, 6, 7, 4])


print('\n')
print("="*10, "Question 6", "="*10)
def q6(arr=[1, 2, 3, 4, 5, 6], k=6):
    arr.sort()

    n = len(arr)

    min_height = min(arr[0] + k, arr[n - 1] - k)
    max_height = max(arr[0] + k, arr[n - 1] - k)

    for i in range(1, n - 1):
        sub = arr[i] - k
        add = arr[i] + k

        if sub >= min_height or add <= max_height:
            continue
        
        if max_height - sub <= add - min_height:
            min_height = sub
        else:
            max_height = add

    print(max_height - min_height)

q6([1, 5, 15, 10], 3)

