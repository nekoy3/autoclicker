import pyautogui
import time
import sys

def load_saved_data(filename):
    with open(filename, 'r') as f:
        x, y = map(int, f.readline().strip().split(','))
        scheduled_time = f.readline().strip()
    return x, y, scheduled_time

def save_mouse_position(filename):
    x, y = pyautogui.position()
    with open(filename, 'w') as f:
        f.write(f'{x},{y}\n')

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "start":
        x, y, scheduled_time = load_saved_data("point.txt")
        print(f"{scheduled_time}に座標({x},{y})をクリックします。")

        while True:
            current_time = time.strftime('%H:%M:%S')
            if current_time == scheduled_time:
                pyautogui.click(x, y)
                print("実行完了。")
                break
            time.sleep(1)

    else:
        print("マウスカーソルを移動してEnterキーを入力してください。")
        input()
        
        save_mouse_position("point.txt")

        while True:
            profile_time = input("実行時間を入力してください。例：hh:MM:ss: ")
            try:
                time.strptime(profile_time, '%H:%M:%S')
                break
            except ValueError:
                print("フォーマットが正しくありません。再度入力してください。")

        with open("point.txt", 'a') as f:
            f.write(f'{profile_time}\n')

        print(f"{profile_time}に座標({x},{y})をクリックするプロファイルです.")

if __name__ == "__main__":
    main()
