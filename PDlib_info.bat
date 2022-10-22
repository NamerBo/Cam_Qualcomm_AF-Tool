adb root
adb remount
adb shell "echo enablePDLibLog=3 >> /vendor/etc/camera/camxoverridesettings.txt"
adb shell pkill camera*