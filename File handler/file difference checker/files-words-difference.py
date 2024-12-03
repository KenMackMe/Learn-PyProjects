import difflib
from colorama import Fore, Style


def compare_files_words(file1, file2):
    with open(file1, 'r') as f3, open(file2, 'r') as f4:
        content1 = f3.read().split()
        content2 = f4.read().split()

    diff = difflib.ndiff(content1, content2)
    print('\nTracking and highlighting every word change in File 2 Compared to File 1:\n')
    position = 0
    for line in diff:
        if line.startswith('+ '):
            print(f'Position {Fore.BLUE}{position}{Style.RESET_ALL} Added word:'
                  f' {Fore.GREEN}+ {line[2:]}{Style.RESET_ALL}\n')
        elif line.startswith('- '):
            print(f'Position {Fore.BLUE}{position}{Style.RESET_ALL} Removed word:'
                  f' {Fore.RED}- {line[2:]}{Style.RESET_ALL}\n')
        position += 1


compare_files_words('My-file1.txt', 'My-file2.txt')
