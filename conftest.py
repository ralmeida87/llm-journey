"""Ensure the project root is on sys.path so absolute imports work in tests."""
import sys, pathlib, os

root = pathlib.Path(__file__).parent.resolve()
if str(root) not in sys.path:
    sys.path.insert(0, str(root))
os.environ.setdefault("PYTHONPATH", str(root))  # also helps IDEs / subprocesses
