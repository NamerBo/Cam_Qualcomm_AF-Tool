adb root
adb remount
adb logcat -c
adb logcat -G 200M
adb logcat -vtime >./SAG_Comp/"%date:~8,2%-%date:~11,2%_%time:~0,2%.%time:~3,2%.%time:~6,2%.txt"