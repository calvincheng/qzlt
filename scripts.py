import subprocess


def run_tests():
    """
    Run all unit tests
    Identical to `python3 -m unittest`
    """
    subprocess.run(["python3", "-m", "unittest"])
