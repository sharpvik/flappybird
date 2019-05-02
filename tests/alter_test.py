# ADD PROJECT ROOT TO sys.path TO ALLOW lib IMPORTS
import sys, os
root_path = os.sep.join( sys.path[0].split(os.sep)[:-1] )
sys.path.append(root_path)



# IMPORTS
from lib.alter import Alter
import unitest



# TESTING
alt = Alter()


tests = [
    # alt.g must be of type float
    type(alt.g) == float or alt.g is None,
    
    # alt.g must be 1.6 <= alt.g <= 360.0
    1.6 <= alt.g <= 360.0,
    
    # alt.s must be of type int
    type(alt.s) == int or alt.s is None,
    
    # alt.s must be 100 <= alt.s <= 1000
    100 <= alt.s <= 1000,
]


unitest.test_logs(tests)
print '\nPercentage passing:', unitest.test_multiple(tests) 