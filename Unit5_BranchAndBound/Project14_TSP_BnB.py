import heapq
import math

INF = math.inf

# Cost matrix for 4 cities: A, B, C, D
cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(cost)


def city_name(city):
    return chr(ord('A') + city)


# Find MST cost among unvisited cities
def mst_cost(cities):

    if len(cities) <= 1:
        return 0

    cities = list(cities)
    visited = {cities[0]}
    total = 0

    while len(visited) < len(cities):

        minimum = INF
        next_city = None

        for u in visited:
            for v in cities:
                if v not in visited and cost[u][v] < minimum:
                    minimum = cost[u][v]
                    next_city = v

        total += minimum
        visited.add(next_city)

    return total


# Calculate a valid lower bound
def calculate_bound(path):

    visited = set(path)
    unvisited = set(range(n)) - visited

    # Cost already paid by the current partial path
    path_cost = 0

    for i in range(len(path) - 1):
        path_cost += cost[path[i]][path[i + 1]]

    # If all cities are visited, complete the tour
    if not unvisited:
        return path_cost + cost[path[-1]][0]

    # Minimum edge from current city to an unvisited city
    current_to_unvisited = min(
        cost[path[-1]][city]
        for city in unvisited
    )

    # Minimum edge from starting city to an unvisited city
    start_to_unvisited = min(
        cost[0][city]
        for city in unvisited
    )

    # Minimum spanning tree connecting all unvisited cities
    remaining_mst = mst_cost(unvisited)

    lower_bound = (
        path_cost
        + current_to_unvisited
        + remaining_mst
        + start_to_unvisited
    )

    return lower_bound


def tsp_branch_and_bound():

    # Priority queue stores:
    # (lower_bound, node_number, path)
    priority_queue = []

    node_number = 0

    initial_path = [0]
    initial_bound = calculate_bound(initial_path)

    heapq.heappush(
        priority_queue,
        (initial_bound, node_number, initial_path)
    )

    best_cost = INF
    best_path = None

    print("==============================================")
    print("   TSP USING LEAST-COST BRANCH AND BOUND")
    print("==============================================")

    print("\nCost Matrix:")

    for row in cost:
        print(row)

    print(f"\nInitial Lower Bound = {initial_bound}")

    print("\n--- Branching Process ---")

    while priority_queue:

        bound, _, path = heapq.heappop(priority_queue)

        path_string = " -> ".join(
            city_name(city) for city in path
        )

        # Pruning condition
        if bound >= best_cost:

            print(
                f"PRUNED: {path_string}"
                f" | Bound = {bound}"
                f" >= Best Cost = {best_cost}"
            )

            continue

        # All cities visited
        if len(path) == n:

            total_cost = (
                sum(
                    cost[path[i]][path[i + 1]]
                    for i in range(n - 1)
                )
                + cost[path[-1]][0]
            )

            print(
                f"COMPLETE TOUR: {path_string} -> A"
                f" | Cost = {total_cost}"
            )

            if total_cost < best_cost:

                best_cost = total_cost
                best_path = path[:]

                print(
                    f"NEW BEST COST = {best_cost}"
                )

            continue

        # Generate branches
        for next_city in range(1, n):

            if next_city in path:
                continue

            child_path = path + [next_city]

            child_bound = calculate_bound(child_path)

            child_path_string = " -> ".join(
                city_name(city) for city in child_path
            )

            print(
                f"BRANCH: {child_path_string}"
                f" | Bound = {child_bound}"
            )

            node_number += 1

            heapq.heappush(
                priority_queue,
                (
                    child_bound,
                    node_number,
                    child_path
                )
            )

    print("\n==============================================")
    print("             FINAL RESULT")
    print("==============================================")

    print(
        "Optimal Tour: "
        + " -> ".join(
            city_name(city)
            for city in best_path
        )
        + " -> A"
    )

    print(f"Minimum Cost: {best_cost}")


if __name__ == "__main__":
    tsp_branch_and_bound()