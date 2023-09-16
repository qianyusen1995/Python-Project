def slidingWindow(t):
    need = {}  # 满足条件的窗口
    window = {} # 窗口计数器
    # need 和 window 一般是用字典表示，有时候也可能会用列表或者其他数据结构表示，具体的应该根据题目变化，有的题目可能就不需要这两个变量。
    for i in t: # 初始化模板数据
        need[i] = need.get(i, 0) + 1
    print (need)

t1 = [1,2,3,4,1]
print (slidingWindow(t1))
