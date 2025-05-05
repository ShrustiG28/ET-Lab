import pandas as pd

# === STEP 1: READ THE CSV (skip the "MVJ College..." line) ===
df = pd.read_csv("etlab_attendance.csv", skiprows=1)

# === STEP 2: Clean headers ===
df.columns = df.columns.str.strip()  # Remove spaces from headers

# === STEP 3: Get the first row (your data) ===
student_row = df.iloc[0]  # The first row of data (index 0)

# === STEP 4: Select subject columns (excluding first 3 and last 2) ===
subject_columns = df.columns[3:-2]

# === STEP 5: Parse attendance ===
attendance_data = []

for subject in subject_columns:
    raw = student_row[subject]
    if '/' in raw:
        attended, total = raw.split('(')[0].split('/')
        percent = raw.split('(')[1].replace('%)', '')
        attendance_data.append({
            'subject_code': subject,
            'attended': int(attended.strip()),
            'total': int(total.strip()),
            'percentage': float(percent.strip())
        })

# === STEP 6: Print the result ===
print("Extracted Attendance Data:\n")
for subject in attendance_data:
    print(subject)
