import json
import os
import argparse
import random
import string
from concurrent.futures import ProcessPoolExecutor, as_completed

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# Helper function for parallel object generation
def generate_single_object(index, list_length):
    def generate_random_string(length=8):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    new_id = generate_random_string(length=12)
    values = set()
    result_values = []

    for _ in range(list_length):
        attempts = 0
        while True:
            val = generate_random_string(length=10)
            if val not in values:
                values.add(val)
                result_values.append(val)
                break
            attempts += 1
            if attempts > 1000:
                raise RuntimeError("Exceeded attempts to generate unique 'values'")

    return {
        "id": new_id,
        "values": result_values
    }

def generate_structured_data(template, count, list_length=3):
    result = []
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(generate_single_object, i, list_length) for i in range(count)]
        for i, future in enumerate(as_completed(futures), 1):
            result.append(future.result())
            if i % 10000 == 0 or i == count:
                print(f"🔄 Generated {i}/{count} objects...")
    return result

def grow_values(data, add_v1=1, add_v2=1, global_unique=True):
    used_v1 = set()
    used_v2 = set()

    if global_unique:
        for obj in data:
            used_v1.update(obj.get("v1", []))
            used_v2.update(obj.get("v2", []))

    for obj in data:
        v1 = obj.get("v1", [])
        v2 = obj.get("v2", [])

        for _ in range(add_v1):
            attempts = 0
            while True:
                new_v1 = generate_random_string(length=10)
                if not global_unique or new_v1 not in used_v1:
                    break
                attempts += 1
                if attempts > 1000:
                    raise RuntimeError("Exceeded attempts to generate unique 'v1' values")
            used_v1.add(new_v1)
            v1.append(new_v1)

        for _ in range(add_v2):
            attempts = 0
            while True:
                new_v2 = generate_random_string(length=8)
                if not global_unique or new_v2 not in used_v2:
                    break
                attempts += 1
                if attempts > 1000:
                    raise RuntimeError("Exceeded attempts to generate unique 'v2' values")
            used_v2.add(new_v2)
            v2.append(new_v2)

        obj["v1"] = v1
        obj["v2"] = v2

    return data

def main(input_path, output_path, count, list_length):
    if not os.path.exists(input_path):
        print(f"❌ Error: File '{input_path}' not found.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        template = json.load(f)

    generated_data = generate_structured_data(template, count, list_length)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(generated_data, f, indent=2)

    print(f"✅ Generated {count} objects and saved to '{output_path}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate and scale random JSON data.")
    parser.add_argument("input_path", help="Path to input JSON template file")
    parser.add_argument("output_path", help="Path to save the generated JSON file")
    parser.add_argument("--count", type=int, default=5, help="Number of objects to generate")
    parser.add_argument("--list_length", type=int, default=3, help="Number of values in each 'values' list")

    args = parser.parse_args()
    main(args.input_path, args.output_path, args.count, args.list_length)