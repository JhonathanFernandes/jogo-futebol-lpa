"""Build helper placeholder.

This project is packaged using PyInstaller, not cx_Freeze.
To generate the Windows executable, run:

    pyinstaller --onefile game.py

Then place the `images` and `sounds` folders alongside the generated
`game.exe` inside the `dist` folder.
"""

if __name__ == '__main__':
    print('Use pyinstaller --onefile game.py to build this project.')
