# py-log-parser

A tiny **Python CLI log parser** that:
- Reads a log file
- Parses each line into: date, time, level, message
- Supports `--level` filter via **argparse** (INFO/WARN/ERROR)
- Summarizes counts per level
- Exports results to **CSV** and **JSON**
- Generates a **matplotlib** bar chart (`summary.png`)
- Uses a **virtual environment (venv)** to isolate dependencies

## Quickstart
```bash
# clone
git clone https://github.com/<your-username>/py-log-parser.git
cd py-log-parser

# set up venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# run (no filter)
python parser.py --file sample.log

# run with filter
python parser.py --file sample.log --level ERROR


