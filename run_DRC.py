import pya
import os
import sys
"""
Load a layout file passed through the commmand line 
Run DRC verification.

Lukas Chrostowski 2024/07/12

"""

num_errors = 0

# gds file to run verification on
if len(sys.argv)>1:
    gds_file = sys.argv[1]
else:
    # debugging:
    import os
    gds_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'submissions/EBeam_heaters_BraggGratingwithHeater.gds')

if "framework/EBL_Framework_1cm_PCM_static" in gds_file:
    exit()

# load into layout
try:
   # load into layout
   layout = pya.Layout()
   layout.read(gds_file)
except:
   print('Error loading layout\n')
   num_errors = 1

# get top cell from layout
try:
   # get top cell from layout
   if len(layout.top_cells()) != 1:
      print('Error: the layout needs to have only 1 top cell. It has %s.\n' % len(layout.top_cells()))
      num_errors += 1
   top_cell = layout.top_cell()
except:
   print('Unknown error occurred (top cell check).\n')
   num_errors += 1

try:
   # Make sure layout extent fits within the allocated area.
   cell_Width = 440000
   cell_Height = 470000
   bbox = top_cell.bbox()
   if bbox.width() > cell_Width or bbox.height() > cell_Height:
      print('Error: Cell bounding box / extent (%s, %s) is larger than the maximum size of %s X %s microns' % (bbox.width()/1000, bbox.height()/1000, cell_Width/1000, cell_Height/1000) )
      num_errors += 1
except:
   print('Unknown error occurred (floor plan check).\n')
   num_errors += 1


'''
# run verification
# Not possible via Python pya module
# https://www.klayout.de/forum/discussion/2108/build-qt-ui-in-python-module-to-run-drc
drc_interpreter = pya.Interpreter.ruby_interpreter()
drc_interpreter.define_variable("input", layout)
drc_script = os.path.join(layout.technology().base_path(), "drc/SiEPIC_EBeam.drc")
m = pya.Macro.new(drc_script)
m.interpreter=pya.Macro.Ruby
m.run()
'''

# run verification
rule_table_space_width = [
    ['Silicon 1/0', 1,0,70,60],
    ['Silicon Nitride 1/5', 1,5,120,120],
    ['M1 Heater 11/0', 11,0,3000,3000],
    ['M2 Routing metal', 12,0,8000,5000],
    ['Metal Pad open', 13,0,10000,10000],
]

def check_space_width (cell, rule_table_space_width, tolerance=1):
    '''
    KLayout DRC checking using pya.Region.  
    Input:
        cell: pya.Cell
        rule_table_space_width: [
            ['name', layer_number, data_type, min_space, min_size]
            ]
        min_space, min_size: Int, in database units
        tolerance: int, subtract from the rule
    '''

    errors = 'Manufacturing Design Rule Check (DRC):\n'
    num_errors = 0
    for rule in rule_table_space_width:
        r = pya.Region(cell.begin_shapes_rec(cell.layout().layer(rule[1], rule[2])))
        e = r.space_check(rule[3]-tolerance, ignore_angle=80, metrics=pya.Region.Euclidian)
        if e:
            errors += ' - Layer %s, Space %s nm minimum, %s error(s).\n' % (rule[0], rule[3], len(e))
            num_errors += len(e)
        e = r.width_check(rule[4]-tolerance, ignore_angle=80, metrics=pya.Region.Euclidian)
        if e:
            errors += ' - Layer %s, Width %s nm minimum, %s error(s).\n' % (rule[0], rule[4], len(e))
            num_errors += len(e)
    if num_errors == 0:
        errors += ' - No Space/Width errors detected.\n'
    return num_errors, errors

try:
    num_errors1, errors = check_space_width (layout.top_cell(), rule_table_space_width)
    num_errors += num_errors1
except:
   print('Unknown error occurred (DRC check_space_width).\n')
   num_errors += 1

print(errors)

# Print the result value to standard output
print(num_errors)

