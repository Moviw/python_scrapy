'''************************************************ 
 * @Author: Movix
 * @Date: 2021-07-29 20:35:53
 * @LastEditTime: 2021-07-29 21:43:15
 * @Github: https://github.com/Moviw
 * @FilePath: /基础/摄像头.py
 * @Description: 
 ************************************************'''

# # 调用摄像头获取每帧（模板）

# 调用摄像头逐帧实时处理模板
# 不需修改任何代码，只需修改process_frame函数即可
# 同济子豪兄 2021-7-8

# 导入opencv-python
import cv2
import time

# 获取摄像头，传入0表示获取系统默认摄像头
cap = cv2.VideoCapture(0)

# 打开cap
cap.open(0)

# 无限循环，直到break被触发
while cap.isOpened():
    # 获取画面
    success, frame = cap.read()

    # 水平镜像翻转图像，使图中左右手与真实左右手对应
    # 参数 1：水平翻转，0：竖直翻转，-1：水平和竖直都翻转
    frame=cv2.flip(frame,1)

    
    if not success:
        print('Error')
        break

    # ## !!!处理帧函数
    # frame = process_frame(frame)
    
    # 展示处理后的三通道图像
    cv2.imshow('my_window',frame)
    if cv2.waitKey(1) in [ord('q'),27]: # 按键盘上的q或esc退出（在英文输入法下）
        break
    
# 关闭摄像头
cap.release()

# 关闭图像窗口
cv2.destroyAllWindows()
