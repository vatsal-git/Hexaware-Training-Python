# Question 1
print("<= Question 1 =>")
result_q1 = [str(x) for x in range(2000, 3201) if x % 7 == 0 and x % 5 != 0]
print(','.join(result_q1))

# Question 2
print("\n<= Question 2 =>")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


num_q2 = int(input())
result_q2 = factorial(num_q2)
print(result_q2)

# Question 3
print("\n<= Question 3 =>")
n_q3 = int(input())
result_q3 = {i: i*i for i in range(1, n_q3+1)}
print(result_q3)

# Question 4
print("\n<= Question 4 =>")
input_sequence_q4 = input()
numbers_list_q4 = input_sequence_q4.split(',')
numbers_tuple_q4 = tuple(numbers_list_q4)
print(numbers_list_q4)
print(numbers_tuple_q4)

# Question 5
print("\n<= Question 5 =>")
import math

C_q5 = 50
H_q5 = 30
input_sequence_q5 = input()
D_values_q5 = [int(x) for x in input_sequence_q5.split(',')]
result_q5 = [str(int(math.sqrt((2 * C_q5 * D_q5) / H_q5))) for D_q5 in D_values_q5]
print(','.join(result_q5))

# Question 6
print("\n<= Question 6 =>")
X_q6, Y_q6 = map(int, input().split())
result_q6 = [[i*j for j in range(Y_q6)] for i in range(X_q6)]
print(result_q6)

# Question 7
print("\n<= Question 7 =>")
input_words_q7 = input().split(',')
sorted_words_q7 = sorted(input_words_q7)
print(','.join(sorted_words_q7))

# Question 8
print("\n<= Question 8 =>")
input_lines_q8 = input().split('\n')
capitalized_lines_q8 = [line.upper() for line in input_lines_q8]
print('\n'.join(capitalized_lines_q8))

# Question 9
print("\n<= Question 9 =>")
input_sequence_q9 = input()
unique_sorted_words_q9 = sorted(set(input_sequence_q9.split()))
print(' '.join(unique_sorted_words_q9))

# Question 10
print("\n<= Question 10 =>")
binary_numbers_q10 = input().split(',')
result_q10 = [num_q10 for num_q10 in binary_numbers_q10 if int(num_q10, 2) % 5 == 0]
print(','.join(result_q10))

# Question 11
print("\n<= Question 11 =>")
result_q11 = [str(x_q11) for x_q11 in range(1000, 3001) if all(int(digit_q11) % 2 == 0 for digit_q11 in str(x_q11))]
print(','.join(result_q11))

# Question 12
print("\n<= Question 12 =>")
input_sentence_q12 = input()
letters_count_q12 = sum(c_q12.isalpha() for c_q12 in input_sentence_q12)
digits_count_q12 = sum(c_q12.isdigit() for c_q12 in input_sentence_q12)
print("LETTERS", letters_count_q12)
print("DIGITS", digits_count_q12)

# Question 13
print("\n<= Question 13 =>")
input_sentence_q13 = input()
upper_count_q13 = sum(c_q13.isupper() for c_q13 in input_sentence_q13)
lower_count_q13 = sum(c_q13.islower() for c_q13 in input_sentence_q13)
print("UPPER CASE", upper_count_q13)
print("LOWER CASE", lower_count_q13)

# Question 14
print("\n<= Question 14 =>")
a_q14 = input()
result_q14 = int(a_q14) + int(a_q14*2) + int(a_q14*3) + int(a_q14*4)
print(result_q14)

