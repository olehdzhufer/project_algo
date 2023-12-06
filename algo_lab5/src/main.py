class UnionFind:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}

        for vertex in vertices:
            self.parent[vertex] = vertex
            self.rank[vertex] = 0

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
                return root2, root1
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
                return root1, root2
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1
                return root2, root1

    def wedd(self, pairs):
        boys = set()
        girls = set()

        for pair in pairs:
            human1, human2 = pair
            if human1 % 2:
                boys.add(human1)
            else:
                girls.add(human1)
            if human2 % 2:
                boys.add(human2)
            else:
                girls.add(human2)

        counter = 0
        new_pairs = []
        for girl in girls:
            for boy in boys:
                curr_pair = (girl, boy)
                root_girl = self.find(girl)
                root_boy = self.find(boy)
                if root_girl != root_boy:
                    new_pairs.append(curr_pair)
                    counter += 1

        
        return counter, new_pairs


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        lines = f.readlines()

    vertex = eval(lines[0].strip())
    pairs = eval(lines[1].strip())

    unionFind = UnionFind(vertex)

    result_pairs = []
    for pair in pairs:
        human1, human2 = pair
        result_pairs.append(unionFind.union(human1, human2))

    with open("output.txt", "w") as f:
        f.write(str(unionFind.wedd(result_pairs)))
