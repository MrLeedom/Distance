'''
曼哈顿距离：想象你在曼哈顿要从一个十字路口到另外一个十字路口，驾驶距离是两点间的直线距离吗？
显然不是，除非你能创越大楼，实际驾驶距离就是这个＂曼哈顿距离＂
曼哈顿距离：绝对值累加
'''
import numpy as np

def Manhattan(vec1,vec2):
    npvec1,npvec2 = np.array(vec1),np.array(vec2)
    return np.abs(npvec1-npvec2).sum()

def main():
    a,b = [1,2],[3,-5]
    num = Manhattan(a,b)
    print('distance = ',num)

if __name__ == '__main__':
    main()