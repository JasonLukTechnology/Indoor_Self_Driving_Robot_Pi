# Detect a logo with certain color.


def shape_detecter(image):
    # Read the picture
    image = cv2.imread(image)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Setup target color ranges and creat a mask to highlight the traget color
    # This is the range for green object
    lower = np.array([28, 10, 10])
    upper = np.array([50, 230, 230])
    shapeMask = cv2.inRange(hsv, lower, upper)
    # Fing contour in the color mask
    cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    # print(cnts)
    # print("I found {} shapes".format(len(cnts)))
    cv2.imwrite("Mask.png", shapeMask)
    cv2.imshow("Mask", shapeMask)
    # Loop all the contour result
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        # Find the object with four contour (left some error margen)
        if len(approx) >= 4 and len(approx) <= 7:
            #Get the shapes x and y center positon and their hight and width
            (x, y, w, h) = cv2.boundingRect(approx) 
            print(w,h)
            # Make sure the shape is correct
            if w > 25 and w < 500 and w > h and h > 15 and h < 500:
                ratio = w / h
                print(w, y, w, h)
                print(ratio)
                mx = x + (w / 2)
                my = y + (h / 2)
                # print("ratio:{}".format(ratio))
                # print("location:{},{}".format(mx,my))
                # print(w,h)
                # draw the contour and show it
                cv2.polylines(image, [approx], True, (0, 255, 0), 2)
                cv2.drawContours(image, [c], -1, (0, 255, 0), 1)
                cv2.rectangle(image, (950,790), (970,798), (110, 250, 0))
                cv2.imwrite("shape1.png", image)
                cv2.imshow("Image", image)
                cv2.waitKey(0)
                return (mx, my, ratio, w, h)
    return None
