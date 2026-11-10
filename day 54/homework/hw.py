# # def vowel_indices(word):
# #     result = []
# #     vowels = "aeiouyAEIOUY"

# #     for i in range(len(word)):
# #         if word[i] in vowels:
# #             result.append(i + 1)

# #     return result

# def strong_enough(earthquake: list[list[int]], age: int) -> str:
#     magnitude = 1

#     for shockwave in earthquake:
#         magnitude *= sum(shockwave)

#     strength = 1000 * (0.99 ** age)

#     if magnitude > strength:
#         return "Needs Reinforcement!"

#     return "Safe!"


# def or_arrays(arr1, arr2, fill=0):
#     result = []
#     length1 = len(arr1)
#     length2 = len(arr2)
#     max_length = max(length1, length2)

#     for i in range(max_length):
#         if i < length1:
#             num1 = arr1[i]
#         else:
#             num1 = fill

#         if i < length2:
#             num2 = arr2[i]
#         else:
#             num2 = fill

#         answer = num1 | num2
#         result.append(answer)

#     return result



def divisible_by_three(num_str: str) -> bool:
    total = 0

    for digit in num_str:
        total += int(digit)

    while total >= 3:
        total -= 3

    return total == 0

