adb root
adb remount
adb shell "echo dumpSensorEEPROMData=FALSE >> /vendor/etc/camera/camxoverridesettings.txt"
adb shell pkill camera*