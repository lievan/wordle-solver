# wordle-solver
This program attempts to solve the wordle by sorting possible candidates by the magnitude of their GLOVE word vectors. Word vectors with lower magnitudes tend to occur more frequently.

wordle_solver.py applies this approach to try to solve all the wordles from 2022. 

Run using ```python3 wordle_solver.py <path/to/2022_words.txt> <first guess>```

For example, using 'react' as a first guess, you should see an output like this 


<img width="617" alt="image" src="https://user-images.githubusercontent.com/42917263/165859798-1a1eee98-a036-4249-a5dd-bb5ed000d4ba.png">
