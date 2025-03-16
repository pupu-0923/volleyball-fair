import os
import time
import pygame
import pygetwindow as gw
import sys
import pyautogui
import threading

# 設置窗口大小
width, height = 1300, 700
running_animation = False  # 防止動畫重複執行

def show_volleyball_animation():
    global running_animation
    running_animation = True  # 設定動畫執行中
    pygame.init()

    # 設定 Pygame 全螢幕 + 無邊框
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.NOFRAME)
    pygame.display.set_caption("排球互動設計")

    # 最小化包含特定關鍵字的視窗
    def minimize_window_by_keyword(keyword):
        for window in gw.getWindowsWithTitle(""):
            if keyword.lower() in window.title.lower():
                window.minimize()

    minimize_window_by_keyword("記事本")
    minimize_window_by_keyword("word")

    # 確保圖片路徑正確
    image_path = os.path.join(os.path.dirname(__file__), "volleyball.png")
    if not os.path.exists(image_path):
        print("錯誤：找不到 volleyball.png，請確認檔案是否存在！")
        running_animation = False
        return

    # 加載並縮小排球圖片
    volleyball_img = pygame.image.load(image_path)
    volleyball_img = pygame.transform.scale(volleyball_img, (volleyball_img.get_width() // 3, volleyball_img.get_height() // 3))
    volleyball_rect = volleyball_img.get_rect()

    # 設置排球初始位置（偏左下）
    volleyball_rect.center =_
