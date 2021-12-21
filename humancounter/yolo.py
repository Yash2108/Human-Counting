import cv2
import numpy as np
import time
import os


net = cv2.dnn.readNet(os.getcwd()+"/humancounter/yolov3.weights", os.getcwd()+"/humancounter/yolov3.cfg")
classes = []
with open(os.getcwd()+"/humancounter/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

def live_feed(img):
    net = cv2.dnn.readNet(os.getcwd()+"/humancounter/yolov3.weights", os.getcwd()+"/humancounter/yolov3.cfg")
    classes = []
    with open(os.getcwd()+"/humancounter/coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    #instantiate a variable 'p' to keep count of persons
    p=0
    (W, H) = (None, None)
    # img = cv2.imread(image_path)
    if W is None or H is None:
            (H, W) = img.shape[:2]
    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    
    # initialize our lists of detected bounding boxes, confidences, and class IDs, respectively
    boxes = []
    confidences = []
    class_ids = []
    # loop over each of the layer outputs
    for out in outs:
        # loop over each of the detections
        for detection in out:
            # extract the class ID and confidence 
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            # filter out weak predictions
            if confidence > 0.7:
                center_x = int(detection[0] * W)
                center_y = int(detection[1] * H)
                w = int(detection[2] * W)
                h = int(detection[3] * H)
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
    
                # update our list of bounding box coordinates, confidences, and class IDs
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    # apply non-maxima suppression to suppress weak, overlapping bounding boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.2)
    #detecting persons
    text = ""
    if len(indexes) > 0:
        # loop over the indexes we are keeping
        for i in indexes.flatten():
            # extract the bounding box coordinates
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            label = str(classes[class_ids[i]])
            if label == 'person':
                p=p+1
            else:
                continue
            # draw a bounding box rectangle and label on the frame
            color = [int(c) for c in colors[class_ids[i]]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            text = label + ':' + str(p)
            #cv2.putText(img, text, (x, y+30),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
            #print("Length: ",len(boxes))
            print("People :", p)
    cv2.putText(img, text, (10,40),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    # cv2.imshow('image',img)
    # cv2.imwrite(os.getcwd()+"/media/images/output_"+image_path.split('/')[-1],img)
    # if cv2.waitKey(1) & 0xFF==ord('q'):
    #     cv2.destroyAllWindows()
    return img
    # net = cv2.dnn.readNet(os.getcwd()+"/humancounter/yolov3.weights", os.getcwd()+"/humancounter/yolov3.cfg")
    # classes = []
    # with open(os.getcwd()+"/humancounter/coco.names", "r") as f:
    #     classes = [line.strip() for line in f.readlines()]
    # layer_names = net.getLayerNames()
    # output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    # colors = np.random.uniform(0, 255, size=(len(classes), 3))

    # #load input video stream
    # # cap = cv2.VideoCapture(0) 
    # #initialize the writer
    # writer = None
    # (W, H) = (None, None)
    # starting_time = time.time()
    # frame_id = 0
    # while True:
    #     ret , frame= cap.read()
    #     frame_id += 1
    #     #instantiate a variable 'p' to keep count of persons
    #     p = 0 
    #     if W is None or H is None:
    #         (H, W) = frame.shape[:2]
    #     # Detecting objects
    #     blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    #     net.setInput(blob)
    #     outs = net.forward(output_layers)
     
    #     # initialize our lists of detected bounding boxes, confidences, and class IDs, respectively
    #     boxes = []
    #     confidences = []
    #     class_ids = []
    #     # loop over each of the layer outputs
    #     for out in outs:
    #         # loop over each of the detections
    #         for detection in out:
    #             # extract the class ID and confidence 
    #             scores = detection[5:]
    #             class_id = np.argmax(scores)
    #             confidence = scores[class_id]
    #             # filter out weak predictions
    #             if confidence > 0.7:
    #                 center_x = int(detection[0] * W)
    #                 center_y = int(detection[1] * H)
    #                 w = int(detection[2] * W)
    #                 h = int(detection[3] * H)
    #                 # Rectangle coordinates
    #                 x = int(center_x - w / 2)
    #                 y = int(center_y - h / 2)
      
    #                 # update our list of bounding box coordinates, confidences, and class IDs
    #                 boxes.append([x, y, w, h])
    #                 confidences.append(float(confidence))
    #                 class_ids.append(class_id)
    #     # apply non-maxima suppression to suppress weak, overlapping bounding boxes
    #     indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.2)
    #     #detecting persons
    #     if len(indexes) > 0:
    #         # loop over the indexes we are keeping
    #         for i in indexes.flatten():
    #             # extract the bounding box coordinates
    #             (x, y) = (boxes[i][0], boxes[i][1])
    #             (w, h) = (boxes[i][2], boxes[i][3])
    #             label = str(classes[class_ids[i]])
    #             if label == 'person':
    #                 p=p+1
    #             else:
    #                 continue
    #             # draw a bounding box rectangle and label on the frame
    #             color = [int(c) for c in colors[class_ids[i]]]
    #             cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
    #             text = label + ':' + str(p)
    #             #cv2.putText(frame, text, (x, y+30),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    #             print("Length: ",len(boxes))
    #             print("People :", p)
    #         cv2.putText(frame, text, (10,40),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    #         # if writer is None:
    #         #     # initialize our video writer
    #         #     fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    #         #     writer = cv2.VideoWriter("person_out1.mp4", fourcc, 10,(frame.shape[1], frame.shape[0]), True)
    #     elapsed_time = time.time() - starting_time
    #     fps = frame_id / elapsed_time
    #     print(str(round(fps, 2)))
    #     jpeg = cv2.imencode('.jpg', frame)[1]
    #     print("Jpeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeg: ",jpeg)
    #     yield(b'--frame\r\n'
    #           b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
    #     # cv2.imshow("Frame", frame)
    #     # writer.write(frame)
    #     # if cv2.waitKey(1) & 0xFF==ord('q'):
    #     #     cap.release()
    #     #     writer.release()
    #     #     break
    # # cv2.destroyAllWindows()

def video_feed(video_path):
    net = cv2.dnn.readNet(os.getcwd()+"/humancounter/yolov3.weights", os.getcwd()+"/humancounter/yolov3.cfg")
    classes = []
    with open(os.getcwd()+"/humancounter/coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    #load input video stream
    cap = cv2.VideoCapture(video_path) 
    #initialize the writer
    writer = None
    (W, H) = (None, None)
    starting_time = time.time()
    frame_id = 0
    while True:
        ret , frame= cap.read()
        frame_id += 1
        if(ret != True):
            cap.release()
            writer.release()
            break
        #instantiate a variable 'p' to keep count of persons
        p = 0 
        if W is None or H is None:
            (H, W) = frame.shape[:2]
        # Detecting objects

        blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)
     
        # initialize our lists of detected bounding boxes, confidences, and class IDs, respectively
        boxes = []
        confidences = []
        class_ids = []
        # loop over each of the layer outputs
        for out in outs:
            # loop over each of the detections
            for detection in out:
                # extract the class ID and confidence 
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                # filter out weak predictions
                if confidence > 0.7:
                    center_x = int(detection[0] * W)
                    center_y = int(detection[1] * H)
                    w = int(detection[2] * W)
                    h = int(detection[3] * H)
                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
      
                    # update our list of bounding box coordinates, confidences, and class IDs
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        # apply non-maxima suppression to suppress weak, overlapping bounding boxes
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.2)
        #detecting persons
        if len(indexes) > 0:
            # loop over the indexes we are keeping
            for i in indexes.flatten():
                # extract the bounding box coordinates
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])
                label = str(classes[class_ids[i]])
                if label == 'person':
                    p=p+1
                else:
                    continue
                # draw a bounding box rectangle and label on the frame
                color = [int(c) for c in colors[class_ids[i]]]
                cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                text = label + ':' + str(p)
                #cv2.putText(frame, text, (x, y+30),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
                #print("Length: ",len(boxes))
                print("People :", p)
            cv2.putText(frame, text, (10,40),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)    
            if writer is None:
                # initialize our video writer
                fourcc = cv2.VideoWriter_fourcc('V','P','8','0')
                writer = cv2.VideoWriter(os.getcwd()+"/media/video/output_"+video_path.split('/')[-1].split(".")[0]+".webm", fourcc, 10,(frame.shape[1], frame.shape[0]), True)
        elapsed_time = time.time() - starting_time
        fps = frame_id / elapsed_time
        print(str(round(fps, 2)))
        # cv2.imshow("Frame", frame)
        writer.write(frame)
        # if cv2.waitKey(1) & 0xFF==ord('q'):
        #     cap.release()
        #     writer.release()
        #     break
    cv2.destroyAllWindows()
    return "/media/video/output_"+video_path.split('/')[-1].split(".")[0]+".webm"


def image_feed(image_path):
    net = cv2.dnn.readNet(os.getcwd()+"/humancounter/yolov3.weights", os.getcwd()+"/humancounter/yolov3.cfg")
    classes = []
    with open(os.getcwd()+"/humancounter/coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    #instantiate a variable 'p' to keep count of persons
    p=0
    (W, H) = (None, None)
    img = cv2.imread(image_path)
    if W is None or H is None:
            (H, W) = img.shape[:2]
    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    
    # initialize our lists of detected bounding boxes, confidences, and class IDs, respectively
    boxes = []
    confidences = []
    class_ids = []
    # loop over each of the layer outputs
    for out in outs:
        # loop over each of the detections
        for detection in out:
            # extract the class ID and confidence 
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            # filter out weak predictions
            if confidence > 0.7:
                center_x = int(detection[0] * W)
                center_y = int(detection[1] * H)
                w = int(detection[2] * W)
                h = int(detection[3] * H)
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
    
                # update our list of bounding box coordinates, confidences, and class IDs
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    # apply non-maxima suppression to suppress weak, overlapping bounding boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.2)
    #detecting persons
    if len(indexes) > 0:
        # loop over the indexes we are keeping
        for i in indexes.flatten():
            # extract the bounding box coordinates
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            label = str(classes[class_ids[i]])
            if label == 'person':
                p=p+1
            else:
                continue
            # draw a bounding box rectangle and label on the frame
            color = [int(c) for c in colors[class_ids[i]]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            text = label + ':' + str(p)
            #cv2.putText(img, text, (x, y+30),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
            #print("Length: ",len(boxes))
            print("People :", p)
    cv2.putText(img, text, (10,40),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    # cv2.imshow('image',img)
    cv2.imwrite(os.getcwd()+"/media/images/output_"+image_path.split('/')[-1],img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        cv2.destroyAllWindows()
    return "/media/images/output_"+image_path.split('/')[-1]

# image_feed("upload_test.jpg")