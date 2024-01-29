import random
import cv2

i = random.randrange(1, 14)

def main():

    color03 = cv2.imread("C:/Users/User/Desktop/로아콘/응애모코코콘/03.png", cv2.IMREAD_COLOR)
    color08 = cv2.imread("C:/Users/User/Desktop/로아콘/응애모코코콘/08.png", cv2.IMREAD_COLOR)
    color29 = cv2.imread("C:/Users/User/Desktop/로아콘/응애모코코콘/29.png", cv2.IMREAD_COLOR)
    color05 = cv2.imread("C:/Users/User/Desktop/로아콘/응애모코코콘/05.png", cv2.IMREAD_COLOR)
    color14 = cv2.imread("C:/Users/User/Desktop/로아콘/응애모코코콘/14.png", cv2.IMREAD_COLOR)
    color38 = cv2.imread("C:/Users/User/Desktop/로아콘/응애모코코콘/38.png", cv2.IMREAD_COLOR)
    color09 = cv2.imread("C:/Users/User/Desktop/로아콘/응애모코코콘/09.png", cv2.IMREAD_COLOR)

    if i == 1:
        print("대길")
        cv2.imshow("C:/Users/User/Desktop/로아콘/응애모코코콘/03.png", color03)
        print(color03.shape)
        print(color03[320,320])

    elif i <= 3:
        print("길")
        cv2.imshow("C:/Users/User/Desktop/로아콘/응애모코코콘/08.png", color08)
        print(color08.shape)
        print(color08[320,320])

    elif i <= 5:
        print("중길")
        cv2.imshow("C:/Users/User/Desktop/로아콘/응애모코코콘/29.png", color29)
        print(color29.shape)
        print(color29[320,320])

    elif i <= 8:
        print("소길")
        cv2.imshow("C:/Users/User/Desktop/로아콘/응애모코코콘/05.png", color05)
        print(color05.shape)
        print(color05[320,320])

    elif i <= 10:
        print("말길")
        cv2.imshow("C:/Users/User/Desktop/로아콘/응애모코코콘/14.png", color14)
        print(color14.shape)
        print(color14[320,320])

    elif i <= 12:
        print("흉")
        cv2.imshow("C:/Users/User/Desktop/로아콘/응애모코코콘/38.png", color38)
        print(color38.shape)
        print(color38[320,320])

    else:
        print("대흉")
        cv2.imshow("C:/Users/User/Desktop/로아콘/응애모코코콘/09.png", color09)
        print(color09.shape)
        print(color09[320,320])

    if __name__ == "__main__":
        main()