import ast
import random
from collections import defaultdict, deque

class MapModule:
    def __init__(self):
        self.map_type = defaultdict(set)  
        self.node_weights = defaultdict(int)  
        self.train_from_file("mapmodule/train.py")

    def predict_snippet(self, code):
        try:
            tree = ast.parse(code)
            context_node = self.bfs_ast(tree)  
            if not context_node:
                return "None"

            node_type = type(context_node).__name__
            if node_type in self.map_type:
                candidates = list(self.map_type[node_type])
                weights = [self.node_weights.get(type(candidate).__name__, 1) for candidate in candidates]
                predicted_node = random.choices(candidates, weights=weights, k=1)[0]
                predicted_code = ast.unparse(predicted_node)
                return self.replace_variable_names(predicted_code)  # Replace variable names
            return "None"
        except SyntaxError:
            return "None"

    def bfs_ast(self, tree):
        queue = deque([tree])
        path = []
        while queue:
            node = queue.popleft()
            if self.is_block_level_node(node): 
                path.append(node)
            for child in ast.iter_child_nodes(node):
                self.map_type[type(node).__name__].add(child) 
                self.node_weights[type(child).__name__] += 1 
                queue.append(child)
        return path[-1] if len(path) > 1 else None

    def is_block_level_node(self, node):
        return isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.If, ast.For, ast.While, ast.Try))

    def train_from_file(self, file_path):
        with open(file_path, "r") as file:
            code = file.read()
            tree = ast.parse(code)
            self.bfs_ast(tree)  

    def is_single_line(self, node):
        return isinstance(node, (ast.Assign, ast.Expr, ast.Call, ast.Return))

    def replace_variable_names(self, code):
        """
        Replace variable names in the code with the placeholder constant 'VARCHANGE'.
        """
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                node.id = "VARCHANGE"  # Replace variable name with 'VARCHANGE'
        return ast.unparse(tree)
