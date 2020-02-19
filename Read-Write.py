import winreg as _winreg

REG_PATH = r"SAM\SAM\Domains\Account\Users\000001F4"

def set_reg(name, value):
    try:
        _winreg.CreateKey(_winreg.HKEY_LOCAL_MACHINE, REG_PATH)
        registry_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, REG_PATH, 0,
                                       _winreg.KEY_WRITE)
        _winreg.SetValueEx(registry_key, name, 0, _winreg.REG_DWORD_LITTLE_ENDIAN, value)
        _winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

def get_reg(name):
    try:
        registry_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, REG_PATH, 0,
                                       _winreg.KEY_READ)
        value, regtype = _winreg.QueryValueEx(registry_key, name)
        _winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None


#set_reg("mysetting", 115)

print( get_reg("F"))
print(get_reg("V"))