import csv
import json
import argparse
import matplotlib.pyplot as plt

# first step: just open the log file and print its contents

# step 2: split each line into its parts (date, time, level, message)

# step 3: filter for ERROR logs and count them

# step 4: count all log levels

def parse_log(filename, level_filter=None):
    """Parse a log file and return counts of log levels."""


    level_counts = {"INFO": 0, "WARN": 0, "ERROR": 0}

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            parts = line.split(" ", 3) # split into 4 chunks max
        
            #guard against malformed lines
            if len(parts) < 4:
                continue

            date, time, level, message = parts # correct ordering

            # If it's a known level, count it
            if level in level_counts:
                level_counts[level] += 1

            # only print lines if no filter, or if it matches the filter
            if level_filter is None or level == level_filter:
                print(f"DATE: {date}, TIME: {time}, LEVEL: {level}, MESSAGE: {message}")


    # Summary
    print(f"\nLog Summary:")
    for lvl, count in level_counts.items():
        print(f"{lvl}: {count}")


    # export summary to a CSV file
    with open("summary.csv", "w", newline="") as csvfile:
        writer =  csv.writer(csvfile)
        writer.writerow(["Level", "Count"]) # Header row
        for lvl, count in level_counts.items():
            writer.writerow([lvl, count])

    # also write the summary to JSON
    with open("summary.json", "w") as jf:
        json.dump(level_counts, jf, indent=2)

    # visualize counts as a bar chart
    plt.bar(level_counts.keys(), level_counts.values())
    plt.title("Log level Counts")
    plt.xlabel("Log Level")
    plt.ylabel("Count")
    plt.tight_layout()    # nice spacing
    plt.savefig("summary.png") # write image file to project folder
    plt.close()
    print("\nVisualization saved as summary.png")

    print("\nSummary also wrriten to summary.csv and summary.json")

    return level_counts

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Simple log parsesr")
    parser.add_argument("--file", required = True, help = "Path to the log file")
    parser.add_argument("--level", choices = ["INFO", "WARN", "ERROR"], help = "Filter by log level")
    args = parser.parse_args()

    # call your function with args
    parse_log(args.file, level_filter = args.level)





