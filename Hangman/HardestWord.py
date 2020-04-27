from Words import *
from PerfectStrategy import *

# search_space = {w for w in WORDS if 'j' in w and len(w) > 3}
search_space = WORDS
print(len(search_space))

# dist = {}
# candidate, max_incorrect_guesses = None, -1
results = {}

for i, word in enumerate(search_space):
    if i % 10 == 0: print(i)
    incorrect_guesses = run_game(word, printing=False)
    results[word] = incorrect_guesses

    # if incorrect_guesses > max_incorrect_guesses:
    #     print(word, incorrect_guesses)
    #     max_incorrect_guesses = incorrect_guesses
    #     candidate = word
    
    # if incorrect_guesses not in dist:
    #     dist[incorrect_guesses] = 0
    # dist[incorrect_guesses] += 1

# print(dist)

with open('results.txt', mode='w') as f:
    results_formatted = [
        f'{k:32} {v}\n' for k, v in 
        sorted(results.items())
    ]
    f.writelines(results_formatted)
