class Museum:
    def __init__(self, values, weights, capacity):
        self.values = values
        self.weights = weights
        self.capacity = capacity
        self.n = len(values) - 1  # ignore index 0 for simplicity

    def solve(self):
        n, c_max = self.n, self.capacity
        values, weights = self.values, self.weights

        # Initialize DP matrix S
        S = [[0] * (c_max + 1) for _ in range(n + 1)]

        # Fill DP table
        for i in range(1, n + 1):
            for w in range(1, c_max + 1):
                if weights[i] <= w:
                    S[i][w] = max(values[i] + S[i - 1][w - weights[i]], S[i - 1][w])
                else:
                    S[i][w] = S[i - 1][w]

        # Backtrack to find chosen items
        chosen_items = []
        w = c_max
        for i in range(n, 0, -1):
            if S[i][w] != S[i - 1][w]:
                chosen_items.append(i)
                w -= weights[i]
        chosen_items.reverse()

        # Calculate stats
        num_subsets = 2**n
        matrix_size = (n + 1) * (c_max + 1)
        total_weight = sum(weights[i] for i in chosen_items)
        total_value = sum(values[i] for i in chosen_items)

        # Print results
        print(f"Total possible subsets: {num_subsets}")
        print(f"Size of DP matrix S: {matrix_size} ({n+1} x {c_max+1})")
        print(f"Number of items in optimal subset: {len(chosen_items)}")
        print(f"Total weight of chosen items: {total_weight} (capacity = {c_max})")
        print(f"Total value of chosen items: {total_value}")
        print(f"Chosen items: {chosen_items}")
