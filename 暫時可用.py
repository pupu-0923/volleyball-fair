import os
import time
import pygame
import pygetwindow as gw
import sys
import pyautogui

# 設置窗口大小
width, height = 1300, 700

def show_volleyball_animation():
    pygame.init()
    import pygetwindow as gw

    # 設定 Pygame 全螢幕 + 無邊框
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.NOFRAME)

    # 取得視窗名稱
    pygame.display.set_caption("排球互動設計")

    # 找到視窗（根據部分標題）
    window = gw.getWindowsWithTitle("記事本")  # 假設要找 "記事本" 視窗
    if window:
        window[0].minimize()  # 最小化視窗
        # 找到視窗（根據部分標題）
    windo = gw.getWindowsWithTitle("Word")  # 假設要找 "記事本" 視窗
    if windo:
        windo[0].minimize()  # 最小化視窗


    # 確保圖片路徑正確
    image_path = os.path.join(os.path.dirname(__file__), "volleyball.png")
    if not os.path.exists(image_path):
        print("錯誤：找不到 volleyball.png，請確認檔案是否存在！")
        return

    # 加載並縮小排球圖片
    volleyball_img = pygame.image.load(image_path)
    volleyball_img = pygame.transform.scale(volleyball_img, (volleyball_img.get_width() // 3, volleyball_img.get_height() // 3))
    volleyball_rect = volleyball_img.get_rect()

    # 設置排球初始位置（偏左下）
    volleyball_rect.center = (width // 4, height - 100)

    # 設置排球速度和重力
    velocity = pygame.Vector2(0, 0)
    gravity = 1  # 重力加速度

    # 設置鼠標變成手指
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

    # 設置顏色
    WHITE = (255, 255, 255)

    # 滑鼠的質量和排球的質量
    mouse_mass = 0.5  # 滑鼠質量
    ball_mass = 0.8  # 排球質量


    # 遊戲循環
    running = True
    ball_launched = False  # 控制排球是否被擊打
    previous_mouse_pos = pygame.Vector2(0, 0)  # 前一幀的滑鼠位置

    while running:
        screen.fill(WHITE)  # 填充背景顏色

        # 處理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 獲取鼠標位置
        mouse_pos = pygame.mouse.get_pos()

        # 計算滑鼠的速度（即滑鼠的位移）
        mouse_velocity = pygame.Vector2(mouse_pos) - previous_mouse_pos

        # 如果鼠標滑過排球範圍，開始模擬擊球
        if volleyball_rect.collidepoint(mouse_pos) and not ball_launched:
            if mouse_velocity.length() > 0:  # 確保滑鼠有移動
                ball_velocity = (mouse_mass * mouse_velocity) / ball_mass
                velocity = ball_velocity
            ball_launched = True  # 標記為已經擊球

        # 更新排球位置
        if ball_launched:
            velocity.y += gravity  # 加上重力影響
            volleyball_rect.x += velocity.x
            volleyball_rect.y += velocity.y

            # 碰撞處理：確保排球不會超出邊界
            if volleyball_rect.left < 0:
                volleyball_rect.left = 0
                velocity.x = 0
            if volleyball_rect.right > width:
                volleyball_rect.right = width
                velocity.x = 0
            if volleyball_rect.bottom > height:
                volleyball_rect.bottom = height
                velocity.y = 0
            if volleyball_rect.top < 0:
                volleyball_rect.top = 0
                velocity.y = 0

        # 畫出排球
        screen.blit(volleyball_img, volleyball_rect)

        # 更新顯示
        pygame.display.flip()

        # 設定遊戲更新頻率
        pygame.time.Clock().tick(60)

        # 更新前一幀的滑鼠位置
        previous_mouse_pos = pygame.Vector2(mouse_pos)

    # 退出 Pygame
    pygame.quit()
    sys.exit()

# 🔍 檢查開啟的檔案並觸發排球動畫
last_detected = None  # 防止重複觸發

def check_open_files():
    global last_detected
    print("開始監視開啟的檔案...")
    while True:
        open_windows = gw.getAllTitles()
        for window in open_windows:
            if ("txt" in window.lower() or "word" in window.lower() ) and window != last_detected:
                print(f"偵測到檔案開啟：{window}")
                last_detected = window
                show_volleyball_animation()

        time.sleep(2)

# 開始執行
check_open_files()
