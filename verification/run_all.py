"""Run the repository's four small, dependency-free algebra checks."""
from pathlib import Path
import subprocess
import sys

here = Path(__file__).resolve().parent
checks = ("check_covariance_identity.py", "check_quadratic_identity.py",
          "check_theta_moments.py", "check_integer_recovery.py")
for name in checks:
    completed = subprocess.run([sys.executable, str(here / name)],
                               capture_output=True, text=True, check=False)
    print(name)
    print(completed.stdout, end="")
    if completed.returncode:
        print(completed.stderr, file=sys.stderr)
        raise SystemExit(completed.returncode)
print("All four checks passed.")

