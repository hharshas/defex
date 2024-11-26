import json
from dataclasses import dataclass

@dataclass
class PkgPosition:
    uld_id: int
    x_min: int
    y_min: int
    z_min: int
    x_max: int
    y_max: int
    z_max: int
    weight: int  # Added weight to track package weight
    ispriority: bool  # Priority flag

def read_output_file(output_file):
    """Reads the output file and parses the package positions."""
    pkg_positions = []

    with open(output_file, 'r') as f:
        for line_number, line in enumerate(f, start=1):
            values = line.strip().split(',')

            # Ensure the line has exactly 8 values
            if len(values) != 8:
                print(f"Skipping invalid line {line_number}: {line.strip()}")
                continue

            try:
                weight = int(values[0])  # First value is the weight

                if values[1] == 'NONE':  # Package not placed
                    pkg_positions.append(PkgPosition(
                        uld_id=None,
                        x_min=None,
                        y_min=None,
                        z_min=None,
                        x_max=None,
                        y_max=None,
                        z_max=None,
                        weight=weight,
                        ispriority=False  # Assume default
                    ))
                else:
                    # Package is placed
                    pkg_positions.append(PkgPosition(
                        uld_id=int(values[1]),
                        x_min=int(values[2]),
                        y_min=int(values[3]),
                        z_min=int(values[4]),
                        x_max=int(values[5]),
                        y_max=int(values[6]),
                        z_max=int(values[7]),
                        weight=weight,
                        ispriority=False  # Assume default
                    ))
            except ValueError as e:
                print(f"Error parsing line {line_number}: {line.strip()} ({e})")
                continue

    return pkg_positions

def convert_to_json(output_file):
    """Converts the output file data to JSON format."""
    pkg_positions = read_output_file(output_file)

    # Generate JSON structure
    data = {
        "pkg_positions": [
            {
                "weight": pkg.weight,
                "uld_id": pkg.uld_id,
                "x_min": pkg.x_min,
                "y_min": pkg.y_min,
                "z_min": pkg.z_min,
                "x_max": pkg.x_max,
                "y_max": pkg.y_max,
                "z_max": pkg.z_max,
                "ispriority": pkg.ispriority
            }
            for pkg in pkg_positions
        ]
    }

    # Write JSON to file
    with open("output_data.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Run conversion
if __name__ == '__main__':
    output_file = "output.txt"  # Replace with your file path
    convert_to_json(output_file)
