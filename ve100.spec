
# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import copy_metadata, collect_data_files, collect_submodules

# Lấy metadata và submodules của google-auth
datas_auth = copy_metadata('google-auth')
datas_oauth = copy_metadata('google-auth-oauthlib')

hidden_google = collect_submodules('google.auth') + collect_submodules('google_auth_oauthlib')

block_cipher = None

a = Analysis(
    ['ve100.py'],
    pathex=['/home/pi/VE100'],
    binaries=[],
    datas=datas_auth + datas_oauth,
    hiddenimports=[
        'ipaddress',
        'urllib',
        'urllib.parse',
        'pathlib',
        'six',
        'PIL',
        'PIL._imagingtk',
        'PIL._tkinter_finder',
        'google',
        'google.auth',
        'google.auth.transport',
        'google.auth.transport.requests',
        'google.oauth2',
        'google_auth_oauthlib',
    ] + hidden_google,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ve100',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ve100',
)
