import numpy as np
import cv2

lower_yellow_green = np.array([30, 75, 141])
upper__yellow_green = np.array([90, 255, 255])
yellow_green = (104, 239, 217)#np.array([104, 239, 217])
pink = (97, 12, 254)

def contours(img, lower, upper):
    """
    :param img:
    :return:
    """
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_img, lower, upper)
    color = cv2.bitwise_and(img, img, mask=mask)

    kernel = np.ones((3, 3), dtype=np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(erosion, kernel, iterations=1)
    # dilation = cv2.dilate(edges, kernel, iterations=2)
    # erosion = cv2.erode(dilation, kernel, iterations=2)

    copy_image = np.copy(color)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(copy_image, contours, -1, (255, 0, 0), 3)


    return copy_image, contours
    pass

def choose_center(con):
    #print(len(con))
    m = 0
    tmp = []
    for i in con:
        if len(i) > m:
            m = len(i)
            tmp = i
    if m == 0:
        return []

    avg = [0, 0]
    for i in tmp:
        avg[0]+=i[0][0]
        avg[1]+=i[0][1]
    if m != 0:
        avg[0]//=m
        avg[1]//=m

    return avg
    pass

def main():
    k = 0
    center_list = []
    c = 0

    vid = cv2.VideoCapture(0)

    while True:
        ret, frame = vid.read()
        frame = cv2.flip(frame, 1)
        cv2.imwrite('test2.png',frame)
        if cv2.waitKey(1) == ord('c'):
            "bắt đầu vẽ / ngừng vẽ"
            c = 1 - c
        if cv2.waitKey(1) == 27:
            break
        if cv2.waitKey(1) == ord("a"):
            "giữ phím a để xóa màn hình"
            c = 0
            center_list = []

        if ret:
            if c == 1:
                img, con = contours(frame, lower_yellow_green, upper__yellow_green)
                #  cv2.imshow("frame", frame)
                center = choose_center(con)

                if len(center) > 0:
                    center_list.append(center)
                    # array = cv2.circle(array, center, 10, yellow_green, -1)

                for i in range(len(center_list)):
                    cv2.circle(frame, center_list[i], 12, pink, -1)
        else:
            break

        for i in range(len(center_list)):
            cv2.circle(frame, center_list[i], 10, pink, -1)
        cv2.imshow('', frame)


    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
