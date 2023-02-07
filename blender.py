import bpy
import random

spacing = 1
for x in range(10):
    for y in range(10):
        locate = (x * spacing, y * spacing, random.random() * 2)
        bpy.ops.mesh.primitive_cube_add(size=2,enter_editmode=False, align='WORLD', location=locate, scale=(random.random(), random.random(), random.random()))

