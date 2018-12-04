import argparse
import sys
import bpy

sys.argv = sys.argv[6:]  # Get rid of the blender arguments

parser = argparse.ArgumentParser(description="Parse arguments")
parser.add_argument("--destfile", dest="destfile", type=str)
parser.add_argument("--width", dest="width", type=int)
parser.add_argument("--height", dest="height", type=int)
parser.add_argument("--depth", dest="depth", type=int)
parser.add_argument("--voxels", dest="voxels", type=str)
args = parser.parse_args()

mat = bpy.data.materials.new(name="Material")
mat.diffuse_color = (0.3, 0.8, 1.0)

x = 0
y = 0
z = 0
for c in args.voxels:
    if c == '1':
        box = bpy.ops.mesh.primitive_cube_add(
            location=(x - args.width//2, y - args.height//2, z - args.depth//2),
            radius=0.5)
        obj = bpy.context.active_object
        if obj.data.materials:
            # assign to 1st material slot
            obj.data.materials[0] = mat
        else:
            # no slots
            obj.data.materials.append(mat)
    x += 1
    if x == args.width:
        x = 0
        y += 1
        if y == args.depth:
            y = 0
            z += 1


bpy.data.scenes["Scene"].render.filepath = args.destfile
bpy.ops.render.render(write_still=True)
