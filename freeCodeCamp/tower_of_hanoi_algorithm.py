def hanoi_solver(disks_input):
    # A contains all disks in descending order; B and C are empty
    rods = [list(range(disks_input, 0, -1)), [], []]
    states = []

    def record_state():
        # Format
        states.append(f"{rods[0]} {rods[1]} {rods[2]}")

    def move(n, source, target, auxiliary):
        if n > 0:
            move(n - 1, source, auxiliary, target)

            disk = rods[source].pop()
            rods[target].append(disk)
            record_state()

            move(n - 1, auxiliary, target, source)

    # First state
    record_state()

    # Recursive: move all disks from rod 0 to rod 2 using rod 1 as auxiliary
    move(disks_input, 0, 2, 1)

    return "\n".join(states)
