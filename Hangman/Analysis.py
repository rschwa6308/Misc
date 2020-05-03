import os

filename = os.path.join(os.path.dirname(__file__), 'results.txt')
with open(filename, mode='r') as f:
    results = {
        entry[0]: int(entry[1]) for entry in
        [line.split() for line in f.read().split('\n')[:-1]]    # newline at EOF
    }

for word_length in range(1, 33):
    filtered_results = {k: v for k, v in results.items() if len(k) == word_length}
    if len(filtered_results) == 0: continue
    res = max(filtered_results.items(), key=lambda item: item[1])
    print(f'Hardest word of length {word_length}: {res[0]} ({res[1]})')
