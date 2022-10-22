adb root
adb remount
adb push camxoverridesettings.txt vendor/etc/camera
::adb shell input keyevent 4 ::开启手机
::adb shell input keyevent 82 ::解锁屏幕
adb shell pkill camera*
::timeout /t 1
::adb shell am start jp.co.sony.mc.camera/.CameraLauncher ::open sony_camera
::timeout /t 2
:: adb shell input keyevent 27 ::拍照
::adb shell pkill camera*
adb shell sync