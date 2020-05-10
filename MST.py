import copy

class edge:
    def __init__(self , src , dest , weight):
        self.src = src
        self.dest = dest
        self.weight = weight


class DSU:
    def __init__(self, noofnode):
        self.node = noofnode
        self.arr = {}
        for i in range(noofnode):
            self.arr[i] = i

    def getParent(self , node):
        #print(node)
        #print(type(self.arr[node]))
        if self.arr[node] == node:
            return self.arr[node]
        else:
            return self.getParent(self.arr[node])


    def isConect(self, node1 , node2):
        parentOfNode1 = self.getParent(node1)
        parentOfNode2 = self.getParent(node2)
        if parentOfNode1 == parentOfNode2:
            return True
        else:
            self.arr[parentOfNode1] = parentOfNode2
            #print(self.arr)
            return False
class minSpanningTree:
    def __init__(self):
        self.edges = []
    def addEdge(self , edge):
        self.edges.append(edge)

    def printMST(self):
        print("=== MST ===")
        for edge in self.edges:
            print(edge[1] , edge[2])

class Graph:
    def __init__(self , noOfNode):
        self.node = noOfNode
        self.edges = []

    def printE(self):
        print(self.edges)
    def addEdge(self , edge):
        self.edges.append(edge)

    def kruskal(self):
        sum = 0
        check = DSU(self.node)
        MST = minSpanningTree()
        self.edges.sort(key=lambda tup : tup[0])
        i = 0
        while len(MST.edges) != self.node-1 and i < len(self.edges):
            if not check.isConect(self.edges[i][1] , self.edges[i][2]):
                sum += self.edges[i][0]
                MST.addEdge(self.edges[i])
            i+=1
        return MST , sum

def handleInput(ip):
    arr = ip.split(" ")
    #print(arr)
    return int(arr[0] ),int(arr[1]),int(arr[2].replace("\n" , ""))

def main():
    #the no of node is = 9 and edge 14
    noOfNode = int(input("Enter no of nodes ?"))
    noOfEdges = int(input("Enter no of edges ?"))
    # noOfMST = int(input("Enter no of MST ?"))
    k =4
    graph = Graph(noOfNode)

    f = open("input.txt" , "r")
    for i in f:
        src, dest, w = handleInput(i)
        graph.addEdge([w, src, dest])

    mst ,sum = graph.kruskal()
    mst.printMST()
    print(" => sum = " + str(sum))
    print("========")

    for i in range(k-1):
        final = [[0,0]]
        sum = 1e9
        edges = []
        for edge in mst.edges:
            edges.append(edge)
        for edge1 in edges:
            tempGraph = copy.deepcopy(graph)
            for edge2 in tempGraph.edges:
                if edge1[0] == edge2[0] and edge1[1] == edge2[1] and edge1[2] == edge2[2]:
                    edge2[0] = 1e9
                    break
            tempMST , tempSum = tempGraph.kruskal()
            if tempSum < sum:
                final[0] = [tempMST , tempSum]
                graph = copy.deepcopy(tempGraph)
                sum = tempSum
        mst = final[0][0]
        final[0][0].printMST()
        print(" => sum = " + str(final[0][1]))
        print("========")

if "__main__" == __name__:
    main()