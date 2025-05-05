import json
import math

# Load attendance data
with open("attendance_data.json", "r") as f:
    data = json.load(f)

target_percentage = 85
plan = []

for subject in data:
    subject_code = subject['subject_code']
    attended = subject['attended']
    total = subject['total']
    current_percentage = (attended / total) * 100 if total != 0 else 0

    # If already above target, no need to plan more
    if current_percentage >= target_percentage:
        plan.append({
            "subject_code": subject_code,
            "status": "Safe",
            "current_percentage": round(current_percentage, 2),
            "extra_classes_needed": 0
        })
    else:
        # Calculate minimum future classes needed to hit 85%
        # Solve: (attended + x) / (total + x) >= 0.85
        x = 0
        while ((attended + x) / (total + x)) < 0.85:
            x += 1
        plan.append({
            "subject_code": subject_code,
            "status": "Low",
            "current_percentage": round(current_percentage, 2),
            "extra_classes_needed": x
        })

# Sort plan by lowest current_percentage first
plan.sort(key=lambda x: x['current_percentage'])

# Display the final plan
for item in plan:
    print(f"{item['subject_code']}: {item['status']} | Current: {item['current_percentage']}% | Extra Needed: {item['extra_classes_needed']}")
