import csv
import argparse
import os
import random
import string

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def read_input_csv(input_path):
    with open(input_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

def scale_data(data, count, duplication_rate):
    sports_pool = [row['Sport'] for row in data]
    result = []
    id_base = max(int(row['ID']) for row in data) + 1

    n_duplicates = int(count * duplication_rate)
    n_new = count - n_duplicates

    # Generate duplicate rows (repeating sports)
    for i in range(n_duplicates):
        base_row = random.choice(data)
        result.append({
            'ID': str(id_base + i),
            'Name': generate_random_string(10),
            'Sport': base_row['Sport']
        })

    # Generate new sports if needed
    for i in range(n_new):
        new_sport = generate_random_string(6)
        result.append({
            'ID': str(id_base + n_duplicates + i),
            'Name': generate_random_string(10),
            'Sport': new_sport
        })

    return result

def write_output_csv(output_path, data):
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['ID', 'Name', 'Sport'])
        writer.writeheader()
        writer.writerows(data)

def main(input_path, output_path, count, duplication_rate):
    if not os.path.exists(input_path):
        print(f"❌ Input file not found: {input_path}")
        return

    data = read_input_csv(input_path)
    scaled = scale_data(data, count, duplication_rate)
    write_output_csv(output_path, scaled)

    print(f"✅ Generated {count} rows with {int(duplication_rate * 100)}% duplicated sports → {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scale a CSV dataset with Sport duplication.")
    parser.add_argument("input_path", help="Path to input CSV")
    parser.add_argument("output_path", help="Path to save output CSV")
    parser.add_argument("--count", type=int, required=True, help="Total number of rows to generate")
    parser.add_argument("--duplication_rate", type=float, default=0.5, help="Rate of repeated 'Sport' values (0.0–1.0)")

    args = parser.parse_args()
    main(args.input_path, args.output_path, args.count, args.duplication_rate)