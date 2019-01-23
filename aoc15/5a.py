nice_counter = 0
vowels = list('aeiou')
data = open('r_input.txt').read().splitlines()
bad_chunk = ['ab','cd','pq','xy']

for value in data:
    # print(value)
    bad_chunk_bool = False
    vowel_counter = 0
    double_char_bool = False
    chunks = [value[i:(i+2%len(value))] for i in range(len(value))]

    for i in value:
        if i in vowels:
            vowel_counter +=1

    for chunk in chunks:
        if chunk in bad_chunk:
            bad_chunk_bool = True
            break
        if len(chunk) != len(set(chunk)):
            double_char_bool = True

    if bad_chunk_bool == True:
        continue

    if vowel_counter >= 3 and double_char_bool == True:
        nice_counter +=1

        # print(f"vowel counter:{vowel_counter}")
        # print(f"double bool:{double_char_bool}")
        # print()
print(f"nice strings:{nice_counter}")
