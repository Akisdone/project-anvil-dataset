import subprocess
import json

def parse_output(output):
    if "passed" in output:
        return {"status": "passed"}
    return {"status": "failed"}

if __name__ == "__main__":
    result = subprocess.run(["python", "-m", "pytest", "task_tests.py", "-v"], capture_output=True, text=True)
    output = result.stdout + result.stderr
    print(json.dumps(parse_output(output)))