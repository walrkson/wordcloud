#分词
import jieba
cont = open('H:\zhuxian.txt','r', encoding='utf-8').read()
segment = jieba.cut(cont)
seg_list = list(segment)
seg_str = ' '.join(seg_list)
#生成词云
from wordcloud import WordCloud
import matplotlib.pyplot as plt
zhuxian_wordcloud = WordCloud(font_path='H:\words.ttf').generate(seg_str)
plt.imshow(zhuxian_wordcloud)
plt.axis("off")
plt.show()

