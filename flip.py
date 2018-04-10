import win32api as win32
import win32con

devices = []

def printAllScreen():
    i = 0
    while True:
        try:
            device = win32.EnumDisplayDevices(None,i);
            devices.append(device)
            print("[%d] %s (%s)"%(i,device.DeviceString,device.DeviceName));
            i = i+1;
        except:
            break;
    return i

screen_count=printAllScreen()
x = int(input("\nEnter a display number [0-%d]: "%screen_count))

if (x == 100):
    for device in devices:
        dm = win32.EnumDisplaySettings(device.DeviceName,win32con.ENUM_CURRENT_SETTINGS)
        dm.DisplayOrientation = win32con.DMDO_DEFAULT
        dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
        dm.Fields = dm.Fields & win32con.DM_DISPLAYORIENTATION
        win32.ChangeDisplaySettingsEx(device.DeviceName,dm)

if (x == 200):
    for device in devices:
        dm = win32.EnumDisplaySettings(device.DeviceName,win32con.ENUM_CURRENT_SETTINGS)
        dm.DisplayOrientation = win32con.DMDO_180
        dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
        dm.Fields = dm.Fields & win32con.DM_DISPLAYORIENTATION
        win32.ChangeDisplaySettingsEx(device.DeviceName,dm)

device = win32.EnumDisplayDevices(None,x);
print("Rotate device %s (%s)"%(device.DeviceString,device.DeviceName));

dm = win32.EnumDisplaySettings(device.DeviceName,win32con.ENUM_CURRENT_SETTINGS)
dm.DisplayOrientation = win32con.DMDO_180
dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth
dm.Fields = dm.Fields & win32con.DM_DISPLAYORIENTATION
win32.ChangeDisplaySettingsEx(device.DeviceName,dm)
