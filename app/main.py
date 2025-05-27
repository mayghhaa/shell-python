import sys


def main():
    # Uncomment this block to pass the first stage
   

    # Wait for user input
    # input()
    while True:
        sys.stdout.write("$ ")
        command = input()


        # exit command 
        if command[:4] == "exit":
            sys.exit(0)

        # echo command 

        if command[:4] == "echo":
            print(f"{command[4:]}")
        
        print(f"{command}: command not found")



if __name__ == "__main__":
    main()
