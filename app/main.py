import sys


def main():
    # Uncomment this block to pass the first stage
   

    # Wait for user input
    # input()
    while True:
        sys.stdout.write("$ ")
        command = input()
        print(f"{command}: command not found")


        if command.strip() == "exit(0)":
            sys.exit(0)  # or just use exit(0)

        if command[:4] == "exit":
            sys.exit(0)

if __name__ == "__main__":
    main()
