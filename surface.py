import sys

argv = sys.argv
x = int(argv[1])
y = int(argv[2])
step = int(argv[3])
speed = int(argv[4])

gcode = []
gcode.append("F{}".format(speed))
gcode.append("G0 Z20")
gcode.append("G0 X0 Y0")
gcode.append("G1 X0 Y0 Z0")

direction = "right"
for y_delta in range(0, y, step):
    if direction == "right":
        gcode.append("G1 X{} Y{}".format(x, y_delta))
        gcode.append("G1 X{} Y{}".format(x, y_delta+step))
        direction = "left"
    else:
        gcode.append("G1 X0 Y{}".format(y_delta))
        gcode.append("G1 X0 Y{}".format(y_delta+step))
        direction = "right"

gcode.append("M2")

print("\n".join(gcode))
