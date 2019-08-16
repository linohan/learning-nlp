import jieba.posseg as psg
sent = '中文分词是文本处理不可或缺的一步！'
seg_list = psg.cut(sent)

# print(' '.join(['{0}/{1}'.format(w, t) for w, t in seg_list]))
# segs = list(temp)
# print(segs[0].word, segs[0].flag)
for seg in seg_list:
    print(type(seg))
