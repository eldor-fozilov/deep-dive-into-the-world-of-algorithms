import random


def min_cut(graph_dict):
  deleted_edges = {}
  while len(graph_dict) > 2:
    # we get all of the existing vertices
    vertices = [vertex for vertex in graph_dict.keys()]
    # choose a random edge
    random_vertex = random.choice(vertices)
    sample_space = graph_dict[random_vertex]
    adjacent_vertex = random.choice(sample_space)

   # delete the connection between the adjacent vertex and all other vertices    
    for key in graph_dict[adjacent_vertex]:
      while adjacent_vertex in graph_dict[key]:
        graph_dict[key].remove(adjacent_vertex)


    
    if random_vertex in graph_dict[adjacent_vertex]:
      graph_dict[adjacent_vertex].remove(random_vertex)

    # create edges with random_vertex and other keys corresponding to adjacent_vertex key
    for vertex in graph_dict[adjacent_vertex]:
      if vertex in graph_dict.keys():
        graph_dict[vertex].append(random_vertex)
    
    # add all the connections of the adjacent_vertex, the one to be deletted,
    # to the random_vertex (duplicates also)     
    graph_dict[random_vertex] += graph_dict[adjacent_vertex]
    

    if len(deleted_edges) == 0 or random_vertex not in deleted_edges.keys():
      deleted_edges[random_vertex] = [adjacent_vertex]
    else:
      deleted_edges[random_vertex].append(adjacent_vertex)
      if adjacent_vertex in deleted_edges.keys():
        deleted_edges[random_vertex] += deleted_edges[adjacent_vertex]
        del deleted_edges[adjacent_vertex]
    
    del graph_dict[adjacent_vertex]

  print(graph_dict)
  
def main():
    graph_dict = {}
    with open("MinCut.txt") as lists:
        for list in lists.readlines():
          split = list.split('\t')
          graph_dict[int(split[0])] = [int(i) for i in split[1:-1]]
          #The dict keys are nodes.
          #The dict values are the list of edge targets from this node.
    min_cut(graph_dict)


main()