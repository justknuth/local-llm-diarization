import argparse

# This is a manually run script from the outbound folder

def replace_speakers(input_path, output_path, replacements):
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        for old, new in replacements.items():
            line = line.replace(old, new)
        new_lines.append(line)

    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"Updated file saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Replace speaker labels with actual names")
    parser.add_argument("--input", required=True, help="inputtedfilename.json") # < name of the file in this folder you want to add names to
    parser.add_argument("--output", required=True, help="outputtedfilename.json") # < this is the output filename. Cant be the same as above
    args = parser.parse_args()

    # Define the replacements
    replacements = {
        "SPEAKER_01": "John",
        "SPEAKER_00": "Jane"
    }

    replace_speakers(args.input, args.output, replacements)

    # run this script from the outbound folder. You must use a valid filename and then desired filename
    # python replace_with_real_names.py --input inputfilename.json --output outputfilename.txt