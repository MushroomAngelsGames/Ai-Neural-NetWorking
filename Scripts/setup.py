import sys
from cx_Freeze import setup,Executable


build_exe_options = {'packages':['pygame'],
                     'include_files':['..\Imagens','..\Music','CreateMap','Interface','Neural','Objects']}

base = None
if sys.platform == 'win32':
    base = "Win32GUI"

setup(
    name ="Neural NetWorking",
    version="0.1",
    description="Inteligencia Artifical - by Luiz Felipe Marian",
    options = {'build_exe':build_exe_options},                      
    executables = [Executable(script="MenuGame.py",base=base,icon="..\Imagens\icon.ico",copyright="Copyright (C) 2023 Mushroom Angels Games"),]
)
