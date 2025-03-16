import pygame
import math
import sys

# 初始化 Pygame
pygame.init()

# 設置窗口大小
width, height = 1300, 900
ans = -1  # -1未判定，0沒過，1有過
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("排球互動設計")

# 加載排球圖片
volleyball_img = pygame.image.load("volleyball.png")

# 縮小排球圖片到原來的三分之一
volleyball_img = pygame.transform.scale(volleyball_img,
                                        (volleyball_img.get_width() // 4, volleyball_img.get_height() // 4))
volleyball_rect = volleyball_img.get_rect()

# 加載圖片
end_screen_img = pygame.image.load("300Fotolia_71874702_Subscription_L@1200x1200.png")  # 新畫面圖片
end_screen1_img = pygame.image.load("1-10.jpg")

# 設置排球初始位置（偏左下）
volleyball_rect.center = (width // 6, height // 1.5)

# 加載中央圖片
center_img = pygame.image.load("1-10.jpg")  # 請替換成你的圖片路徑
center_img = pygame.transform.scale(center_img, (center_img.get_width() // 13, center_img.get_height() // 7))
center_img_rect = center_img.get_rect(center=(width // 2, height // 1.5))  # 設定圖片置中

# 設置排球速度和加速度
velocity = pygame.Vector2(0, 0)
gravity = 3  # 重力加速度

# 設置鼠標變成手指
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

# 載入手掌游標圖片
hand_img = pygame.image.load("300Fotolia_71874702_Subscription_L@1200x1200.png")
hand_img = pygame.transform.scale(hand_img, (80, 80))  # 調整大小

# 設定鼠標游標
hand_cursor = pygame.cursors.Cursor((0, 0), hand_img)
pygame.mouse.set_cursor(hand_cursor)

# 設置顏色
WHITE = (255, 255, 255)

# 滑鼠的質量和排球的質量
mouse_mass = 3  # 滑鼠質量 1 kg (更新為 1 公斤)
ball_mass = 2.4  # 排球質量 0.5 kg

# 狀態管理
game_state = "playing"  # "playing" -> 正在玩, "end_screen" -> 結束畫面
end_screen_type = None

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

    # 繪製中央圖片
    screen.blit(center_img, center_img_rect)

    # 獲取鼠標位置
    mouse_pos = pygame.mouse.get_pos()

    # 計算滑鼠的速度（即滑鼠的位移）
    mouse_velocity = pygame.Vector2(mouse_pos) - previous_mouse_pos

    # 如果鼠標滑過排球範圍，開始模擬擊球
    if volleyball_rect.collidepoint(mouse_pos) and not ball_launched:
        # 動量守恆：計算排球的初始速度
        if mouse_velocity.length() > 0:  # 確保滑鼠有移動
            ball_velocity = (mouse_mass * mouse_velocity) / ball_mass
            velocity = ball_velocity

        ball_launched = True  # 標記為已經擊球

    # 更新排球位置
    if ball_launched:
        velocity.y += gravity  # 加上重力影響
        volleyball_rect.x += velocity.x
        volleyball_rect.y += velocity.y

        # **處理邊界與網子碰撞（反彈或直接停止）**
        # 碰到左邊界
        if volleyball_rect.left < 0:
            volleyball_rect.left = 0
            velocity.x = 0  # 停止水平移動
            velocity.y = 0  # 停止鉛直移動
            ans = 0
            gravity = 0  # 重力加速度

        # 碰到右邊界
        if volleyball_rect.right > width:
            volleyball_rect.right = width
            velocity.x = 0  # 停止水平移動
            velocity.y = 0  # 停止鉛直移動
            ans = 0
            gravity = 0  # 重力加速度

        # 碰到底部（地板）
        if volleyball_rect.bottom > height:
            volleyball_rect.bottom = height
            velocity.x = 0  # 停止水平移動
            velocity.y = 0  # 停止垂直移動
            if (volleyball_rect.x <= (width // 2)):
                ans = 0
            else:
                ans = 1

        # 碰到網子
        if ((volleyball_rect.x >= (width * 10 / 21)) and (volleyball_rect.x <= (width * 11 / 21))) and (
                volleyball_rect.y < (height / 2)):
            velocity.x = 0  # 停止水平移動
            velocity.y = 0  # 停止垂直移動
            ans = 0
            gravity = 0  # 重力加速度

        # 碰到頂部
        if volleyball_rect.top < 0:
            volleyball_rect.top = 0
            velocity.y = -velocity.y  # 反彈
            ans = -1

        '''# 確保排球不會超出螢幕
        if volleyball_rect.left < 0 or volleyball_rect.right > width:
           velocity.x = -velocity.x  # 撞牆反彈
        if volleyball_rect.top < 0 or volleyball_rect.bottom > height:
           velocity.y = -velocity.y  # 撞天花板或地板反彈'''

    if ans != -1:
        if ans == 1:
            game_state == "end_screen"
            # 顯示結束畫面
            screen.blit(end_screen_img, (0, 0))
        else:
            game_state == "end_screen1"
            # 顯示結束畫面
            screen.blit(end_screen1_img, (0, 0))

    # 畫出排球
    if ans == -1:
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