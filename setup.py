from cx_Freeze import setup, Executable

base = None    

executables = [Executable("degui.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Speed Tracker",
    options = options,
    version = "1.2",
    description = 'Choose any video file it will process it and give the result as the speed of cars',
    executables = executables
)