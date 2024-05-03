import os, sys, yaml

"""
Load YAML file and check that the format is correct

"""

# gds file to run verification on
yaml_file = sys.argv[1]
print(yaml_file)

with open(yaml_file, 'r') as file:
    yaml_data = yaml.safe_load(file)

print(yaml_data)

print(' - number of devices: %s' % len(yaml_data['Devices']))
print(' - number of routines: %s' % len(yaml_data['Routines']))
for r in yaml_data['Routines']:
    print('   - routine: %s' % r)
