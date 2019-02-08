import itertools
eng_dict = open('words_alpha.txt').read().splitlines()
input_phrase = input().split()
output_phrase = [[] for i in range(len(input_phrase))]
check_len = False
for i in range(len(input_phrase)):
    if len(input_phrase[i]) > 2:
        check_len = True
        for j in range(len(eng_dict)):
            # searching for anagrams
            if sorted(eng_dict[j]) == sorted(input_phrase[i]):
                output_phrase[i].append(eng_dict[j])
    else:
        output_phrase[i] = [input_phrase[i]]
# making all possible rearrangements of lists of anagrams in a phrase
output_permutations = list(itertools.permutations(output_phrase))
input_permutations = list(itertools.permutations(input_phrase))
result_list = []
if check_len is True:
    for i in range(len(output_permutations)):
        # creating a list of all possible output phrases
        result_list += list(itertools.product(*output_permutations[i]))
    for i in range(len(result_list)):
        # making sure there are not the same input words in different order
        if result_list[i] not in input_permutations:
            for j in range(len(result_list[i])):
                print(result_list[i][j], end=' ')
            print()
else:  # rearrange the input phrase if all words are two letter words
    for i in range(len(input_permutations)):
        for j in range(len(input_permutations[i])):
            print(input_permutations[i][j], end=' ')
        print()
