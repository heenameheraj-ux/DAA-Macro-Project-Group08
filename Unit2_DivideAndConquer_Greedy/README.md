# Greedy Job Sequencing with Deadlines and Profits

## Description

This project implements the Greedy Job Sequencing problem using Python. Each job has a deadline and a profit. The objective is to select and schedule jobs so that the total profit is maximized while satisfying the job deadlines.

The algorithm first sorts jobs in decreasing order of profit. For each job, it searches backward from its deadline and places the job in the latest available time slot.

## Problem Statement

Given a set of jobs, where every job has a deadline and an associated profit, schedule the jobs to maximize total profit. Only one job can be completed in one time slot, and a selected job must be completed on or before its deadline.

## Algorithm

1. Sort jobs by decreasing profit.
2. Find the maximum deadline.
3. Create empty time slots.
4. Consider jobs one by one in decreasing profit order.
5. For each job, search backward from its deadline.
6. Place the job in the latest available slot.
7. If no slot is available, reject the job.
8. Calculate and display the total profit.

See `Algorithm.txt` for the complete pseudocode.

## Example Input

| Job | Deadline | Profit |
|---|---:|---:|
| J1 | 2 | 100 |
| J2 | 1 | 19 |
| J3 | 2 | 27 |
| J4 | 1 | 25 |
| J5 | 3 | 15 |

## Expected Output

Optimal schedule:

- Slot 1 -> J3
- Slot 2 -> J1
- Slot 3 -> J5

Maximum total profit = **142**

## Prompt Used

See `Prompt.txt`.

The faculty instructions require submitting both the prompt and the AI-generated visualization. After generating the visualization with the prompt, save the final AI-generated image as `Visualization.png`.

## Visualization

`Visualization.png` contains the decision-flow representation of the greedy job sequencing process.

## Learning Outcome

- Understood the Greedy Job Sequencing problem.
- Learned how deadlines and profits affect job selection.
- Understood the greedy choice of selecting higher-profit jobs first.
- Learned how to place jobs in the latest available slot.
- Practiced prompt-based algorithm visualization.
- Practiced documenting and organizing a DAA project for GitHub.

## Files

- `Project4_JobSequencing.py` - Python implementation.
- `Algorithm.txt` - Algorithm and pseudocode.
- `Prompt.txt` - AI prompt for the required flowchart.
- `Visualization.png` - Flowchart/visualization.
- `README.md` - Project documentation.

## Note

The PDF's sample repository structure names the Unit II source file as `Project4_JobSequencing.cpp`. This project uses `Project4_JobSequencing.py` instead because the requested implementation language is Python.
