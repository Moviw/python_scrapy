'''************************************************ 
 * @Author: Movix
 * @Date: 2021-07-28 20:27:28
 * @LastEditTime: 2021-07-29 13:41:59
 * @Github: https://github.com/Moviw
 * @FilePath: /数据可视化/ciyun.py
 * @Description: 
 ************************************************'''
import jieba
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
#! scipy.disc中的imread已经被删除了以后都用这个
from imageio import imread

def get_words(text_path,useless_word=[]):  
    '''
    ************************************************ 
     * @description: 获取经清洗后的词表,且自动过滤常见的标点符号
     * @param {
         useless_word:无用词表，默认类型为列表
         text_path:文件路径}
     * @return {
         washed_word_List:经清洗后的词表}
    ************************************************
     '''  
 
    useless_already=[]
    #*这里直接借助停用词表将常用词剔除
    with open('停用词表.txt','r',encoding='utf-8') as fp:
       for line in fp.readlines():                          #依次读取每行  
            useless_already.append(line.strip())
    useless_word=useless_word+useless_already
    #获取源文件
    with open(text_path,'r',encoding='utf-8') as fp:     #TODO这里改成目标文件的路径
        words=fp.read()
        
    #被清洗过的词表
    washed_word_List=[]
    #未被清洗过的词表
    unwashed_word_List=[]
  

    #切割后的词表  类型为容器
    unwashed_words = jieba.cut(words)
    
    # jieba.cut 方法接受四个输入参数: 
    #     1.需要分词的字符串；
    #     剩下三种没用
    # 待分词的字符串可以是 unicode 或 UTF-8 字符串、GBK 字符串。注意：不建议直接输入 GBK 字符串，可能无法预料地错误解码成 UTF-8
    # jieba.cut 返回的结构都是一个可迭代的 generator，可以使用 for 循环来获得分词后得到的每一个词语(unicode)
    # jieba.lcut 直接返回 list

    for word in unwashed_words:
        #将容器内的词加入未被清洗过的词表中
        unwashed_word_List.append(word)

    print('开始词频清洗')
    #词频清洗  清洗诸如“的”,"其中","左右",之类的无用词汇
    for word in unwashed_word_List:

        if word not in useless_word:
            washed_word_List.append(word)
    
    print('无用词清洗完毕')
    return washed_word_List



def get_frequency(washed_word_List):
    '''
    ************************************************ 
     * @description: 
     * @param {*}
     * @return {*}
    ************************************************
     '''    
    count_dict = {}
    for item in washed_word_List:
        if item in count_dict.keys():
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    return count_dict



def get_non_frequencied_wordCloud(washed_word_List,pic_path):
    '''
    ************************************************ 
     * @description: 获取一张词云图，该词云图与词表的单词出现频次无关
     * @param {
         washed_word_List:一个经清洗过的词表
         pic_path:背景图片路径}
     * @return {
         一张绚丽多彩的词云图}
    ************************************************
     '''    
    new_text = ' '.join(washed_word_List)
   
    img_mask = imread(pic_path)

    print('正在生成词云...')
    wordcloud = WordCloud(background_color="black",font_path=('C:\\Program Files (x86)\\Thunder '             #这里是字符路径
     'Network\\Thunder\\profiles\\AdData\\AdTips\\Functional\\Scenes\\MyDock\\pingfang0.ttf'),                   
      mask=img_mask,max_font_size=150, ).generate(new_text)              
    print('词云生成完毕')

    plt.imshow(wordcloud)
    plt.axis('off')
    plt.savefig('picture_non.jpg',dpi=200)
    plt.show()



def get_frequencied_wordCloud(washed_word_List,pic_path):
    '''
    ************************************************ 
     * @description: 获取一张词云图，该词云图与词表的单词出现频次有关
     * @param {
         washed_word_List:一个经清洗过的词表
         pic_path:背景图片路径}
     * @return {
         一张绚丽多彩的词云图}
    ************************************************
     '''   
    img_mask = imread(pic_path)

    print('正在生成词云...')
    wordcloud = WordCloud(background_color="black",font_path=('C:\\Program Files (x86)\\Thunder '             #这里是字符路径
     'Network\\Thunder\\profiles\\AdData\\AdTips\\Functional\\Scenes\\MyDock\\pingfang0.ttf'),                   
     mask=img_mask,max_font_size=1000).generate_from_frequencies(washed_word_List)       #max_font_size可用于调节字体大小              
    print('词云生成完毕')

    plt.imshow(wordcloud)
    plt.axis('off')
    plt.savefig('picture.jpg',dpi=200)
    plt.show()



if __name__ == '__main__':
    #无用词表  用于清洗无用词
    useless_word = []    #TODO在这里加入需要屏蔽的无用字符
   
    text_path='article.txt'  #TODO在这里加入源文本的路径
  
    pic_path = ('china.jpg')         #TODO这里改成背景图片文件的路径
    #!这里的图片必须是背景透明图 普通的图在这不行
    washed_word_List = get_words(text_path,useless_word)
    frequiencied_washed_word_List=get_frequency(washed_word_List)
    
    # get_non_frequencied_wordCloud(washed_word_List,pic_path)

    get_frequencied_wordCloud(frequiencied_washed_word_List,pic_path)
