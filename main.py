import sys
import subprocess
import os
"""
Main routine to simplify and centralize the process of running the benchmarking scripts.

Usage:
Since the benchmarking scripts use the signal module and set alarm, on Windows this needs to be run from a WSL terminal, due to compatibility issues with signal handling on native Windows Python environments.
"""
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py [random|ordered|reversed|partial|duplicated]")
        sys.exit(1)

    choice = sys.argv[1]

    # dir where the script is being run
    base_dir = os.getcwd()

    script_map = {
        "random": os.path.join(base_dir, "benchmarking_scripts/benchmarking_randomlists.py"),
        "ordered": os.path.join(base_dir, "benchmarking_scripts/benchmarking_orderedlists.py"),
        "reversed": os.path.join(base_dir, "benchmarking_scripts/benchmarking_reversedlists.py"),
        "partial": os.path.join(base_dir, "benchmarking_scripts/benchmarking_nearlyordered.py"),
        "duplicated": os.path.join(base_dir, "benchmarking_scripts/benchmarking_duplicatedlists.py")
    }

    if choice in script_map:
        subprocess.run(["python3", script_map[choice]])
    else:
        print(f"Invalid choice '{choice}'. Available options are: random, ordered, reversed, partial, duplicated.")
        sys.exit(1)

if __name__ == '__main__':
    main()
