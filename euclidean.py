'''
欧式距离：常见的那种，源自欧式空间中两点间的距离
'''
import numpy as np
import math

def Euclidean(vec1,vec2):
    npvec1,npvec2 = np.array(vec1),np.array(vec2)
    return math.sqrt(((npvec1-npvec2)**2).sum())

def main():
    a,b=[1,2],[4,2]
    num = Euclidean(a,b)
    print('distance = ',num)
    
if __name__ == '__main__':
    main()
