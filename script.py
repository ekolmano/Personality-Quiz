"""script storing my project"""

import sys
sys.path.append('../')

import modules.functions as fn


result = fn.quiz()

print("Your favorite coding language is ")
print(result)
