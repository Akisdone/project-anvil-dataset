@echo off
setlocal enabledelayedexpansion

cd my-dsa-dataset

for /L %%i in (2,1,10) do (
    echo Adding Anvil files to task-%%i...
    
    if exist "task-%%i\tests.py" (
        ren "task-%%i\tests.py" "task_tests.py"
    )
    
    xcopy task-1\run_script.sh task-%%i\ /Y
    xcopy task-1\parser.py task-%%i\ /Y
    xcopy task-1\Dockerfile task-%%i\ /Y
    
    (
        echo task_id,task_name,difficulty,description
        echo %%i,Task %%i,medium,DSA Task %%i
    ) > "task-%%i\tasks.csv"
    
    echo Done with task-%%i
)

echo.
echo All Anvil files added!