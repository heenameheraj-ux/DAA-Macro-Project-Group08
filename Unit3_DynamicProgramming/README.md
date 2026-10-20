# Traveling Salesperson Problem using Dynamic Programming

## Description
This project implements the Traveling Salesperson Problem (TSP) using Dynamic Programming for four cities.

## Input Distance Matrix

| City | A | B | C | D |
|---|---:|---:|---:|---:|
| A | 0 | 10 | 15 | 20 |
| B | 10 | 0 | 35 | 25 |
| C | 15 | 35 | 0 | 30 |
| D | 20 | 25 | 30 | 0 |

## How to Run

Ensure Python 3 is installed. Run the following command from the project folder:

```bash
python Project7_TSP_DP.py
```

The program displays the minimum-cost tour and sample Dynamic Programming states.

## Objective
Find the minimum-cost tour that visits every city exactly once and returns to the starting city A.

## Algorithm
The DP state is `dp(current, mask)`, where `current` represents the current city and `mask` represents the visited cities.

- Base case: When all cities are visited, return the cost of travelling back to A.
- Transition: Try every unvisited city and select the minimum total cost.

## Optimal Result
Route: A → B → D → C → A

Minimum tour cost: 80

## Complexity Analysis
- Time Complexity: O(n² × 2ⁿ)
- Space Complexity: O(n × 2ⁿ)

## Project Files
- `Project7_TSP_DP.py` — Python implementation
- `Prompt.txt` — AI visualization prompt
- `Visualization.png` — Algorithm visualization
- `Sample_Output.txt` — Program output
