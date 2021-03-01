from aip import AipNlp

class baidu_nlp_ts(object):
    """对百度的自然语言api进行使用和测试"""
    def __init__(self):
        APP_ID = '23707603'
        API_KEY = 'gZtlW60sE1GwCdBmed02ZSUi'
        SECRET_KEY = 'qqFxA27KGVy4fYWFOPI8mSmDvtsIeSB0'

        self.client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


    def tst_pingtai(self):
        # """"""
        # text = "百度是一家高科技公司"
        #
        # """ 调用词法分析 """
        # res = self.client.lexer(text);
        # print(res)
        #
        # """ 调用依存句法分析 """
        # res = self.client.depParser(text);
        # print(res)
        #
        # word = "张飞"
        #
        # """ 调用词向量表示 """
        # res = self.client.wordEmbedding(word);
        # print(res)
        #
        # text = "床前明月光"
        #
        # """ 调用DNN语言模型 """
        # res = self.client.dnnlm(text);
        # print(res)
        #
        # word1 = "海洋"
        # word2 = "天空"
        # word3 = "海"
        #
        # """ 调用词义相似度 """
        # res = self.client.wordSimEmbedding(word1, word2);
        # res1 = self.client.wordSimEmbedding(word1, word3);
        # print(res)
        # print(res1)
        #
        # text1 = "浙富股份"
        #
        # text2 = "万事通自考网"
        #
        # """ 调用短文本相似度 """
        # res = self.client.simnet(text1, text2);
        #
        # """ 如果有可选参数 """
        # options = {}
        # options["model"] = "CNN"
        #
        # """ 带参数调用短文本相似度 """
        # self.client.simnet(text1, text2, options)
        #
        # text = "三星电脑电池不给力"
        #
        # """ 调用评论观点抽取 """
        # res = self.client.commentTag(text);
        #
        # """ 如果有可选参数 """
        # options = {}
        # options["type"] = 13
        #
        # """ 带参数调用评论观点抽取 """
        # res = self.client.commentTag(text, options)
        #

        """ 调用情感倾向分析 """
        texts = ["苹果是一家伟大的公司", "这有一个水杯"]
        for text in texts:
            res = self.client.sentimentClassify(text)
            print(res)


        #
        # title = "iphone手机出现“白苹果”原因及解决办法，用苹果手机的可以看下"
        #
        # content = "如果下面的方法还是没有解决你的问题建议来我们门店看下成都市锦江区红星路三段99号银石广场24层01室。"
        #
        # """ 调用文章标签 """
        # self.client.keyword(title, content);

if __name__ == "__main__":
    b = baidu_nlp_ts()
    b.tst_pingtai()
