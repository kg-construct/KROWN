import json
import os
import argparse
import random
import string

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def grow_values(data, add_values=1, global_unique=True):
    used = set()

    if global_unique:
        for obj in data:
            used.update(obj.get("v1", []))

    for i, obj in enumerate(data):
        if (i + 1) % 10000 == 0:
            print(f"🔄 Processed {i + 1}/{len(data)} objects...")

        v = obj.get("v1", [])

        for _ in range(add_values):
            attempts = 0
            while True:
                new_value = generate_random_string(length=10)
                if not global_unique or new_value not in used:
                    break
                attempts += 1
                if attempts > 1000:
                    raise RuntimeError("Exceeded attempts to generate unique values")
            used.add(new_value)
            v.append(new_value)

        obj["v1"] = v
        obj["v2"] = list(v)  # v2 is the same as v1

    return data

def main(input_path, output_path, add_values, unique):
    if not os.path.exists(input_path):
        print(f"❌ Error: File '{input_path}' not found.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated_data = grow_values(data, add_values=add_values, global_unique=unique)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(updated_data, f, indent=2)

    print(f"✅ Expanded 'v1' and 'v2' in {len(data)} objects and saved to '{output_path}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Expand 'v1' and 'v2' lists in a JSON structure.")
    parser.add_argument("input_path", help="Path to the input JSON file")
    parser.add_argument("output_path", help="Path to write the modified JSON file")
    parser.add_argument("--add_values", type=int, default=2, help="Number of new elements to add to 'v1' and 'v2'")
    parser.add_argument("--unique", action="store_true", help="Ensure global uniqueness of added values")

    args = parser.parse_args()
    main(args.input_path, args.output_path, args.add_values, args.unique)