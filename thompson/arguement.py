import regex
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--v', '--version', action='version', version='Version two', help="This arguement shows the version number of the program")
parser.add_argument('--i', '--info ', action='version', version='Information', help="For the program we are executing a regular expression with strings using Thompsons's Algorithm")
parser.add_argument('--e', '--editor', action='version', version='Jack Haugh', help="The creator and editor for this project was Jack Haugh")
parser.add_argument('--l', '--Language', action='version', version='Language', help="We used the python language for the coding while using a virtual machine from google cloud platform.")
args = parser.parse_args()

def main ():
    print("hello there")

if __name__  == "__main__":
    main()

