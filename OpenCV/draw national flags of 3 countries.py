import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
#from queue import Queue

m = 2**8 - 1


def DDA(a, x1, y1, x2, y2):
    """
    Thuật toán vẽ đường thẳng
    :param a:
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """
    Dx = x2 - x1
    Dy = y2 - y1
    step = max(abs(Dx), abs(Dy))
    xi = Dx / step
    yi = Dy / step
    x = x1
    y = y1
    a[x, y] = 1
    for i in range(1, step + 1):
        x += xi
        y += yi
        x_t = int(round(x, 0))
        y_t = int(round(y, 0))
        a[x_t, y_t] = 1
    return a

def Star(a, R, xI, yI):
    """
    Vẽ ngôi sao và đánh dấu tô màu
    :param a: ma trận đánh dấu
    :param R: bán kính hình tròn ngoại tiếp ngôi sao
    :param xI: tâm ngôi sao / hình tròn
    :param yI:  tâm ngôi sao / hình tròn
    :return: mảng đã đánh dấu a
    """

    x = xI - R
    y = yI

    cos = math.cos(72 * math.pi / 180)
    sin = math.sin(72 * math.pi / 180)

    a[x, y] = 1  # điểm thứ 1

    x2 = int((x - xI) * cos - (y - yI) * sin + xI)
    y2 = int((x - xI) * sin + (y - yI) * cos + yI)
    a[x2, y2] = 1  # điểm thứ 2

    x3 = int((x2 - xI) * cos - (y2 - yI) * sin + xI)
    y3 = int((x2 - xI) * sin + (y2 - yI) * cos + yI)
    a[x3, y3] = 1  # điểm thứ 3

    x4 = int((x3 - xI) * cos - (y3 - yI) * sin + xI)
    y4 = int((x3 - xI) * sin + (y3 - yI) * cos + yI)
    a[x4, y4] = 1  # điểm thứ 4

    x5 = x2
    y5 = int((x4 - xI) * sin + (y4 - yI) * cos + yI)
    a[x5, y5] = 1  # điểm thứ 5

    # dis = math.sqrt((x-x2)**2 + (y-y2)**2) # Khoảng cách giữa 2 điểm

    # vẽ 5 đường thẳng tạo thành hình ngôi sao
    a = DDA(a, x, y, x3, y3)
    a = DDA(a, x, y, x4, y4)
    a = DDA(a, x2, y2, x5, y5)
    a = DDA(a, x2, y2, x4, y4)
    a = DDA(a, x3, y3, x5, y5)

    # tô màu
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if a[i][j] == 1:
                break
            a[i][j] = -1
        for j in range(a.shape[1] - 1, -1, -1):
            if a[i][j] == 1:
                break
            a[i][j] = -1
    for j in range(a.shape[1]):
        for i in range(a.shape[0]):
            if a[i][j] == 1:
                break
            a[i][j] = -1
        for i in range(a.shape[0] - 1, -1, -1):
            if a[i][j] == 1:
                break
            a[i][j] = -1
    return a

def Bresenham(a, R: int, xI: int, yI: int):
    """
    Thuật toán Bresenham vẽ đường tròn

    :param a: Ma trận đánh dấu
    :param R: bán kính
    :param xI: điểm x tâm
    :param yI: điểm y tâm
    :return:
    """

    # Tô màu 8 điểm
    def paint_8_points(a, x, y, xI, yI):
        a[x + xI][y + yI] = 1
        a[-x + xI][y + yI] = 1
        a[x + xI][-y + yI] = 1
        a[-x + xI][-y + yI] = 1
        a[y + xI][x + yI] = 1
        a[-y + xI][x + yI] = 1
        a[y + xI][-x + yI] = 1
        a[-y + xI][-x + yI] = 1

        return a

    # Vẽ đường tròn
    P = 3 - 2 * R
    x = 0
    y = R
    a = paint_8_points(a, x, y, xI, yI)
    while x <= y:
        if P < 0:
            P = P + 4 * x + 6
        else:
            y -= 1
            P = P + 4 * (x - y) + 10
        a = paint_8_points(a, x, y, xI, yI)
        x += 1

    # Tô màu hình tròn
    x = xI - R
    y = yI
    for i in range(2 * R):
        if a[x, y] == 0:

            x_tmp, y_tmp = x, y
            while a[x_tmp, y_tmp - 1] == 0:
                y_tmp -= 1
                a[x_tmp, y_tmp] = 1

            x_tmp, y_tmp = x, y
            while a[x_tmp, y_tmp + 1] == 0:
                y_tmp += 1
                a[x_tmp, y_tmp] = 1
            a[x, y] = 1

        x += 1
    return a

def Libya():
    k = int(1.618 * 400 // 1)
    a = np.ones((400, k, 3))
    green = np.array([49 / m, 149 / m, 0 / m])

    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            a[i][j] = green

    img = cv2.imshow('Libya', a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def France():
    k = int(1.618 * 400 // 1)
    a = np.ones((400,k,3))
    blue = np.array([150/m, 36/m, 0/m])
    white = np.array([1,1,1])
    red = np.array([57/m, 40/m, 237/m])

    p = k//3
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if j <= p:
                a[i][j] = blue
            elif j <= 2*p:
                a[i][j] = white
            else:
                a[i][j] = red

    img = cv2.imshow('France', a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Italy():
    k = int(1.618 * 400 // 1)
    a = np.ones((400, k, 3))
    green = np.array([53/m,149/m,31/m])
    white = np.ones(3)
    red = np.array([11/m,0,226/m])

    p = k // 3
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if j <= p:
                a[i][j] = green
            elif j <= 2 * p:
                a[i][j] = white
            else:
                a[i][j] = red

    img = cv2.imshow('Italy', a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def Japan():
    k = int(1.618 * 400 // 1)
    A = np.ones((400, k, 3))
    a = np.zeros((400, k))
    a = Bresenham(a, 130, 200, 323)

    white = np.ones(3)
    red = np.array([45/m,0,188/m])

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if a[i][j] == 0:
                A[i][j] = np.array(white)
            else:
                A[i][j] = np.array(red)

    img = cv2.imshow('Japan', A)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def HaLan():
    k = int(1.618 * 400 // 1)
    a = np.ones((400, k, 3))
    red = np.array([1/m,11/m,172/m])
    white = np.ones(3)
    blue = np.array([162/m,40/m,0/m])

    p = 400 // 3
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            if i <= p:
                a[i][j] = red
            elif i <= 2*p:
                a[i][j] = white
            else:
                a[i][j] = blue

    img = cv2.imshow('HaLan', a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def VietNam():
    k = int(1.618 * 400 // 1)
    A = np.ones((400, k, 3))
    a = np.zeros((400, k))
    a = Star(a,130,200,323)

    yellow = np.array([1/m, 255/m, 254/m])
    red = np.array([29/m, 39/m, 217/m])

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if a[i][j] == -1:
                A[i][j] = red
            else:
                A[i][j] = yellow

    img = cv2.imshow('VietNam', A)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Bangladesh():
    k = int(1.618 * 400 // 1)
    A = np.ones((400, k, 3))
    a = np.zeros((400, k))
    a = Bresenham(a, 130, 200, 290)

    green = np.array([70/m, 158/m, 35/m])
    red = np.array([39 / m, 0, 190 / m])

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if a[i][j] == 0:
                A[i][j] = np.array(green)
            else:
                A[i][j] = np.array(red)

    img = cv2.imshow('Bangladesh', A)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Benin():
    k = int(1.618 * 400 // 1)
    a = np.ones((400, k, 3))
    green = np.array([81/m, 135/m, 0])
    yellow = np.array([22/m, 209/m, 252/m])
    red = np.array([45/m, 17/m, 232/m])

    p = k*2//5
    for i in range(a.shape[0]):
        for j in range(p):
            a[i,j] = green

    q = a.shape[0]//2
    for i in range(a.shape[0]):
        for j in range(p,a.shape[1]):
            if i <= q:
                a[i,j] = yellow
            else:
                a[i,j] = red

    img = cv2.imshow('Benin', a)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def BurkinaFaso():
    k = int(1.618 * 400 // 1)
    A = np.ones((400, k, 3))
    a = np.zeros((400, k))
    a = Star(a, 60, 200, 323)

    yellow = np.array([22/m, 209/m, 252/m])
    red = np.array([45/m, 43/m, 239/m])
    green = np.array([73/m, 158/m, 0])

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if a[i][j] == -1:
                if i < A.shape[0]//2-1:
                    A[i][j] = red
                else:
                    A[i][j] = green
            else:
                A[i][j] = yellow

    img = cv2.imshow('Burkina Faso', A)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Cameroon():
    k = int(1.618 * 400 // 1)
    A = np.ones((400, k, 3))
    a = np.zeros((400, k))
    a = Star(a, 40, 175, 323)

    yellow = np.array([9 / m, 244 / m, 247 / m])
    red = np.array([39 / m, 0 / m, 190 / m])
    green = np.array([70 / m, 158 / m, 25/m])

    p = k//3
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if a[i,j]==-1:
                if j < p:
                    A[i,j]=green
                elif j <= 2*p:
                    A[i,j]=red
                else:
                    A[i,j]=yellow
            else:
                A[i,j] = yellow

    img = cv2.imshow('Cameroon', A)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Congo():
    k = int(1.618 * 400 // 1)
    A = np.ones((400, k, 3))
    a = np.zeros((400, k))
    a = Star(a, 80, 100, 100)

    yellow = np.array([24 / m, 214 / m, 247 / m])
    red = np.array([33 / m, 16 / m, 206 / m])
    blue = np.array([255 / m, 127 / m, 0 / m])

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if a[i,j] == -1:
                A[i,j] = blue
            else:
                A[i,j] = yellow

    t = 0
    a = np.zeros((400, k))
    for i in range(320, A.shape[0]):
        a = DDA(a,i,0,t,A.shape[1]-1)
        t+=1

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if a[i,j] == 1:
                A[i,j] = red

    a = np.zeros((400,k))


    for i in range(319,300,-1):
        q = int(i*(A.shape[1]-1)//320)
        a = DDA(a,i,0,0,q)

    for i in range(40):
        n = A.shape[1] - 1
        q = 320 *(i-n)/n + 399
        q = int(q)
        a = DDA(a,399,i,q,A.shape[1]-1)

    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if a[i,j] == 1:
                A[i,j] = yellow
    img = cv2.imshow('Congo', A)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    Libya()
    France()
    Italy()
    Japan()
    HaLan()
    VietNam()
    Bangladesh()
    Benin()
    BurkinaFaso()
    Cameroon()
    Congo()
    pass