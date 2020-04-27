from Words import *

# Given the current game state (remaining words set, remaining letters set), return the optimal letter to guess
# Strategy: guess the most common letter from the list of all remaining possible words
#           (guaranteed to be previously un-guessed)
def optimal_guess(remaining_words, remaining_letters):
    freq = letter_frequency(remaining_words)
    freq = {k: v for k, v in freq.items() if k in remaining_letters}
    return max(freq.items(), key=lambda item: item[1])[0]


# Returns True iff the given word is possible under the given board
def match_board(board, word):
    for b, l in zip(board, word):
        if b is not None and b != l:
            return False
    return True


# Given the answer, run the game using the optimal strategy
# Return the number of incorrect guesses
def run_game(answer, printing=True):
    answer_length = len(answer)
    remaining_words = {w for w in WORDS if len(w) == answer_length}

    board = [None for _ in range(answer_length)]
    remaining_letters = set(LETTERS)
    incorrect_guesses = 0

    if printing:
        print(' '.join('_' if b is None else b for b in board))
        print(f'Remaining: {len(remaining_words)}\n')

    while(any(b is None for b in board)):
        guess = optimal_guess(remaining_words, remaining_letters)
        remaining_letters.remove(guess)
        occurrences = 0
        for i in range(answer_length):
            if answer[i] == guess:
                occurrences += 1
                board[i] = guess
        if occurrences == 0:
            incorrect_guesses += 1
            remaining_words = {w for w in remaining_words if guess not in w}
        else:
            remaining_words = {w for w in remaining_words if match_board(board, w)}
        
        if printing:
            print(f'Guess: {guess}\t{"✗" if occurrences == 0 else "✓"}')
            print(' '.join('_' if b is None else b for b in board))
            print(f'Remaining: {len(remaining_words)}\n')

    return incorrect_guesses
    



if __name__ == '__main__':
    answer = random_word()
    num_incorrect = run_game(answer)
    print(f'Incorrect guesses for "{answer}": {num_incorrect}')
