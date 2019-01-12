'''
切比雪夫距离：最大的绝对值差
'''
import numpy as np

def Chebyshev(vec1,vec2):
    npvec1,npvec2 = np.array(vec1),np.array(vec2)
    return max(np.abs(npvec1-npvec2))

def main():
    a,b = [1,2],[3,4]
    num = Chebyshev(a,b)
    print('distance = ',num)

if __name__ == '__main__':
    main()