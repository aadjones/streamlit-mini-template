import shutil, os, sys
from pathlib import Path

PROJECT_DIR = Path.cwd()

def main():
    include_tests = "{{ cookiecutter.include_tests }}"
    if include_tests.lower() != "y":
        test_dir = PROJECT_DIR / "tests"
        if test_dir.exists():
            shutil.rmtree(test_dir)
            print("Removed tests/ because include_tests != 'y'")
    else:
        print("Tests included.")

if __name__ == "__main__":
    main()
