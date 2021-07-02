import numpy as np
import cv2

lower_green = np.array([30, 75, 141])
upper_green = np.array([90, 255, 255])
# yellow_green = (104, 239, 217)#np.array([104, 239, 217])

lower_red = np.array([0,125,0])
upper_red = np.array([17,224,146])

lower_blue = np.array([105,135,80])
upper_blue = np.array([119,224,231])
pink = (97, 12, 254)

def contours(img, lower, upper):
    """
    :param img:
    :return:
    """
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_img, lower, upper)
    color = cv2.bitwise_and(img, img, mask=mask)

    kernel = np.ones((5, 5), dtype=np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=2)
    dilation = cv2.dilate(erosion, kernel, iterations=6)
    # dilation = cv2.dilate(edges, kernel, iterations=2)
    # erosion = cv2.erode(dilation, kernel, iterations=2)

    copy_image = np.copy(color)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(copy_image, contours, -1, (255, 0, 0), 3)

    return copy_image, contours
    pass

def choose_center(center_list, con):
    #print(len(con))
    # m = 0
    # tmp = []
    # for i in con:
    #     if len(i) > m:
    #         m = len(i)
    #         tmp = i
    # if m == 0:
    #     return []
    #
    # avg = [0, 0]
    # for i in tmp:
    #     avg[0]+=i[0][0]
    #     avg[1]+=i[0][1]
    # if m != 0:
    #     avg[0]//=m
    #     avg[1]//=m
    #
    # return avg
    for i in range(len(con)):
        avg = [0,0]
        for j in range(len(con[i])):
            avg[0]+=con[i][j][0][0]
            avg[1]+=con[i][j][0][1]
        avg[0]//=len(con[i])
        avg[1]//=len(con[i])
        center_list.append(avg)
    return center_list
    pass

def main(t):
    center_list = []
    c = 0 # check cho phép vẽ

    vid = cv2.VideoCapture(t)

    while True:
        ret, frame = vid.read()
        frame = cv2.flip(frame, 1)

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
                img, con = contours(frame, lower_blue, upper_blue)
                #  cv2.imshow("frame", frame)
                center_list = choose_center(center_list, con)

                # if len(center) > 0:
                #     center_list.append(center)
                #     # array = cv2.circle(array, center, 10, yellow_green, -1)

                # for i in range(len(center_list)):
                #     cv2.circle(frame, center_list[i], 12, pink, -1)
        else:
            break

        for i in range(len(center_list)):
            cv2.circle(frame, center_list[i], 12, pink, -1)
        cv2.imshow('', frame)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(1)
