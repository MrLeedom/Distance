'''
夹角余弦：几何中夹角余弦可用来衡量两个向量方向的差异，机器学习中借用这一概念来衡量样本向量之间的差异
'''
import numpy as np
import math

def Cosine(vec1,vec2):
    npvec1,npvec2 = np.array(vec1),np.array(vec2)
    return npvec1.dot(npvec2)/(math.sqrt((npvec1**2).sum())*math.sqrt((npvec2**2).sum()))

def main():
    a,b = [1,2],[3,4]
    num = Cosine(a,b)
    print('distance = ',num)

if __name__ == '__main__':
    main()
