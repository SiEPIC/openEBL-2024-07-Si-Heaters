import os, sys, yaml

"""
Load YAML file and check that the format is correct

"""

num_errors = 0

print('Checking YAML file:')

# YAML file to run verification on
if len(sys.argv)>1:
    yaml_file = sys.argv[1]
else:
    # debugging:
    import os
    yaml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'submissions/Example.yaml')

try:
    with open(yaml_file, 'r') as file:
        yaml_data = yaml.safe_load(file)
except:
   print(' - Error loading layout: %s' % yaml_file)
   num_errors += 1
    
try:
    print(' - number of Devices: %s' % len(yaml_data['Devices']))
    for r in yaml_data['Devices']:
        print('   - Device: %s' % r)
except:
    print(" - No 'Devices' found.")
    num_errors += 1
    
try:
    print(' - number of Sequences: %s' % len(yaml_data['Sequences']))
    for r in yaml_data['Sequences']:
        print('   - Sequence: %s' % r)
except:
   print(" - No 'Sequence' found.")
   num_errors += 1


# Print the result value to standard output
print(num_errors)

