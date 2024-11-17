import argparse
import json
from dataclasses import dataclass

@dataclass
class ULD:
    length: int
    width: int
    height: int
    weight_limit: int

@dataclass
class Package:
    length: int
    width: int
    height: int
    weight: int
    priority: str
    cost: int

@dataclass
class PkgPosition:
    uld_id: int
    x_min: int
    y_min: int
    z_min: int
    x_max: int
    y_max: int
    z_max: int

def read_input(input_file):
    ulds = []
    packages = []
    
    with open(input_file, 'r') as f:
        n, m, k = map(int, f.readline().split())
        

        for _ in range(n):
            length, width, height, weight_limit = map(int, f.readline().split()[1:])
            ulds.append(ULD(length, width, height, weight_limit))
        
        for _ in range(m):
            vals = f.readline().split()
            length, width, height, weight = map(int, vals[1:5])
            priority = vals[5]
            cost = int(vals[6])
            packages.append(Package(length, width, height, weight, priority, cost))
    
    return n, m, k, ulds, packages

def read_output(output_file, m):
    pkg_positions = [None] * (m + 1)
    cost = used_pkg = priority_uld_cnt = None
    
    with open(output_file, 'r') as f:
        cost, used_pkg, priority_uld_cnt = map(int, f.readline().split(','))
        

        for i in range(1, m + 1):
            vals = f.readline().split(',')
            pkg_id = int(vals[0].split('-')[-1])
            if vals[1] != 'NONE':
                uld_id = int(vals[1].split('-')[-1])
                x_min, y_min, z_min, x_max, y_max, z_max = map(int, vals[2:])
                pkg_positions[pkg_id] = PkgPosition(uld_id, x_min, y_min, z_min, x_max, y_max, z_max)
    
    return cost, used_pkg, priority_uld_cnt, pkg_positions

def convert_to_json(input_file, output_file):
    n, m, k, ulds, packages = read_input(input_file)
    cost, used_pkg, priority_uld_cnt, pkg_positions = read_output(output_file, m)
    

    data = {
        "uld_count": n,
        "package_count": m,
        "k": k,
        "ulds": [{"length": uld.length, "width": uld.width, "height": uld.height, "weight_limit": uld.weight_limit} for uld in ulds],
        "packages": [{"length": pkg.length, "width": pkg.width, "height": pkg.height, "weight": pkg.weight, "priority": pkg.priority, "cost": pkg.cost} for pkg in packages],
        "pkg_positions": [
            {
                "pkg_id": i,
                "uld_id": pkg_positions[i].uld_id if pkg_positions[i] else None,
                "x_min": pkg_positions[i].x_min if pkg_positions[i] else None,
                "y_min": pkg_positions[i].y_min if pkg_positions[i] else None,
                "z_min": pkg_positions[i].z_min if pkg_positions[i] else None,
                "x_max": pkg_positions[i].x_max if pkg_positions[i] else None,
                "y_max": pkg_positions[i].y_max if pkg_positions[i] else None,
                "z_max": pkg_positions[i].z_max if pkg_positions[i] else None
            }
            for i in range(1, m + 1)
        ],
        "cost": cost,
        "used_pkg": used_pkg,
        "priority_uld_count": priority_uld_cnt
    }


    with open("output_data.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--output", required=True, help="Output file path")
    args = parser.parse_args()
    
    convert_to_json(args.input, args.output)
