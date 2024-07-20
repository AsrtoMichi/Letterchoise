The program allows you to efficiently identify all combinations of letters, which, through their presence in the word, will enable the word to be uniquely identified.
The efficiency is because the maximum number of letters is ceil(log2(len(words))). Since the letters can be sorted as desired, the combinations can be generated through combinations instead of permutations.
