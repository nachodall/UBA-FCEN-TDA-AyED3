class DisjSet: 
    def __init__(self): 
        # Constructor to create and initialize sets
        self.rank = {}
        self.parent = {}

    # Make a new set with a single item
    def make_set(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    # Finds set of given item x
    def find(self, x): 
        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x] 

    # Do union of two sets represented by x and y
    def union(self, x, y): 
        xset = self.find(x) 
        yset = self.find(y) 

        if xset == yset: 
            return

        if self.rank[xset] < self.rank[yset]: 
            self.parent[xset] = yset 
        elif self.rank[xset] > self.rank[yset]: 
            self.parent[yset] = xset 
        else: 
            self.parent[yset] = xset 
            self.rank[xset] += 1

# Driver code 
ds = DisjSet()

# Make sets for characters
for char in ['a', 'b', 'c', 'd', 'e']:
    ds.make_set(char)

# Perform union operations
ds.union('a', 'c') 
ds.union('e', 'c') 
ds.union('d', 'b') 

# Check if 'e' and 'a' are in the same set
if ds.find('e') == ds.find('a'): 
    print('Yes') 
else: 
    print('No') 

# Check if 'b' and 'a' are in the same set
if ds.find('b') == ds.find('a'): 
    print('Yes') 
else: 
    print('No') 
