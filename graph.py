class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, key):
        if key not in self.vertices:
            self.vertices[key] = {}

    def add_edge(self, vtx1, vtx2, weight=1):
        if vtx1 in self.vertices and vtx2 in self.vertices:
            self.vertices[vtx1][vtx2] = weight
            self.vertices[vtx2][vtx1] = weight  
        else:
            print(f"One or both vertices {vtx1}, {vtx2} not found.")

    def remove_edge(self, vtx1, vtx2):
        if vtx1 in self.vertices and vtx2 in self.vertices:
            self.vertices[vtx1].pop(vtx2, None)
            self.vertices[vtx2].pop(vtx1, None)
        else:
            print(f"One or both vertices {vtx1}, {vtx2} not found.")

    def remove_vertex(self, key):
        if key in self.vertices:
            for neighbor in list(self.vertices[key].keys()):
                self.vertices[neighbor].pop(key, None)
            del self.vertices[key]
        else:
            print(f"Vertex {key} not found.")

    def list_vertices(self):
        for vertex, edges in self.vertices.items():
            edges_str = ", ".join(f"({v}, {w})" for v, w in edges.items())
            print(f"{vertex} -> {edges_str or 'None'}")


