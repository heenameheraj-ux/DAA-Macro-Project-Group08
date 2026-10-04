class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit


def job_sequencing(jobs):

    # Sort jobs by decreasing profit
    jobs.sort(key=lambda job: job.profit, reverse=True)

    # Find maximum deadline
    max_deadline = max(job.deadline for job in jobs)

    # Create empty time slots
    schedule = [None] * (max_deadline + 1)

    total_profit = 0
    selected_jobs = []

    # Schedule each job
    for job in jobs:

        # Check from deadline towards slot 1
        for slot in range(job.deadline, 0, -1):

            if schedule[slot] is None:

                schedule[slot] = job
                total_profit += job.profit
                selected_jobs.append(job)

                break

    return schedule, selected_jobs, total_profit


# -------------------------------
# MAIN PROGRAM
# -------------------------------

print("===== GREEDY JOB SEQUENCING =====")

# Take number of jobs from user
n = int(input("Enter number of jobs: "))

jobs = []

# Take job details from keyboard
print("\nEnter job details:")

for i in range(n):

    print(f"\nJob {i + 1}")

    job_id = input("Enter Job ID: ")
    deadline = int(input("Enter Deadline: "))
    profit = int(input("Enter Profit: "))

    jobs.append(Job(job_id, deadline, profit))


# Apply Job Sequencing
schedule, selected_jobs, total_profit = job_sequencing(jobs)


# Display sorted jobs
print("\nJobs sorted by decreasing profit:")

for job in jobs:
    print(
        f"{job.job_id}  "
        f"Deadline: {job.deadline}  "
        f"Profit: {job.profit}"
    )


# Display optimal schedule
print("\nOptimal Job Schedule:")

for slot in range(1, len(schedule)):

    if schedule[slot] is not None:

        print(
            f"Slot {slot} -> "
            f"{schedule[slot].job_id} "
            f"(Profit = {schedule[slot].profit})"
        )


# Display final result
print("\nNumber of Jobs Selected:", len(selected_jobs))
print("Maximum Total Profit:", total_profit)