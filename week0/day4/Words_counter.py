import re

#定义常见停用词列表
stop_words = ["the", "a", "an", "is", "are", "it", "in", "on", "at", "and", "or", "of", "to", "we", "its", "all", "that", "just", "not", "for", "here", "this"]

def count_words(filename):
    #读取文件
    try:
        #f = open(filename, "r", encoding="utf-8")
        with open(filename, "r", encoding="utf-8") as f:
            #读取文件并转化为小写
            content = f.read().lower()
        #用正则re.split按非字母拆分出单词
        words = re.split(r"[^a-zA-Z]", content)
        
        #定义字典来存储每个单词出现的次数
        dic = dict()
        
        #遍历单词列表
        for word in words:
            if word and word not in stop_words:
                if word in dic:
                    dic[word] += 1
                else:
                    dic[word] = 1
        
        #按次数降序排序，取前20
        sort_words = sorted(dic.items(), key = lambda x: x[1], reverse = True)
        top_20 = sort_words[:20]
        
        #输出出现最多的20个单词
        print("======top20词频======")
        for w, num in top_20:
            print(f"{w} {num}")
        #f.close()
    except FileNotFoundError:
        print("文件未找到！！")

    



if __name__ == "__main__":
    count_words(r"day4/article.txt")