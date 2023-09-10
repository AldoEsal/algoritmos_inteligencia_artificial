graph = {'a':{'b':2, 'f':1},
'b':{'a':2, 'c':2, 'd':2},
'c':{'b':2, 'e':3, 'z':1},
'd':{'b':2, 'e':4, 'f':3},
'e':{'c':3, 'd':4, 'g':7},
'f':{'a':1, 'd':3, 'g':5},
'g':{'e':7, 'f':5, 'z':6},
'z':{'c':1, 'g':6}
}

def dijikstra (graph, ini, fin):
    
     shortest_distance = {}
     track_predecessor = {}
     unseenNodes = graph
     infinity = 9999999
     track_path =[]
     
     for node in unseenNodes:
         shortest_distance[node] = infinity
     shortest_distance[ini] = 0
     
     while unseenNodes: 
         min_distance_node = None
         for node in unseenNodes:
             if min_distance_node is None:
                 min_distance_node = node
             elif shortest_distance[node] < shortest_distance[min_distance_node]:
                 min_distance_node = node
         path_options = graph[min_distance_node].items()
         
         for child_node, weight in path_options:
             if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                 shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                 track_predecessor[child_node] = min_distance_node
         unseenNodes.pop(min_distance_node)        
     currentNode = fin

     while currentNode != ini:         
         try:
             track_path.insert(0, currentNode)
             currentNode =track_predecessor[currentNode]
         except KeyError:
             print("Camino no valido")
             
     track_path.insert(0,ini)
     
     if shortest_distance[fin] != infinity:
         print("Camino mas corto: " + str(shortest_distance[fin]))
         print("Mejor camino: " + str(track_path))
         
         
dijikstra(graph, 'b', 'g')