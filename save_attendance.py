import json

# Sample attendance data (replace this with your real parsed data)
attendance_data = [
    {'subject_code': 'MVJ22A4092', 'attended': 16, 'total': 16, 'percentage': 100.0},
    {'subject_code': 'MVJ22CS41', 'attended': 27, 'total': 30, 'percentage': 90.0},
    {'subject_code': 'MVJ22CS42', 'attended': 42, 'total': 50, 'percentage': 84.0},
    {'subject_code': 'MVJ22CS43', 'attended': 41, 'total': 47, 'percentage': 87.0},
    {'subject_code': 'MVJ22CSL44', 'attended': 14, 'total': 16, 'percentage': 88.0},
    {'subject_code': 'MVJ22BI47', 'attended': 10, 'total': 15, 'percentage': 67.0},
    {'subject_code': 'MVJ22UHV48', 'attended': 7, 'total': 8, 'percentage': 88.0},
    {'subject_code': 'MVJ22CS452', 'attended': 25, 'total': 29, 'percentage': 86.0}
]

# Save to a JSON file
with open("attendance_data.json", "w") as f:
    json.dump(attendance_data, f, indent=4)

print("✅ Attendance data saved to attendance_data.json")
