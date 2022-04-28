import numpy as np
import sys
import pickle

KEY_WORD = ''
magnitudes = {}

def get_constraints(guess, prev_constraints):
  for i in range(len(KEY_WORD)):
    if guess[i] == KEY_WORD[i]:
      prev_constraints['green'][guess[i]] = i
    if guess[i] in KEY_WORD and KEY_WORD[i] != guess[i]:
      prev_constraints['yellow'][guess[i]] = i
    if guess[i] not in KEY_WORD:
      prev_constraints['grey'].add(guess[i])
  return prev_constraints

def validate(constraints, word):
    if len(word) != 5:
      return False
    for character in word:
      if character in constraints['grey']:
        return False
    for character in constraints['yellow']:
      if not (character in word and word[constraints['yellow'][character]] != character):
        return False
    for character in constraints['green']:
      if word[constraints['green'][character]] != character:
        return False
    return True


def solve(candidates, prev_constraints, guess, count):
  count += 1
  if guess == KEY_WORD:
    print("Got the word on guess #{}: {}".format(count, guess))
    return count
  else:
    print("Guess #{}: {}".format(count, guess))
    if count == 6:
      print("Failed")
      return 'FAIL'

  new_candidates = []

  if count == 1:
    prev_constraints = get_constraints(guess, {'grey': set(), 'yellow': {}, 'green':{}})
    for candidate in magnitudes:
      if validate(prev_constraints, candidate):
        new_candidates.append((candidate, magnitudes[candidate]))
  else:
    for candidate in candidates:
      word, vector = candidate
      if validate(prev_constraints, word):
        new_candidates.append((word, vector))

  new_candidates = sorted(new_candidates, key = lambda a:a[1])
  next_guess = new_candidates[0]

  new_constraints = get_constraints(next_guess[0], prev_constraints)
  return solve(new_candidates, new_constraints, next_guess[0], count)


if len(sys.argv) != 3:
  print("usage: python3 wordle_solver.py <answers.txt> <first_guess>")
  exit(-1)

with open('word_norms.pickle', 'rb') as handle:
  magnitudes = pickle.load(handle)

stats = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 'FAIL': 0}

with open(sys.argv[1], 'r') as f:
  answers = f.readlines()
  for answer in answers:
    KEY_WORD = answer.split(': ')[-1].strip().lower()
    print("="*15 + '\n')
    print("Guessing for key word '{}'\n".format(KEY_WORD))
    guesses = solve(None, None, sys.argv[2], 0)
    stats[guesses] += 1
    print('\n' + "="*15)
    print('\n')

print("Final Stats:\n")
for num_guess in stats:
  print("{} guesses: {}".format(num_guess, stats[num_guess]))