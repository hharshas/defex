#!/usr/bin/env python
import json
import argparse
from random import randint

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--config")
  parser.add_argument("--output")
  args = parser.parse_args()
  
  config = None
  with open(args.config) as f:
    config = json.load(f)

  with open(args.output, '+w') as f:
    f.write(f'{config['n']} {config['m']} {config['k']}\n')
    uld = config['ULD']
    for i in range(config['n']):
      length = randint(uld['length_min'], uld['length_max'])
      width = randint(uld['width_min'], uld['width_max'])
      height = randint(uld['height_min'], uld['height_max'])
      weight_limit = randint(uld['weight_limit_min'], uld['weight_limit_max'])
      f.write(f'ULD-{i + 1} {length} {width} {height} {weight_limit}\n')

    pkg = config['Package']
    for i in range(config['m']):
      length = randint(pkg['length_min'], pkg['length_max'])
      width = randint(pkg['width_min'], pkg['width_max'])
      height = randint(pkg['height_min'], pkg['height_max'])
      weight = randint(pkg['weight_min'], pkg['weight_max'])
      type = 'P' if randint(1, 100) <= pkg['priority_probability'] else 'E'
      cost = randint(pkg['cost_min'], pkg['cost_max'])
      f.write(f'P-{i + 1} {length} {width} {height} {weight} {type} {cost}\n')

if __name__ == '__main__':
  main()