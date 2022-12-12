import pandas as pd
import numpy as np

def number_guessing_game():
    print('''
          Selamat datang di permainan tebak Angka
          Silakan tebak angka 0-9 sebanyak 3 kali
          ''')
    
    computer_numbers = np.random.randint(0,9,3)
    user_numbers = []
    for loop in range(3):
        number = int(input(f'Masukkan angka: '))
        user_numbers.append(number)
        
    result = list(user_numbers == computer_numbers)
    output = pd.DataFrame([user_numbers, computer_numbers, result], index=['Angka Anda', 'Angka Komputer', 'Hasil']).T
    print(output)
    
if __name__ == '__main__':
    number_guessing_game()