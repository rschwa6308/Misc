from Words import *
from PerfectStrategy import *

# Calculate difficulty for every word
results = {}
for i, word in enumerate(WORDS):
    if i % 10 == 0: print(i)
    incorrect_guesses = run_game(word, printing=False)
    results[word] = incorrect_guesses

# Write results to a file
with open('results.txt', mode='w') as f:
    results_formatted = [
        f'{k:32} {v}\n' for k, v in 
        sorted(results.items())
    ]
    f.writelines(results_formatted)
