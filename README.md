# PCB trace calculator

A PCB trace is a thin copper path that carries current on a circuit board. This calculator estimates its resistance, how much voltage is lost along it, and how much electrical power becomes heat.

## How it works

Enter the trace length and width in millimeters. The program also uses the copper thickness, which defaults to 0.035 mm. That is a common thickness for 1 oz copper.

Resistance depends on the trace's length and cross-sectional area. A longer trace has more resistance. A wider or thicker trace has less resistance. The calculation uses copper resistivity of 1.68e-8 ohm-meters.

The program multiplies resistance by current to find the voltage drop. It uses current squared times resistance to find power loss. The default current is 2 amps, and the default voltage-drop limit is 0.1 volts.

For example, a trace that is 100 mm long and 1 mm wide has a resistance of 0.048 ohms with the default thickness. At 2 amps, its voltage drop is 0.096 volts.

## Reading the result

The output is JSON, a text format that other programs can also read. If the drop is above the limit, the program prints a HOLD message and exits with status 1. Invalid inputs give status 2. A result within the limit gives status 0.

This is a voltage-drop estimate. It does not calculate the trace's temperature or decide how much current the board can safely carry. It also does not connect to a CAD program.

## Try it

Use Python 3.11 or newer. Open a terminal in this project's folder and create a virtual environment. This keeps its packages separate from your other Python projects.

```sh
python -m venv .venv
```

On Windows, activate it with this command.

```sh
.venv\Scripts\activate
```

On macOS or Linux, use this command instead.

```sh
source .venv/bin/activate
```

Then install the packages the project needs.

```sh
python -m pip install -r requirements.txt
```

```sh
python trace.py 100 1
python trace.py 50 2 --current 3 --limit 0.1
```

The first two inputs are length and width. Use `--thickness` to change copper thickness, `--current` to change current, or `--limit` to change the allowed voltage drop.

## Tests

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

The tests check unit conversions, voltage drop, power loss, the voltage limit, and invalid dimensions.
