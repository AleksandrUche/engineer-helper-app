# -*- mode: python ; coding: utf-8 -*-

added_file = [
    ('./data/images/icon/*.ico', 'icon'),
    ('./data/images/images_vesseles/*.png', 'images_vesseles'),
    ('./data/images/images_metal_rolling/*.png', 'images_metal_rolling'),
]

a = Analysis(
    ['.//main//main.py'],
    pathex=[],
    binaries=[],
    datas=added_file,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='Engineer helper 1.0.1',
    debug=False,
    strip=False,
    upx=False,
    clean=True,
    runtime_tmpdir=None,
    console=False,
    icon=['.//data//images//icon//icon.ico']
)
