import cv2
print(cv2.__version__)
vidcap = cv2.VideoCapture('1.mp4')
success,image = vidcap.read()
count = 0
while success:
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # (thresh, image) = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY)
    cv2.imwrite("gray_cash/gray%d.jpg" % count, image)     # save frame as JPEG file
    success, image = vidcap.read(count)
    print ('Read a new frame: ', success)
    count += 1
print ('Example for Git, commit 2')
