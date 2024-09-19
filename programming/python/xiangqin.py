# import pyautogui

# # screenshot = pyautogui.screenshot()
# # 找到微信图标的位置
# icon_position = pyautogui.locateOnScreen('./xq.png', confidence=0.8)  # 请替换为你的微信图标的截图

# # 计算微信图标的中心位置
# icon_center = pyautogui.center(icon_position)

# # 双击微信图标
# pyautogui.doubleClick(icon_center)

# # 等待一段时间，让微信客户端打开
# pyautogui.sleep(5)

# # 找到搜索框的位置
# search_position = pyautogui.locateOnScreen('wechat_search.png')  # 请替换为你的搜索框的截图

# # 计算搜索框的中心位置
# search_center = pyautogui.center(search_position)

# # 点击搜索框
# pyautogui.click(search_center)

# # 输入好友的昵称
# pyautogui.write('赵杰')  # 请替换为你的好友的昵称

# # 按下回车键
# pyautogui.press('enter')

# import pyautogui
# import time

# # 等待几秒钟以确保微信窗口已经打开
# # time.sleep(3)

# # 模拟按下 Command + Space 打开 Spotlight 搜索（适用于 macOS）
# print("打开搜索框");
# pyautogui.hotkey('command', 'space')
# time.sleep(10)
# print("搜索框已打开");

# # 输入 "WeChat" 并按下 Enter 键
# print("输入微信");
# pyautogui.typewrite('微信')
# pyautogui.press('enter')

# # 等待微信窗口打开
# time.sleep(3)

# # 模拟按下 Command + F 打开搜索对话框
# pyautogui.hotkey('command', 'f')

# # 输入联系人名称并按下 Enter 键
# contact_name = '联系人名称'  # 替换为实际联系人名称
# pyautogui.typewrite(contact_name)
# pyautogui.press('enter')


import os

# 创建AppleScript内容
# apple_script = '''
# tell application "System Events"
#     -- 获取当前输入法
#     set currentInputSource to do shell script "defaults read ~/Library/Preferences/com.apple.HIToolbox.plist AppleSelectedInputSources | grep 'KeyboardLayout Name' | awk -F '\"' '{print $4}'"
    
#     -- 如果当前输入法是中文，则切换到英文
#     if currentInputSource contains "Pinyin" or currentInputSource contains "Simplified" then
#         do shell script "osascript -e 'tell application \"System Events\" to key code 49 using {command down, option down}'"
#         delay 1
#     end if

#     -- 打开Spotlight搜索
#     keystroke space using {command down}
#     delay 2
#     -- 输入 "WeChat" 并按下回车键
#     keystroke "WeChat"
#     delay 2
#     keystroke return
#     delay 3
#     -- 打开微信搜索框
#     keystroke "f" using {command down}
#     delay 2
#     -- 输入联系人名称
#     keystroke "zhaojie" -- 替换为实际联系人名称
#     delay 1
#     keystroke return
# end tell
# '''

# 将AppleScript保存为文件并执行
script_path = os.path.join(os.getcwd(), 'open_wechat.scpt')
# with open(script_path, 'w') as file:
#     file.write(apple_script)

os.system(f'osascript {script_path}')