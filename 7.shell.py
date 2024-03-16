import subprocess
import shlex
import os

def execute_command(command):
    try:
        # Split the command into a list of arguments
        args = shlex.split(command)

        # Check for IO redirection operators
        if '>' in args:
            output_index = args.index('>')
            output_file = args[output_index + 1]
            args = args[:output_index]  # Remove the '>' and the output file from the arguments
            with open(output_file, 'w') as f:
                subprocess.run(args, stdout=f)
        elif '<' in args:
            input_index = args.index('<')
            input_file = args[input_index + 1]
            args = args[:input_index]  # Remove the '<' and the input file from the arguments
            with open(input_file, 'r') as f:
                subprocess.run(args, stdin=f)
        elif '|' in args:
            # Handle piping by splitting the command into multiple subprocess calls
            commands = command.split('|')
            processes = []
            for cmd in commands:
                processes.append(subprocess.Popen(shlex.split(cmd.strip()), stdout=subprocess.PIPE))
            # Wait for all processes to finish
            for p in processes:
                p.wait()
        else:
            # No IO redirection, execute the command as is
            subprocess.run(args)
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        user_input = input("Shell > ")
        if user_input.lower() == 'exit':
            break
        execute_command(user_input)

if __name__ == "__main__":
    main()


#run in terminal 
#$ python 7.shell.py
#Shell > ls -la
#Shell > ls -la > out.txt
#Shell > bc < input.txt
#Shell > ps aux | grep term
