"""
Script to view the contents of context pkl files from idea generation output.

Usage:
    python view_context.py <context_directory>

Example:
    python view_context.py course_project/20251126_162603/idea_generation_output/context
"""

import pickle
import sys
from pathlib import Path
import pprint


def view_pkl_files(context_dir: str | Path) -> None:
    """Load and display all pkl files in the given directory."""

    context_path = Path(context_dir)

    if not context_path.exists():
        print(f"Error: Directory '{context_dir}' does not exist.")
        sys.exit(1)

    pkl_files = sorted(context_path.glob("*.pkl"))

    if not pkl_files:
        print(f"No .pkl files found in '{context_dir}'")
        sys.exit(1)

    print(f"Found {len(pkl_files)} pkl file(s) in {context_dir}\n")

    for pkl_file in pkl_files:
        print(f"\n{'='*60}")
        print(f"File: {pkl_file.name}")
        print('='*60)

        with open(pkl_file, 'rb') as f:
            data = pickle.load(f)

        # Pretty print the contents
        if isinstance(data, dict):
            for key, value in data.items():
                print(f"\n--- {key} ---")
                if isinstance(value, str) and len(value) > 500:
                    print(value[:500] + "...[truncated]")
                else:
                    pprint.pprint(value, width=100)
        else:
            pprint.pprint(data, width=100)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Default to the known context directory
        default_dir = Path(__file__).parent / "course_project/20251126_162603/idea_generation_output/context"
        if default_dir.exists():
            view_pkl_files(default_dir)
        else:
            print("Usage: python view_context.py <context_directory>")
            print("\nExample:")
            print("  python view_context.py course_project/20251126_162603/idea_generation_output/context")
            sys.exit(1)
    else:
        view_pkl_files(sys.argv[1])
