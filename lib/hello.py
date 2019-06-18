#default is world
#Author: Shubham Singh (ssingh@tavisca.in)
from greeter import Greeter
import sys
if len(sys.argv)>1:
	name=sys.argv[1]
else:
	name="world"

gr=Greeter(name)
gr.greet()

