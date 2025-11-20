# A simple simulation of the Banker's Algorithm for deadlock avoidance

def is_safe_state(processes, available, max_need, allocation):
    """
    Checks if the current system state is safe.
    """
    
    num_processes = len(processes)
    num_resources = len(available)

    # 1. Calculate the 'need' matrix
    # Need = Max - Allocation
    need = [[max_need[i][j] - allocation[i][j] for j in range(num_resources)] for i in range(num_processes)]

    # 2. Initialize our work vector and finish vector
    work = available[:]  # A copy of the available resources
    finish = [False] * num_processes # No process is finished yet

    safe_sequence = [] # This will store the safe sequence if one exists

    print("--- Checking for a Safe State ---")
    print(f"Initial Available Resources (Work): {work}")

    # 3. The main safety check loop
    count = 0
    while count < num_processes:
        found_process = False
        
        for p in range(num_processes):
            # Check if this process (p) is already finished
            if not finish[p]:
                
                # Check if this process's 'need' can be met by the current 'work'
                # i.e., can process 'p' run to completion?
                if all(need[p][j] <= work[j] for j in range(num_resources)):
                    
                    # Yes, it can!
                    print(f"  -> Process P{p} can run. (Need: {need[p]} <= Work: {work})")
                    
                    # Pretend it runs and releases its resources
                    # Work = Work + Allocation
                    for j in range(num_resources):
                        work[j] += allocation[p][j]
                        
                    # Mark this process as finished
                    finish[p] = True
                    found_process = True
                    safe_sequence.append(p)
                    count += 1
                    
                    print(f"     ...Process P{p} finishes, releases resources. New Work: {work}")

        # If we went through all processes and couldn't find one that could run,
        # the system is in an unsafe state.
        if not found_process:
            print("\n--- System is in an UNSAFE STATE! ---")
            print("No process could be found that can run to completion.")
            return False, []

    # If we get here, all processes finished successfully
    print("\n--- System is in a SAFE STATE! ---")
    return True, safe_sequence


# --- Define our system state ---

# 5 processes
processes = [0, 1, 2, 3, 4]

# 3 resource types (e.g., CPU, RAM, Disk)
# Total available resources in the system
available_resources = [10, 5, 7] # 10 of R1, 5 of R2, 7 of R3

# Maximum resources each process *could* request
max_need_matrix = [
    [7, 5, 3],  # P0
    [3, 2, 2],  # P1
    [9, 0, 2],  # P2
    [2, 2, 2],  # P3
    [4, 3, 3]   # P4
]

# Resources currently allocated to each process
allocation_matrix = [
    [0, 1, 0],  # P0
    [2, 0, 0],  # P1
    [3, 0, 2],  # P2
    [2, 1, 1],  # P3
    [0, 0, 2]   # P4
]

# --- Run the simulation ---
if __name__ == "__main__":
    
    # Calculate the currently available resources
    # Available = Total - (Sum of all allocations)
    total_allocated = [0] * len(available_resources)
    for i in range(len(processes)):
        for j in range(len(available_resources)):
            total_allocated[j] += allocation_matrix[i][j]
            
    current_available = [available_resources[j] - total_allocated[j] for j in range(len(available_resources))]

    # Run the safety check
    is_safe, sequence = is_safe_state(processes, current_available, max_need_matrix, allocation_matrix)
    
    if is_safe:
        print(f"A safe sequence was found: {' -> '.join(f'P{p}' for p in sequence)}")