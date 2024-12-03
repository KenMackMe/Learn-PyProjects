import difflib  # For finding differences between the contents of the two files
from colorama import Fore, Style  # For adding color to the console output for better visibility


def compare_files_words(file1, file2):
    # Open the files and read their contents
    with open(file1, 'r') as f3, open(file2, 'r') as f4:
        # Read the files and split the content into words (creates a list of words for each file)
        content1 = f3.read().split()
        content2 = f4.read().split()

    # Use difflib's ndiff method to generate a list of differences at the word level
    diff = difflib.ndiff(content1, content2)
    print('\nTracking and highlighting every word change in File 2 Compared to File 1:\n')

    position = 0
    # Loop through each difference and identify changes
    for line in diff:
        # If the line starts with '+ ', it means a word was added in file2 compared to file1
        if line.startswith('+ '):
            print(f'Position {Fore.BLUE}{position}{Style.RESET_ALL} Added word:'
                  f' {Fore.GREEN}+ {line[2:]}{Style.RESET_ALL}\n')

        # If the line starts with '- ', it means a word was removed in file2 compared to file1
        elif line.startswith('- '):
            print(f'Position {Fore.BLUE}{position}{Style.RESET_ALL} Removed word:'
                  f' {Fore.RED}- {line[2:]}{Style.RESET_ALL}\n')
        position += 1


# Specify the file paths for comparison
compare_files_words('My-file1.txt', 'My-file2.txt')
