# PCB trace calculator

This estimates the resistance, voltage drop, and power loss of a copper PCB trace. It is useful for checking a trace while changing its length or width.

## Run it

Use Python 3.11 or newer. Run these commands from this repository's folder.

```sh
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
# source .venv/bin/activate
python -m pip install -r requirements.txt
```

```sh
python trace.py 100 1
python trace.py 50 2 --current 3 --limit 0.1
```

## How it works and current limits

Uses copper resistivity 1.68e-8 ohm-m and defaults to 0.035 mm copper thickness. Exit status 1 means the voltage-drop limit was exceeded; 2 means invalid input. This does not calculate temperature rise or certify current capacity. It is a command-line calculation, not a live CAD integration.

## Tests

```sh
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

Tests check unit conversions, power loss, voltage limits, and invalid dimensions.
