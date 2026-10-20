"""
Traveling Salesperson Problem (TSP) using Dynamic Programming.
Uses bitmasks to represent visited cities and memoization to avoid
recomputing the same (current city, visited set) state.
Run: python Project7_TSP_DP.py
"""

from functools import lru_cache
import itertools

CITIES = ["A", "B", "C", "D"]
# Symmetric distance matrix: distance[i][j] is the cost from city i to j.
DISTANCE = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]
N = len(CITIES)
ALL_VISITED = (1 << N) - 1


def tsp_dp():
    """Return minimum tour cost, best route, and memoized DP states."""
    parent = {}

    @lru_cache(maxsize=None)
    def dp(current, mask):
        # Base case: all cities visited; return to the starting city A (index 0).
        if mask == ALL_VISITED:
            return DISTANCE[current][0]

        best_cost = float("inf")
        best_next = None

        # Try each city that has not been visited yet.
        for nxt in range(N):
            if mask & (1 << nxt) == 0:
                new_mask = mask | (1 << nxt)
                cost = DISTANCE[current][nxt] + dp(nxt, new_mask)
                if cost < best_cost:
                    best_cost = cost
                    best_next = nxt

        parent[(current, mask)] = best_next
        return best_cost

    start_mask = 1  # Only city A is visited initially.
    minimum_cost = dp(0, start_mask)

    # Reconstruct the optimal route by following stored choices.
    route = [0]
    current, mask = 0, start_mask
    while mask != ALL_VISITED:
        nxt = parent[(current, mask)]
        route.append(nxt)
        mask |= 1 << nxt
        current = nxt
    route.append(0)

    # Generate the reachable DP states for display.
    raw_states = dp_states(dp)
    states = []
    for (current, mask), cost in sorted(raw_states.items(), key=lambda item: (item[0][1].bit_count(), item[0][1], item[0][0])):
        states.append((CITIES[current], mask, visited_names(mask), cost))

    return minimum_cost, [CITIES[i] for i in route], states


def visited_names(mask):
    return "{" + ", ".join(CITIES[i] for i in range(N) if mask & (1 << i)) + "}"


def dp_states(dp_function):
    """Generate reachable DP states by evaluating the memoized recurrence."""
    table = {}
    for size in range(1, N + 1):
        for subset in itertools.combinations(range(N), size):
            if 0 not in subset:
                continue
            mask = sum(1 << i for i in subset)
            for current in subset:
                if current == 0 and size != 1:
                    # A can be the current city only in the initial state.
                    continue
                if current != 0 and size == 1:
                    continue
                table[(current, mask)] = dp_function(current, mask)
    return table


def main():
    minimum_cost, route, states = tsp_dp()
    print("TSP using Dynamic Programming")
    print("-----------------------------")
    print("Cities:", " -> ".join(CITIES))
    print("Minimum tour:", " -> ".join(route))
    print("Minimum tour cost:", minimum_cost)
    print("\nSample DP states (current city, visited set, minimum remaining cost):")
    for current, mask, visited, cost in states:
        print(f"  ({current}, {visited}) -> {cost}")


if __name__ == "__main__":
    main()
