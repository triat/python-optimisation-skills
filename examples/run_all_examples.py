#!/usr/bin/env python3
"""
Run all optimization examples and display results.
This demonstrates the practical impact of the optimizations.
"""

import sys
import importlib.util
from pathlib import Path


def run_example(example_file: Path):
    """Run a single example file and capture its output."""
    print(f"\n{'='*70}")
    print(f"Running: {example_file.name}")
    print('='*70)

    # Load the module
    spec = importlib.util.spec_from_file_location("example", example_file)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        sys.modules["example"] = module
        try:
            spec.loader.exec_module(module)
        except Exception as e:
            print(f"❌ Error running {example_file.name}: {e}")
        finally:
            # Clean up
            if "example" in sys.modules:
                del sys.modules["example"]
    else:
        print(f"❌ Could not load {example_file.name}")


def main():
    """Run all example files in order."""
    examples_dir = Path(__file__).parent

    # Get all example files in order
    example_files = sorted(examples_dir.glob("0*.py"))

    if not example_files:
        print("No example files found!")
        return

    print("="*70)
    print("Python Optimization Examples - Performance Demonstrations")
    print("="*70)
    print(f"\nFound {len(example_files)} examples to run\n")

    for example_file in example_files:
        run_example(example_file)

    print(f"\n{'='*70}")
    print("All examples completed!")
    print('='*70)
    print("\nKey Takeaways:")
    print("  1. Sets are 100-200x faster than lists for membership testing")
    print("  2. Dicts are essential for O(1) lookups and counting operations")
    print("  3. __slots__ can reduce memory usage by ~30% for many instances")
    print("  4. Choosing the right container matters for performance at scale")
    print("\nSee QUICK_REFERENCE.md for optimization patterns!")


if __name__ == "__main__":
    main()
