import numpy as np

def generate_4d_off(vertices, edges, faces, cells, filename):
    with open(filename, 'w') as file:
        file.write("OFF\n")
        file.write(f"{len(vertices)} {len(edges)} {len(faces)} {len(cells)}\n")

        for vertex in vertices:
            file.write(f"{vertex[0]} {vertex[1]} {vertex[2]} {vertex[3]}\n")

        for edge in edges:
            file.write(f"{edge[0]} {edge[1]}\n")

        for face in faces:
            file.write(f"{len(face)} {' '.join(map(str, face))}\n")

        for cell in cells:
            file.write(f"{len(cell)} {' '.join(map(str, cell))}\n")

# Example data
vertices = np.random.rand(8, 4)  # 8 vertices in 4D space
# edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4)]
edges = []
faces = [(0, 1, 2, 3), (4, 5, 6, 7)]
cells = [(0, 1, 2, 3, 4, 5, 6, 7)]

generate_4d_off(vertices, edges, faces, cells, '4d_shape.off')

print("4D OFF file generated: 4d_shape.off")
