import argparse
import json
import math

def calculate(length_mm, width_mm, thickness_mm=0.035, current=2.0, limit=0.1):
    values = (length_mm, width_mm, thickness_mm, current, limit)
    if not all(math.isfinite(v) for v in values):
        raise ValueError('All values must be finite')
    if length_mm < 0 or width_mm <= 0 or thickness_mm <= 0 or current < 0 or limit < 0:
        raise ValueError('Width and thickness must be positive; other values cannot be negative')
    resistance = 1.68e-8 * (length_mm / 1000) / ((width_mm / 1000) * (thickness_mm / 1000))
    drop = current * resistance
    return dict(resistance_ohms=resistance, voltage_drop_volts=drop,
                power_watts=current**2 * resistance, within_limit=drop <= limit)

def main():
    parser = argparse.ArgumentParser(description='Copper trace voltage drop calculator')
    parser.add_argument('length', type=float, help='Length in millimeters')
    parser.add_argument('width', type=float, help='Width in millimeters')
    parser.add_argument('--thickness', type=float, default=0.035)
    parser.add_argument('--current', type=float, default=2.0)
    parser.add_argument('--limit', type=float, default=0.1)
    args = parser.parse_args()
    try:
        result = calculate(args.length, args.width, args.thickness, args.current, args.limit)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))
    if not result['within_limit']:
        print('HOLD: voltage drop exceeds the design limit')
        return 1
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
