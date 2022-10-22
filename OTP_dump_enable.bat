adb root
adb remount
adb shell "echo dumpSensorEEPROMData=TRUE >> /vendor/etc/camera/camxoverridesettings.txt"
adb shell pkill camera*