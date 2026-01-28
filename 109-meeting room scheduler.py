#meeting room scheduler problem
def can_schedule_meetings(intervals):
    if not intervals:
        return True

    # Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True

# Example usage
meetings = [[0, 30], [5, 10], [15, 20]]
can_schedule = can_schedule_meetings(meetings)
print("Can schedule all meetings:", can_schedule)  # Output: Can schedule all meetings: False