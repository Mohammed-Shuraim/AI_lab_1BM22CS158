# -*- coding: utf-8 -*-
"""alphaBeta.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UfAeZT5zf-9CQe94uwPLd0wi2yPS1prv
"""

class AlphaBetaPruningWithPath:
    def __init__(self, tree):
        self.tree = tree  # Represent the tree as a dictionary {node: [children]}
        self.path = []  # To track the optimal path

    def alphabeta(self, node, depth, alpha, beta, maximizingPlayer):
        if depth == 0 or node not in self.tree:
            return node  # Assuming `node` itself is the heuristic value for simplicity

        if maximizingPlayer:
            maxEval = float('-inf')
            bestChild = None
            for child in self.tree[node]:
                eval = self.alphabeta(child, depth - 1, alpha, beta, False)
                if eval > maxEval:
                    maxEval = eval
                    bestChild = child
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cutoff
            if bestChild is not None:
                self.path.append(bestChild)  # Add to path
            return maxEval
        else:
            minEval = float('inf')
            bestChild = None
            for child in self.tree[node]:
                eval = self.alphabeta(child, depth - 1, alpha, beta, True)
                if eval < minEval:
                    minEval = eval
                    bestChild = child
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cutoff
            if bestChild is not None:
                self.path.append(bestChild)  # Add to path
            return minEval

# Running Alpha-Beta Pruning with path tracking
algorithm = AlphaBetaPruningWithPath(tree)
algorithm.path.append('A')  # Starting from root
result = algorithm.alphabeta('A', 3, float('-inf'), float('inf'), True)
optimal_path = algorithm.path

result, optimal_path