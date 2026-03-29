@echo off
cd my-dsa-dataset

for /L %%i in (1,1,10) do (
    (
        echo import subprocess
        echo import json
        echo.
        echo def parse_output(output):
        echo     if "passed" in output:
        echo         return {"status": "passed"}
        echo     return {"status": "failed"}
        echo.
        echo if __name__ == "__main__":
        echo     result = subprocess.run(["python", "-m", "pytest", "task_tests.py", "-v"], capture_output=True, text=True)
        echo     output = result.stdout + result.stderr
        echo     print(json.dumps(parse_output(output)))
    ) > "task-%%i\parser.py"
    echo Created parser.py in task-%%i
)

echo All parser.py files created!