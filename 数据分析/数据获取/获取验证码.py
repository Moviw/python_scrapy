'''************************************************ 
 * @Author: Movix
 * @Date: 2021-07-27 00:26:36
 * @LastEditTime: 2021-07-27 00:49:54
 * @Github: https://github.com/Moviw
 * @FilePath: \数据分析\get_V_code.py
 * @Description: 
 ************************************************'''
import pytesseract
from PIL import Image
def get_yzm(url):
    image=Image.open(url)
    vcode=pytesseract.image_to_string(image)
    return vcode