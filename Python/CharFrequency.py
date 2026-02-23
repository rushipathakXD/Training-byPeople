# user_input = input("Enter a String: ")
# dict_user_input = {}

# for i in user_input:
#     if i not in dict_user_input:
#         dict_user_input[i] = 1
#     else:
#         dict_user_input[i] += 1

# print(dict_user_input)
user_input = input("Enter a String: ").lower()
freq = {}

for ch in user_input:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] += 1

print(freq)