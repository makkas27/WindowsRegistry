from winreg import *

key = OpenKey(HKEY_CURRENT_USER, 'Console', 0, KEY_READ)
val, regtype = QueryValueEx(key, 'ColorTable04')
CloseKey(key)
key = OpenKey(HKEY_CURRENT_USER, 'Console', 0, KEY_ALL_ACCESS)
SetValueEx(key, 'ColorTable05', 0, REG_DWORD, '8388736')
CloseKey(key)

print(val)

print(regtype)

