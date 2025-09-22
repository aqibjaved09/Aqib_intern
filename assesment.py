
from datetime import datetime, timedelta
import json

# Define room rules as a dictionary
ROOM_RULES = {
    "ServerRoom": {"min_access_level": 2, "open_time": "09:00", "close_time": "11:00", "cooldown": 15},
    "Vault": {"min_access_level": 3, "open_time": "09:00", "close_time": "10:00", "cooldown": 30},
    "R&D Lab": {"min_access_level": 1, "open_time": "08:00", "close_time": "12:00", "cooldown": 10}




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
