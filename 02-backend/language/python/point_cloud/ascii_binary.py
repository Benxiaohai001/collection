import struct

def write_binary_ply(vertices, faces, filename):
    # Write header
    header = '''ply
format binary_little_endian 1.0
comment Created in Blender version 4.0.2
element vertex {}
property float x
property float y
property float z
property float nx
property float ny
property float nz
property float s
property float t
element face {}
property list uchar uint vertex_indices
end_header
'''.format(len(vertices), len(faces))

    with open(filename, 'wb') as f:
        f.write(header.encode('utf-8'))

        # Write vertices
        for vertex in vertices:
            f.write(struct.pack('<fff', *vertex[:3]))
            f.write(struct.pack('<fff', *vertex[3:6]))
            f.write(struct.pack('<ff', *vertex[6:]))

        # Write faces
        for face in faces:
            f.write(struct.pack('<B', face[0]))  # number of vertices
            f.write(struct.pack('<IIII', *face[1:]))
            # f.write(struct.pack('<BBB', *face[5:]))

# ASCII PLY data
vertices = [
    [1, 1, 1, 0.5773503, 0.5773503, 0.5773503, 0.625, 0.5],
    [-1, 1, 1, -0.5773503, 0.5773503, 0.5773503, 0.875, 0.5],
    [-1, -1, 1, -0.5773503, -0.5773503, 0.5773503, 0.875, 0.75],
    [1, -1, 1, 0.5773503, -0.5773503, 0.5773503, 0.625, 0.75],
    [1, -1, -1, 0.5773503, -0.5773503, -0.5773503, 0.375, 0.75],
    [-1, -1, 1, -0.5773503, -0.5773503, 0.5773503, 0.625, 1],
    [-1, -1, -1, -0.5773503, -0.5773503, -0.5773503, 0.375, 1],
    [-1, -1, -1, -0.5773503, -0.5773503, -0.5773503, 0.375, 0],
    [-1, -1, 1, -0.5773503, -0.5773503, 0.5773503, 0.625, 0],
    [-1, 1, 1, -0.5773503, 0.5773503, 0.5773503, 0.625, 0.25],
    [-1, 1, -1, -0.5773503, 0.5773503, -0.5773503, 0.375, 0.25],
    [-1, 1, -1, -0.5773503, 0.5773503, -0.5773503, 0.125, 0.5],
    [1, 1, -1, 0.5773503, 0.5773503, -0.5773503, 0.375, 0.5],
    [-1, -1, -1, -0.5773503, -0.5773503, -0.5773503, 0.125, 0.75],
]

faces = [
    [4, 0, 1, 2, 3],
    [4, 4, 3, 5, 6],
    [4, 7, 8, 9, 10],
    [4, 11, 12, 4, 13],
    [4, 12, 0, 3, 4],
    [4, 10, 9, 0, 12],
]

# Write to binary PLY file
write_binary_ply(vertices, faces, 'output_binary.ply')
