# Graph Coloring using Backtracking

## Description

This project implements the Graph Coloring problem using the
Backtracking technique.

The objective is to assign one of three colors to each of four
vertices such that no two adjacent vertices have the same color.

## Algorithm

1. Select an uncolored vertex.
2. Try each available color.
3. Check whether the selected color conflicts with any adjacent
   colored vertex.
4. If there is no conflict, assign the color.
5. Move to the next vertex.
6. If all vertices are successfully colored, return SUCCESS.
7. If no valid color is available, backtrack to the previous vertex.
8. Change the previous vertex's color and try another color.
9. Continue until a valid coloring is found or all possibilities
   are exhausted.

## Prompt Used

"Illustrate backtracking steps for coloring a 4-vertex graph using
3 colors. Show the color assignment process, validity checks for
adjacent vertices, backtracking when a color assignment is not
possible, and the final result using a clear flowchart."

## Output

The program successfully colors the four vertices using three colors.

Vertex 1 -> Color 1  
Vertex 2 -> Color 2  
Vertex 3 -> Color 3  
Vertex 4 -> Color 1

## Visualization

The AI-generated visualization shows the graph coloring process,
color validity checks, and the backtracking process.

## Learning Outcome

- Understood the Graph Coloring problem.
- Learned the Backtracking technique.
- Learned how to check whether a color assignment is valid.
- Learned how to visualize an algorithm using AI tools.
- Practiced implementing recursive backtracking in Python.