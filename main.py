import cv2

# openCV DNN
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320,320),scale=1/255)

# load class
classes=[]
with open("dnn_model/classes.txt","r")as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)

print("object list")
print(classes)

# initialize camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1200)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
# FULL HD 1920x 1880

def click_button(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


# craeate a window
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",click_button)

while True:
    # Get frames
    ret, frame = cap.read()
    # object detection
    (class_ids,scores,bboxes) = model.detect(frame)
    for class_id, score, bbox in zip(class_ids,scores,bboxes):
        (x, y, w, h) = bbox
        class_name = classes[class_id]

        cv2.putText(frame,class_name,(x,y-10),cv2.FONT_HERSHEY_PLAIN, 2,(288,8,58),2)
        cv2.rectangle(frame, (x, y), (x+w, y+h),(200, 0, 50), 3)

    # create a button
    # cv2.rectangle(frame,(20,20),(220,70),(0,0,200), -1)  # 20x20 frame size #20
    # cv2.putText(frame,"persion",(30,60),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)
    # cv2.putText(frame,"Phone",)

    print("class ids",class_ids)
    print("score", scores)
    print("bboxes", bboxes)


    cv2.imshow("Frame", frame)

    cv2.waitKey(1)
