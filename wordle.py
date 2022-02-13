import json
import random 
from typing import List, Tuple
import os
import time

with open('game.json', 'r', encoding='utf-8') as f:
    data: List[List] = json.load(f)
 
def turn_green(a: str) -> str:
    return f'\033[1;32;1m{a}\033[0m' 

def turn_yellow(a: str) -> str:
    return f'\033[1;33;1m{a}\033[0m' 
   
def print_colour(word: str, correct: List[int], might_correct: List[int]) -> str:
    
    output: str = ''
    for i in range(len(word)):
        if i in correct:
            output += turn_green(word[i])
        elif i in might_correct:
            output += turn_yellow(word[i])  
        else:
            output += word[i]
    return output
    
def clear_screen() -> None:
    time.sleep(0.5)
    os.system('cls')
    return
def clear_n_wait() -> None:
    os.system('pause')
    os.system('cls')

def show_matrix(mode:int, time: int):
    raw = '*' * mode
    matrix = [raw for i in range(time)]
    print('\n'.join(matrix))
    return matrix
   
def play_n_check(word: str) -> Tuple[bool, str]:   
    
    correct = []
    might_correct = []
    
    input_ = input('please input the word\n')
    
    if len(word) != len(input_):
        raise TypeError
    
    for i in range(len(input_)):
        
        if input_[i] == word[i]:
            correct.append(i)
            
        elif input_[i] in word:
            might_correct.append(i)
    word_ = print_colour(input_, correct, might_correct)
    
    return ((len(correct) == len(word)), word_ )       
    
def main() -> None:   
    clear_screen()   
    while True:
        mode = int(input("please select a mode to play, 5 or 7\n"))
        if mode != 5 and mode != 7:
            print("please select a correct number\n")
            continue
        break
    
    game_time = 6
    word = random.choice(data[mode == 7])
    matrix = show_matrix(mode, game_time)
    
    while game_time > 0:
        chk, word_ = play_n_check(word)
        clear_n_wait()         
        matrix[6-game_time] = word_
        clear_screen()
        print('\n'.join(matrix))       
        if chk:
            print('you got the word successfully')
            break             
        game_time -= 1
    if game_time == 0:
        print(f"The correct answer is {word}")
    return    
        
main()