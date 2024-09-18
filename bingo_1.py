from datetime import datetime, timedelta
import random

# Initial data setup
children = ["Joshua", "Skylar", "Saige", "Lauryn"]
cycle_duration_days = 30
shuffle_interval_days = 2

def get_child_pairs_and_singles(start_date, days_to_cycle=30, shuffle_interval_days=2):
    index = 0
    current_date = start_date
    end_date = start_date + timedelta(days=days_to_cycle)
    pairs = []
    singles = []

    while current_date < end_date:
        # Select a pair of children
        child_1 = children[index % len(children)]
        child_2 = children[(index + 1) % len(children)]
        pairs.append((current_date.strftime('%Y-%m-%d'), child_1, child_2))
        
        # Select a single child
        single_child = random.choice(children)
        singles.append((current_date.strftime('%Y-%m-%d'), single_child))

        # Print the current date, selected children, and single child
        print(f"{current_date.strftime('%Y-%m-%d')} - Selected pair: {child_1}, {child_2}")
        print(f"{current_date.strftime('%Y-%m-%d')} - Single child: {single_child}")

        index = (index + 2) % len(children)
        current_date += timedelta(days=1)

        # Shuffle the list of children every 'shuffle_interval_days' days
        if (current_date - start_date).days % shuffle_interval_days == 0:
            random.shuffle(children)
            print("Combinations shuffled!")

    return pairs, singles

def generate_html_file(pairs, singles, filename='front_seat.html'):
    with open(filename, 'w') as file:
        file.write('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Child Pairing Schedule</title>
    <link rel="stylesheet" href="front_seat.css">
</head>
<body>
    <h1>Child Pairing Schedule</h1>
    
    <h2>Child Pairs</h2>
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
    
    <h2>Single Child Selection</h2>
    <table>
        <thead>
            <tr>
                <th>Date</th>
                <th>Child</th>
            </tr>
        </thead>
        <tbody>
''')
        for date, single_child in singles:
            file.write(f'''
            <tr>
                <td>{date}</td>
                <td>{single_child}</td>
            </tr>
            ''')
        file.write('''
        </tbody>
    </table>
</body>
</html>
''')

def main():
    # Start from the current date
    start_date = datetime.now()

    while True:
        # Generate child pairs and single child selections for the specified cycle duration
        pairs, singles = get_child_pairs_and_singles(start_date, cycle_duration_days, shuffle_interval_days)
        generate_html_file(pairs, singles)
        print("HTML file 'front_seat.html' has been generated.")

        # Ask user if they want to continue
        user_input = input("Do you want to continue cycling through the schedule? (yes/no): ").strip().lower()
        if user_input != 'yes':
            break

        # Increment the start date by the cycle duration to continue from the next period
        start_date += timedelta(days=cycle_duration_days)

if __name__ == '__main__':
    main()
