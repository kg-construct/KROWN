import json
import os
import argparse
import random
import string
from concurrent.futures import ProcessPoolExecutor

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_single_object(index, list_length, duplication_rate):
    new_id = generate_random_string(length=12)

    n_duplicates = int(list_length * duplication_rate)
    n_unique = list_length - n_duplicates

    unique_values = []

    if n_unique > 0:
        for i in range(n_unique):
            if (i + 1) % 10000 == 0:
                print(f"🧪 Generating unique values: {i + 1}/{n_unique}")
            unique_values.append(generate_random_string(length=10))
    else:
        # Duplication rate is 100%, we need at least one value to duplicate
        seed_value = generate_random_string(length=10)
        unique_values.append(seed_value)

    duplicates = []
    for i in range(n_duplicates):
        if (i + 1) % 10000 == 0:
            print(f"🔁 Generating duplicates: {i + 1}/{n_duplicates}")
        duplicates.append(random.choice(unique_values))

    all_values = unique_values + duplicates
    random.shuffle(all_values)

    return {
        "id": new_id,
        "values": all_values
    }

def unpack_and_generate(params):
    return generate_single_object(*params)

def generate_structured_data(template, count, list_length=3, duplication_rate=0.0):
    result = []

    if count == 1:
        print("⚙️ Generating a single object without parallelism...")
        result.append(generate_single_object(0, list_length, duplication_rate))
        return result

    print(f"⚙️ Generating {count} objects using parallel processing...")
    with ProcessPoolExecutor() as executor:
        args = ((i, list_length, duplication_rate) for i in range(count))

        for i, obj in enumerate(executor.map(unpack_and_generate, args), 1):
            result.append(obj)
            if i % 10000 == 0:
                print(f"🔄 Generated {i}/{count} objects...")

    return result

def main(input_path, output_path, count, list_length, duplication_rate):
    if not os.path.exists(input_path):
        print(f"❌ Error: File '{input_path}' not found.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        template = json.load(f)

    generated_data = generate_structured_data(
        template, count, list_length, duplication_rate=duplication_rate
    )

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(generated_data, f, indent=2)

    dup_percent = int(duplication_rate * 100)
    obj_word = "object" if count == 1 else "objects"
    print(f"✅ Generated {count} {obj_word} with {dup_percent}% duplicates in 'values' and saved to '{output_path}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate random JSON data with optional duplication and parallel processing.")
    parser.add_argument("input_path", help="Path to input JSON template file")
    parser.add_argument("output_path", help="Path to save the generated JSON file")
    parser.add_argument("--count", type=int, default=5, help="Number of objects to generate")
    parser.add_argument("--list_length", type=int, default=3, help="Number of values in each 'values' list")
    parser.add_argument("--duplication_rate", type=float, default=0.0, help="Proportion of duplicates in each 'values' list (0.0 - 1.0)")

    args = parser.parse_args()
    main(args.input_path, args.output_path, args.count, args.list_length, args.duplication_rate)