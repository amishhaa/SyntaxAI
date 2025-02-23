import ast
import random

from collections import defaultdict, deque

class MapModule:
    def __init__(self):
        self.map_type = defaultdict(set) 
        self.node_weights = defaultdict(int) 

    def predict_snippet(self, code):
        tree = ast.parse(code)
        context_node = self.bfs_ast(tree)  
        if not context_node:
            return "None"
        node_type = type(context_node).__name__
        if node_type in self.map_type:
            candidates = list(self.map_type[node_type])
            weights = [self.node_weights.get(type(candidate).__name__, 1) for candidate in candidates]
            predicted_node = random.choices(candidates, weights=weights, k=1)[0]
            return ast.unparse(predicted_node) 
        return "None"

    def bfs_ast(self, tree):
        queue = deque([tree])
        path = []
        while queue:
            node = queue.popleft()
            if hasattr(node, "body"):
                path.append(node)
            for child in ast.iter_child_nodes(node):
                self.map_type[type(node).__name__].add(child) 
                self.node_weights[type(child).__name__] += 1 
                queue.append(child) 
        return path[-1] if len(path) > 1 else None  

    def is_single_line(self, node):
        return isinstance(node, (ast.Assign, ast.Expr, ast.Call, ast.Return))
