-- 定义一个函数来切换到英文输入法
on switchToEnglishInput()
    set currentInputSource to do shell script "defaults read ~/Library/Preferences/com.apple.HIToolbox.plist AppleSelectedInputSources | grep 'KeyboardLayout Name' | awk -F '\"' '{print $4}'"
    if currentInputSource contains "Pinyin" or currentInputSource contains "Simplified" then
        do shell script "osascript -e 'tell application \"System Events\" to key code 49 using {command down, option down}'"
        delay 1
    end if
end switchToEnglishInput

tell application "System Events"
    -- 确保输入法为英文
    my switchToEnglishInput()
    -- 打开Spotlight搜索
    keystroke space using {command down}
    delay 2

    -- 确保输入法为英文
    my switchToEnglishInput()
    -- 输入 "WeChat" 并按下回车键
    keystroke "WeChat"
    delay 2
    keystroke return
    delay 5

    -- 确保输入法为英文
    my switchToEnglishInput()
    -- 打开微信搜索框
    keystroke "f" using {command down}
    delay 2

    -- 确保输入法为英文
    my switchToEnglishInput()
    -- 输入联系人名称
    keystroke "zhaojie" -- 替换为实际联系人名称
    delay 1
    keystroke return
end tell