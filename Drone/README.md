# Main structure
drone.py is including a class:

    class DroneStatus()
with two main method:

    def __init__(self, text)
is written for getting drone log for a text called _Signal.text.And it's including two arguments--_self and _text . 
'''while    
'''

    def get_status(self, index)
for getting status of drone based on log.  
# Test case
I used Signal.text for log input:
 ''' plane1 1 1 1
  plane1 1 1 1 1 2 3
  plane1 2 3 4 1 1 1
  plane1 3 4 5
  plane1 1 1 1 1 2 3
  plane1 2 3 4 1 1 1
'''
and a loop for index input:

    for i in range(7)

and the output is:    
'''plane1 0 1 1 1
   plane1 1 2 3 4
   plane1 2 3 4 5
   plane1 3 3 4 5
   Error: 4
   Error: 5
   Cannot find 6
'''
# Programmer
Dilmuratjan [GitHub](https://github.com/Dilmuratjan)
