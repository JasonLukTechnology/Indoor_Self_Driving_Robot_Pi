# The distance between each neighbor nodes
# Remember to mark its own distance as 0

G = {1: {1: 0, 2: 3},
     2: {1: 3, 2: 0, 3: 2, 11: 20},
     3: {2: 2, 3: 0, 4: 10, },
     4: {3: 10, 4: 0, 5: 3, 8: 6},
     5: {4: 3, 5: 0, 6: 4},
     6: {5: 3, 6: 0, 7: 10,12:8},
     7: {6: 10, 7: 0},
     8: {4: 6, 8: 0, 9: 2},
     9: {8: 2, 9: 0, 10: 1},
     10: {9: 1, 10: 0, 11: 4},
     11: {2: 20, 10: 4, 11:0, 13:4},
     12: {6: 8, 12:0},
     13: {11: 4, 13:0},
     }

# Names for each node
encode_list = {
    26: "Z",
    25: "Y",
    24: "X",
    23: "W",
    22: "V",
    21: "U",
    20: "T",
    19: "S",
    18: "R",
    17: "Q",
    16: "P",
    15: "O",
    14: "N",
    13: "M",
    12: "L",
    11: "K",
    10: "J",
    9: "I",
    8: "H",
    7: "G",
    6: "F",
    5: "E",
    4: "D",
    3: "C",
    2: "B",
    1: "A",
    }

def Dijkstra(G, v0, INF=999):  # Creat a loop
    dis = dict((i, INF) for i in G.keys())  # Initial a table with distances data
    current_node = v0  # Mark the starting point
    dis[v0] = 0  # initial a starting point
    visited = []  # recorded the path ran throught
    ###
    path = dict((i, []) for i in G.keys())  # Ditionary to save the shortest path
    path[v0] = str(v0)  
    ###
    while len(G) > len(visited):  # Keep looping before it finishs all the walk throught.
        visited.append(current_node)  # Log the current node
        for k in G[current_node]:  # Loop with their neighbor 
            if dis[current_node] + G[current_node][k] < dis[k]:  # If the crrent path is short than the pervious path
                dis[k] = dis[current_node] + G[current_node][k]  # Update the shortest distance
                seq = (path[current_node], str(k))
                sym = '-'
                path[k] = sym.join(seq)  # Save the shortest path
        # Go to the next node
        # Go by the closest node
        new = INF
        for node in dis.keys():
            if node in visited:
                continue
            if dis[node] < new:
                new = dis[node]
                current_node = node
    return dis, path

length_dictionary = len(G)

# This is my way to reorganize the output
# so it can read by my robot
for x1 in range(1, length_dictionary+1):
    dis, path = Dijkstra(G, v0=x1)
    x = str(x1)
    x = x.replace(x, "'{}':".format(encode_list[int(x)]))
    print(x)
    path = str(path)
    for a in range(26, 0,-1):
        path = path.replace("{}:".format(str(a)), "'{}':".format(encode_list[int(a)]))
        path = path.replace(str(a), "{}".format(encode_list[int(a)]))
    path = path.replace("-", "")
    print(path)
    x1 = x1 + 1

# It should generate the simliar output
##
'A':
{'A': 'A', 'B': 'AB', 'C': 'ABC', 'D': 'ABCD', 'E': 'ABCDE', 'F': 'ABCDEF', 'G': 'ABCDEFG', 'H': 'ABCDH', 'I': 'ABCDHI', 'J': 'ABKJ', 'K': 'ABK', 'L': 'ABCDEFL', 'M': 'ABKM'}
'B':
{'A': 'BA', 'B': 'B', 'C': 'BC', 'D': 'BCD', 'E': 'BCDE', 'F': 'BCDEF', 'G': 'BCDEFG', 'H': 'BCDH', 'I': 'BCDHI', 'J': 'BKJ', 'K': 'BK', 'L': 'BCDEFL', 'M': 'BKM'}
'C':
{'A': 'CBA', 'B': 'CB', 'C': 'C', 'D': 'CD', 'E': 'CDE', 'F': 'CDEF', 'G': 'CDEFG', 'H': 'CDH', 'I': 'CDHI', 'J': 'CDHIJ', 'K': 'CBK', 'L': 'CDEFL', 'M': 'CBKM'}
'D':
{'A': 'DCBA', 'B': 'DCB', 'C': 'DC', 'D': 'D', 'E': 'DE', 'F': 'DEF', 'G': 'DEFG', 'H': 'DH', 'I': 'DHI', 'J': 'DHIJ', 'K': 'DCBK', 'L': 'DEFL', 'M': 'DCBKM'}
'E':
{'A': 'EDCBA', 'B': 'EDCB', 'C': 'EDC', 'D': 'ED', 'E': 'E', 'F': 'EF', 'G': 'EFG', 'H': 'EDH', 'I': 'EDHI', 'J': 'EDHIJ', 'K': 'EDCBK', 'L': 'EFL', 'M': 'EDCBKM'}
'F':
{'A': 'FEDCBA', 'B': 'FEDCB', 'C': 'FEDC', 'D': 'FED', 'E': 'FE', 'F': 'F', 'G': 'FG', 'H': 'FEDH', 'I': 'FEDHI', 'J': 'FEDHIJ', 'K': 'FEDCBK', 'L': 'FL', 'M': 'FEDCBKM'}
'G':
{'A': 'GFEDCBA', 'B': 'GFEDCB', 'C': 'GFEDC', 'D': 'GFED', 'E': 'GFE', 'F': 'GF', 'G': 'G', 'H': 'GFEDH', 'I': 'GFEDHI', 'J': 'GFEDHIJ', 'K': 'GFEDCBK', 'L': 'GFL', 'M': 'GFEDCBKM'}
'H':
{'A': 'HDCBA', 'B': 'HDCB', 'C': 'HDC', 'D': 'HD', 'E': 'HDE', 'F': 'HDEF', 'G': 'HDEFG', 'H': 'H', 'I': 'HI', 'J': 'HIJ', 'K': 'HDCBK', 'L': 'HDEFL', 'M': 'HDCBKM'}
'I':
{'A': 'IHDCBA', 'B': 'IHDCB', 'C': 'IHDC', 'D': 'IHD', 'E': 'IHDE', 'F': 'IHDEF', 'G': 'IHDEFG', 'H': 'IH', 'I': 'I', 'J': 'IJ', 'K': 'IJK', 'L': 'IHDEFL', 'M': 'IJKM'}
'J':
{'A': 'JKBA', 'B': 'JKB', 'C': 'JKBC', 'D': 'JIHD', 'E': 'JIHDE', 'F': 'JIHDEF', 'G': 'JIHDEFG', 'H': 'JIH', 'I': 'JI', 'J': 'J', 'K': 'JK', 'L': 'JIHDEFL', 'M': 'JKM'}
'K':
{'A': 'KBA', 'B': 'KB', 'C': 'KBC', 'D': 'KBCD', 'E': 'KBCDE', 'F': 'KBCDEF', 'G': 'KBCDEFG', 'H': 'KBCDH', 'I': 'KJI', 'J': 'KJ', 'K': 'K', 'L': 'KBCDEFL', 'M': 'KM'}
'L':
{'A': 'LFEDCBA', 'B': 'LFEDCB', 'C': 'LFEDC', 'D': 'LFED', 'E': 'LFE', 'F': 'LF', 'G': 'LFG', 'H': 'LFEDH', 'I': 'LFEDHI', 'J': 'LFEDHIJ', 'K': 'LFEDCBK', 'L': 'L', 'M': 'LFEDCBKM'}
'M':
{'A': 'MKBA', 'B': 'MKB', 'C': 'MKBC', 'D': 'MKBCD', 'E': 'MKBCDE', 'F': 'MKBCDEF', 'G': 'MKBCDEFG', 'H': 'MKBCDH', 'I': 'MKJI', 'J': 'MKJ', 'K': 'MK', 'L': 'MKBCDEFL', 'M': 'M'}
##
