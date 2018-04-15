from cx_Freeze import setup, Executable

setup(
    name="Shooter",
    version="1.0",
    description="Shooter-Retravel",
    executables=[Executable(script="launcher.py", icon="icone.ico", base="Win32GUI")])
