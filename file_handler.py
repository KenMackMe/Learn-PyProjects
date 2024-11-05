import os


# Function that contains the predefined text
def text_py():
    return [
        "My name is Kenny, and this program demonstrates how to work with creating, writing, reading and deleting a "
        "file in Python.\n",
        "First, we create a text file called 'test.txt' and give you the option to either write your own text or use "
        "a predefined text.\n"
        "Your file is saved in the current working directory (CWD) This is the folder where your Python script is "
        "running from. If you choose \n"
        "to write your own text you can enter anything you'd like, and it will be saved to the file. Alternatively, "
        "you can use this text that\n",
        "explains the program. After writing the text to the file, the program also gives you the option to delete "
        "the file or keep it for "
        "later use.\n",
        "This program is a simple demonstration of file handling and user interaction, and I hope it gives "
        "you a brief understanding on how\n"
        "files work in python.\n"
    ]



# Function to write and read predefined text to the file

def write():
    with open("test.txt", "w") as f:
        lines = text_py()
        print("file bytes: ")
        for line in lines:
            print(f.write(line))  # Write each line
    with open("test.txt", "r") as f:
        content = f.read() #read text
        print("")
        print(f"Predefined text: {content}")


try:
    # create file
    f = open("test.txt", "x")
    print("File created")
    f.close()

    # Loop for user to choose text input method
    end = False
    while not end:
        user_choice = int(input("Choose: 1 to write your text, 2 to use predefined text: "))
        if user_choice == 1:
            txt = input("Enter your text: ")
            # Write user's text to the file
            with open("test.txt", "w") as f:
                print("file bytes: ", f.write(txt))
            # Read and print the content of the file
            with open("test.txt", "r") as f:
                content = f.read()
                print(f"your file content: {content}")
            end = True

        elif user_choice == 2:
            write()  # Call function to write predefined text
            end = True
        else:
            # Invalid input, ask the user again
            print("Invalid choice.")
            user_words = int(input("Press enter"))

except FileExistsError:
    print("File already exists")  # Handle case if the file already exists
except Exception as e:
    print(f"file error {e}")  # Catch any other errors


# Ask user about deleting the file
delete_me = input("Do you want to delete the file, (y/n)?: ")
stop = False
while not stop:
    if delete_me == 'y':
        if os.path.exists("test.txt"):
            os.remove("test.txt")  # Delete the file
            print("File has been deleted")
        stop = True

    elif delete_me == 'n':
        print("File saved, you can either delete it or modify it in your source folder")
        stop = True
    else:
        print("Error, choose between 'y' and 'n' to delete")
        # Prompt again if input is invalid
        delete_me = input("Do you want to delete the file, (y/n)?: ")
