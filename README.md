step 1: Initialize classes Edge and Vertex
step 2: Topological Sort for the source vertex to generate a sorted vertices
step 3: Initizlize the distance hashmap with -inf  
step 4: Iterate over the sorted vertices and update the distance hashmap
step 5: Return the distance hashmap

Complexity: O(E+V) as it iterate through edges and vertices.
