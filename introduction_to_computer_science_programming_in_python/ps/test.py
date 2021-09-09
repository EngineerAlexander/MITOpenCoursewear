shift = 1

# Uppercase shifts
lower_bound = 'a'
higher_bound = 'z'

lower_bound_dec = ord(lower_bound)
higher_bound_dec = ord(higher_bound)

list = list(range(lower_bound_dec, higher_bound_dec + 1))
list_chr = [chr(el) for el in list]
list_zero = [el - lower_bound_dec for el in list]
list_zero_shift = [el + shift for el in list_zero]

list_zero_shift_fixed = []
for el in list_zero_shift:
    while el < 0:
        el = el + list_zero[-1] + 1
    while el > list_zero[-1]:
        el = el - list_zero[-1] - 1
    list_zero_shift_fixed.append(el)

ans_list = [el + lower_bound_dec for el in list_zero_shift_fixed]
ans_list_chr = [chr(el) for el in ans_list]

cipher_dict = {}
for i in range(len(list_chr)):
    cipher_dict[list_chr[i]] = ans_list_chr[i]


print(list)
print(list_zero)
print(list_zero_shift)
print(list_zero_shift_fixed)
print(ans_list)
print(ans_list_chr)

for i in cipher_dict:
    print(i, cipher_dict[i])

num_upper_letters = len(list)

shift = list

#for lowercase_iter in range(26)