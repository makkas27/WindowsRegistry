import winreg

reg_connection = winreg.ConnectRegistry(winreg.HKEY_CURRENT_USER);
reg_key = winreg.OpenKey(reg_connection, r"")
.