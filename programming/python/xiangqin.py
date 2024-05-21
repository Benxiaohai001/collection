import pyautogui

# screenshot = pyautogui.screenshot()
# 找到微信图标的位置
icon_position = pyautogui.locateOnScreen('./xq.png', confidence=0.8)  # 请替换为你的微信图标的截图

# 计算微信图标的中心位置
icon_center = pyautogui.center(icon_position)

# 双击微信图标
pyautogui.doubleClick(icon_center)

# 等待一段时间，让微信客户端打开
pyautogui.sleep(5)

# 找到搜索框的位置
search_position = pyautogui.locateOnScreen('wechat_search.png')  # 请替换为你的搜索框的截图

# 计算搜索框的中心位置
search_center = pyautogui.center(search_position)

# 点击搜索框
pyautogui.click(search_center)

# 输入好友的昵称
pyautogui.write('赵杰')  # 请替换为你的好友的昵称

# 按下回车键
pyautogui.press('enter')