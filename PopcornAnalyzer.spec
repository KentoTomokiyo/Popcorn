# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

project_dir = Path(SPECPATH)
app_script = project_dir / "popcorn_analyzer_windows_easy.py"

def first_existing(paths):
    for p in paths:
        if p.exists():
            return p
    return None

ffmpeg = first_existing([
    project_dir / "ffmpeg.exe",
    project_dir / "ffmpeg" / "bin" / "ffmpeg.exe",
])

ffprobe = first_existing([
    project_dir / "ffprobe.exe",
    project_dir / "ffmpeg" / "bin" / "ffprobe.exe",
])

binaries = []
if ffmpeg:
    binaries.append((str(ffmpeg), '.'))
if ffprobe:
    binaries.append((str(ffprobe), '.'))

a = Analysis(
    [str(app_script)],
    pathex=[str(project_dir)],
    binaries=binaries,
    datas=[],
    hiddenimports=[
        "PIL._tkinter_finder",
        "scipy.signal",
        "scipy.ndimage",
        "soundfile",
        "yt_dlp",
        "matplotlib.backends.backend_agg",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PopcornAnalyzer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='PopcornAnalyzer',
)
