
from datetime import datetime, timedelta
import json

# Define room rules as a dictionary
ROOM_RULES = {
    "ServerRoom": {"min_access_level": 2, "open_time": "09:00", "close_time": "11:00", "cooldown": 15},
    "Vault": {"min_access_level": 3, "open_time": "09:00", "close_time": "10:00", "cooldown": 30},
    "R&D Lab": {"min_access_level": 1, "open_time": "08:00", "close_time": "12:00", "cooldown": 10}

}


# Firstly add the Given Employee Data 
employee_data = [
    {"id": "EMP001", "access_level": 2, "request_time": "09:15", "room": "ServerRoom"},
    {"id": "EMP002", "access_level": 1, "request_time": "09:30", "room": "Vault"},
    {"id": "EMP003", "access_level": 3, "request_time": "10:05", "room": "ServerRoom"},
    {"id": "EMP004", "access_level": 3, "request_time": "09:45", "room": "Vault"},
    {"id": "EMP005", "access_level": 2, "request_time": "08:50", "room": "R&D Lab"},
    {"id": "EMP006", "access_level": 1, "request_time": "10:10", "room": "R&D Lab"},
    {"id": "EMP007", "access_level": 2, "request_time": "10:18", "room": "ServerRoom"},
    {"id": "EMP008", "access_level": 3, "request_time": "09:55", "room": "Vault"},
    {"id": "EMP001", "access_level": 2, "request_time": "09:28", "room": "ServerRoom"},
    {"id": "EMP006", "access_level": 1, "request_time": "10:15", "room": "R&D Lab"}
]

def parse_time(time_str):
    # Add Helper function to convert 'HH:MM' string to a datetime.time object
    return datetime.strptime(time_str, '%H:%M').time()

def is_time_between(check_time, start_time, end_time):
    #Adding Check if a time is between two other times.
    return start_time <= check_time <= end_time


# 5th Commit Create Main Function
def run_simulation():
    """The main function to run the simulation logic."""
    # We need to keep a history of granted access to check cooldowns.
    # Format: (employee_id, room_name, access_time)
    access_history = []
    results = []

    # Sort requests by time to handle cooldown checks chronologically
    employee_data_sorted = sorted(employee_data, key=lambda x: x['request_time'])

    for employee in employee_data_sorted:
        emp_id = employee['id']
        emp_access_level = employee['access_level']
        emp_request_time_str = employee['request_time']
        room_name = employee['room']

        # Convert string time to a time object for comparison
        emp_request_time = parse_time(emp_request_time_str)

        # Get the rules for the requested room
        room_rules = ROOM_RULES.get(room_name)
        if not room_rules:
            results.append({
                "id": emp_id,
                "status": "Denied",
                "reason": f"Room '{room_name}' does not exist."
            })
            continue

        # Commit 6th Check 1 Access Level
        if emp_access_level < room_rules['min_access_level']:
            results.append({
                "id": emp_id,
                "status": "Denied",
                "reason": f"Access level too low. Required: {room_rules['min_access_level']}, Had: {emp_access_level}"
            })
            continue

                # Commit 7th Check 2 Time Window
        room_open_time = parse_time(room_rules['open_time'])
        room_close_time = parse_time(room_rules['close_time'])
        if not is_time_between(emp_request_time, room_open_time, room_close_time):
            results.append({
                "id": emp_id,
                "status": "Denied",
                "reason": f"Room is closed. Open hours: {room_rules['open_time']} to {room_rules['close_time']}"
            })
            continue


        # Commit 8th we add Check 3: Cooldown Period
        # Convert request time to a full datetime for cooldown calculation (we use an arbitrary date, only time matters for difference)
        arbitrary_date = datetime(2024, 1, 1)  # Use any date
        emp_request_datetime = datetime.combine(arbitrary_date, emp_request_time)
        cooldown_period = timedelta(minutes=room_rules['cooldown'])

        # Check if this employee accessed this room within the cooldown period
        grant_access = True
        reason = ""
        for history in access_history:
            hist_emp_id, hist_room, hist_access_datetime = history
            if hist_emp_id == emp_id and hist_room == room_name:
                time_difference = emp_request_datetime - hist_access_datetime
                if time_difference < cooldown_period:
                    grant_access = False
                    cooldown_end_time = (hist_access_datetime + cooldown_period).time().strftime('%H:%M')
                    reason = f"Access denied. Cooldown active until {cooldown_end_time}. Last access at {hist_access_datetime.time().strftime('%H:%M')}"
                    break

        if not grant_access:
            results.append({"id": emp_id, "status": "Denied", "reason": reason})
            continue

        # If all checks passed, grant access
        results.append({
            "id": emp_id,
            "status": "Granted",
            "reason": f"Access granted to {room_name}"
        })
        # Record this successful access in history for future cooldown checks
        access_history.append((emp_id, room_name, emp_request_datetime))

    return results

# Run the simulation and print results
print("Running Employee Access Simulation\n")

simulation_results = run_simulation()

# Print the results in a readable format
print(f"{'ID':<8} | {'Status':<8} | Reason")
print("-" * 60)
for result in simulation_results:
    print("{result['id']:<8} | {result['status']:<8} | {result['reason']}")

print("\n Simulation complete.")

