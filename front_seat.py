from datetime import datetime, timedelta 
import random

# Initial data setup
children = ["Joshua", "Skylar", "Saige", "Lauryn"]
start_date = datetime.now()
cycle_duration_days = 30
change_combinations_every = 5

# Function to get the current date and child pairs
def get_child_pairs(start_date, days_to_cycle=30, change_combinations_every=5):
    index = 0
    current_date = start_date
    end_date = start_date + timedelta(days=days_to_cycle)
    pairs = []

    while current_date < end_date:
        child_1 = children[index % len(children)]
        child_2 = children[(index + 1) % len(children)]
        pairs.append((current_date.strftime('%Y-%m-%d'), child_1, child_2))

        index = (index + 2) % len(children)
        current_date += timedelta(days=1)

        if (current_date - start_date).days % change_combinations_every == 0:
            random.shuffle(children)

    return pairs

def generate_html_file(pairs, filename='front_seat.html'):
    with open(filename, 'w') as file:
        file.write('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Child Pairing Schedule</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Child Pairing Schedule</h1>
    <table>
        <thead>
            <tr>
                <th>Date</th>
                <th>Child 1</th>
                <th>Child 2</th>
            </tr>
        </thead>
        <tbody>
''')
        for date, child_1, child_2 in pairs:
            file.write(f'''
            <tr>
                <td>{date}</td>
                <td>{child_1}</td>
                <td>{child_2}</td>
            </tr>
            ''')
        file.write('''
        </tbody>
    </table>
</body>
</html>
''')

# Generate the child pairs and create an HTML file
child_pairs = get_child_pairs(start_date, cycle_duration_days, change_combinations_every)
generate_html_file(child_pairs)

print("HTML file 'front_seat.html' has been generated.")



