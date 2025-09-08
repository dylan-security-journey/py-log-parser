# Project Setup Guide: py-log-parser

This guide explains how I built this project from scratch to a full setup.

---

## 1. Create the Project Folder
```bash
mkdir py-log-parser
cd py-log-parser
```

---

## 2. Initialize Git and Connect to GitHub
```bash
git init
git branch -M main
git remote add origin https://github.com/<your-username>/py-log-parser.git
```

---

## 3. Create a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

This keeps dependencies isolated to this project.

---

## 4. Install Dependencies
Install **matplotlib** for visualization:
```bash
pip install matplotlib
```

Export dependencies so others can recreate them:
```bash
pip freeze > requirements.txt
```

---

## 5. Build the Parser Step by Step
- Started with reading a log file line by line.
- Stripped whitespace and split each line into: date, time, level, message.
- Counted log levels (`INFO`, `WARN`, `ERROR`) using a dictionary.
- Printed a structured summary.
- Added CSV export with Python’s built-in `csv` module.
- Added JSON export with Python’s built-in `json` module.
- Wrapped the logic in a function `parse_log()`.
- Added **argparse** so the script can be run like:
  ```bash
  python parser.py --file sample.log --level ERROR
  ```
- Added **matplotlib** bar chart export to `summary.png`.

---

## 6. Add Documentation Files
- `.gitignore` → to keep repo clean (`.venv/`, `__pycache__/` etc.).
- `README.md` → main description, usage examples, chart preview.
- `SETUP.md` → this file, explaining how it was built step by step.

---

## 7. Push to GitHub
```bash
git add .
git commit -m "initial version of py-log-parser with argparse, exports, and visualization"
git push -u origin main
```

---

## 8. Run the Project
Example with no filter:
```bash
python parser.py --file sample.log
```

Example with a filter:
```bash
python parser.py --file sample.log --level ERROR
```

---

✅ That’s the complete setup — from empty folder to a fully working Python CLI tool with visualization.
