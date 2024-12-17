import struct

def read_ascii_stl(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    vertices = []
    for line in lines:
        parts = line.strip().split()
        if parts[0] == 'vertex':
            vertices.append([float(parts[1]), float(parts[2]), float(parts[3])])
    return vertices

def write_binary_stl(file_path, vertices):
    with open(file_path, 'wb') as f:
        f.write(struct.pack('<80s', b'Binary STL file'))
        f.write(struct.pack('<I', len(vertices) // 3))
        for i in range(0, len(vertices), 3):
            f.write(struct.pack('<3f', 0.0, 0.0, 0.0))  # normal vector
            for j in range(3):
                f.write(struct.pack('<3f', vertices[i + j][0], vertices[i + j][1], vertices[i + j][2]))
            f.write(struct.pack('<H', 0))  # attribute byte count

ascii_stl_path = 'google.stl'
binary_stl_path = 'google_binary.stl'

vertices = read_ascii_stl(ascii_stl_path)
write_binary_stl(binary_stl_path, vertices)

print(f'Converted {ascii_stl_path} to {binary_stl_path}')
