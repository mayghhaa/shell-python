import sys

COMMAND_LIST=["echo", "type","exit"]


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
        elif command[:5] == "echo ":
            print(f"{command[5:]}")
        elif command[:4] =="type":
            if command[5:] in COMMAND_LIST:
                print(f"{command[5:]} is a shell builtin")
        else:
            print(f"{command}: not found")



if __name__ == "__main__":
    main()
