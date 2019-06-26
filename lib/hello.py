#default is world
#Author: Shubham Singh (ssingh@tavisca.in)
from greeter import Greeter
import sys

def main():
	if len(sys.argv)>1:
		name=sys.argv[1]
	else:
		name="world"

	gr=Greeter(name)
	gr.greet()


if __name__ == '__main__':
	main()
