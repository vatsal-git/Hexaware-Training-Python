print('\n')
print("="*10, "Question 1", "="*10)
def q1(str="ilike", word_dict={"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}):
    n = len(str)
    
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and str[j:i] in word_dict:
                dp[i] = True
                break

    print(dp[n])

q1('icecream')


print('\n')
print("="*10, "Question 2", "="*10)
def q2(n=100):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], 1 + dp[i - j * j])
            j += 1

    print(dp[n])

q2(33)


print('\n')
print("="*10, "Question 3", "="*10)
def q3(n=371):
    if n < 0:
        return q3(-n)
    if n == 0 or n == 7:
        return True
    if n < 10:
        return False

    return q3(n // 10 - 2 * (n % 10))

print(q3(12312312))


print('\n')
print("="*10, "Question 4", "="*10)
def count_and_say(n=5):
    if n == 1:
        return "1"

    prev_term = count_and_say(n - 1)
    result = ""
    count = 1

    for i in range(1, len(prev_term)):
        if prev_term[i] == prev_term[i - 1]:
            count += 1
        else:
            result += str(count) + prev_term[i - 1]
            count = 1

    result += str(count) + prev_term[-1]
    return result

print(count_and_say())

