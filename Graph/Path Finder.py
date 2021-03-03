class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print("graph dict:", self.graph_dict)

    def get_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_path(node, end, path)
                for p in new_path:
                    paths.append(p)

        return paths


if __name__ == '__main__':
    routes = [
        ("mumbai", "pune"),
        ("mumbai", "surat"),
        ("surat", "bengaluru"),
        ("pune", "hyderabad"),
        ("hyderabad", "bengaluru"),
        ("hyderabad", "chennai"),
        ("mysuru", "bengaluru"),
        ("chennai", "bengaluru")
    ]

    route_graph = Graph(routes)
    start = "mumbai"
    end = "bengaluru"

    print(f"path between {start} and {end} is:", route_graph.get_path(start, end))
