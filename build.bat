cd /d %~dp0
pyinstaller update_nexus_library_location.py --onefile --icon Nexus3.ico --clean --distpath .

REM this equals to "rm -rf build" on linux
rmdir /S /Q build
