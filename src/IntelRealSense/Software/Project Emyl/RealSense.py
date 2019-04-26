# First import the library
import cv2                                # state of the art computer vision algorithms library
import numpy as np                        # fundamental package for scientific computing
import matplotlib.pyplot as plt           # 2D plotting library producing publication quality figures
import pyrealsense2 as rs                 # Intel RealSense cross-platform open-source API
import math

# install cv2 and numpy : pip install opencv-pyhton
# install matplotlib : python -m pip install -U matplotlib

try:
    # Create a context object. This object owns the handles to all connected realsense devices
    pipeline = rs.pipeline()
    pipeline.start()
    profile = pipeline.get_active_profile()

    while True:
        # This call waits until a new coherent set of frames is available on a device
        # Calls to get_frame_data(...) and get_frame_timestamp(...) on a device will return stable values until wait_for_frames(...) is called
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue
        
        color = np.asanyarray(color_frame.get_data())
        plt.rcParams["axes.grid"] = False
        plt.rcParams['figure.figsize'] = [12, 6]
        #plt.rcParams['figure.figsize'] = [9, 6]     #figure(figsize=(1,1)) would create an inch-by-inch image, which would be 80-by-80 pixels unless you also give a different dpi argument.

        colorizer = rs.colorizer()
        colorized_depth = np.asanyarray(colorizer.colorize(depth_frame).get_data())
        
        # Create alignment primitive with color as its target stream:
        align = rs.align(rs.stream.color)
        frameset = align.process(frames)

        # Update color and depth frames:
        aligned_depth_frame = frameset.get_depth_frame()
        colorized_depth = np.asanyarray(colorizer.colorize(aligned_depth_frame).get_data())

        # Show the two frames together: gewoon en depth naast elkaar
        images = np.hstack((color, colorized_depth))
        
        # Standard OpenCV boilerplate for running the net:
        
        height, width = color.shape[:2]
        expected = 300.0 #spelen met dit om tot de nauwkeurigste meting te gaan. 
        #expected = 720.0 #vermoedlijk is dit gelijk aan de breedte van de frame     
        aspect = width / height
        print(height,expected)
        scale = int(math.ceil(height / expected))

        print(scale)
        resized_image = cv2.resize(color, (int(round(expected * aspect)),int( expected)))
        crop_start = round(expected * (aspect - 1) / 2)
        crop_img = resized_image[0:int(expected), int(crop_start):int(crop_start+expected)]

        net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt", "MobileNetSSD_deploy.caffemodel")
        inScaleFactor = 0.007843
        meanVal       = 127.53
        classNames = ("background", "aeroplane", "bicycle", "bird", "boat",
                    "bottle", "bus", "car", "cat", "chair",
                    "cow", "diningtable", "dog", "horse",
                    "motorbike", "person", "pottedplant",
                    "sheep", "sofa", "train", "tvmonitor")

        blob = cv2.dnn.blobFromImage(crop_img, inScaleFactor, (int(expected), int(expected)), meanVal, False)
        net.setInput(blob, "data")
        detections = net.forward("detection_out")
        print(detections)
        length = int(detections.size / 7)

        for x in range(length):

            label = detections[0,0,x,1]
            conf  = detections[0,0,x,2]
            xmin  = detections[0,0,x,3]
            ymin  = detections[0,0,x,4]
            xmax  = detections[0,0,x,5]
            ymax  = detections[0,0,x,6]

            className = classNames[int(label)]
            xmin_depth = int((xmin * expected + crop_start) * scale)
            ymin_depth = int((ymin * expected) * scale)
            xmax_depth = int((xmax * expected + crop_start) * scale)
            ymax_depth = int((ymax * expected) * scale)
            xmin_depth,ymin_depth,xmax_depth,ymax_depth

            

            cv2.rectangle(crop_img, (int(xmin * expected), int(ymin * expected)), 
                        (int(xmax * expected), int(ymax * expected)), (255, 255, 255), 2)
            cv2.putText(crop_img, className, 
                        (int(xmin * expected), int(ymin * expected) - 5),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
            depth = np.asanyarray(aligned_depth_frame.get_data())
            # Crop depth data:
            depth = depth[xmin_depth:xmax_depth,ymin_depth:ymax_depth].astype(float)

            # Get data scale from the device and convert to meters
            depth_scale = profile.get_device().first_depth_sensor().get_depth_scale()
            depth = depth * depth_scale
            dist,_,_,_ = cv2.mean(depth)
            
            cv2.rectangle(colorized_depth, (xmin_depth, ymin_depth), 
                        (xmax_depth, ymax_depth), (255, 255, 255), 2)

            cv2.putText(colorized_depth, className, 
                        (xmin_depth, ymin_depth - 5),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
            cv2.putText(colorized_depth, str(round(dist,2)), 
                        (xmin_depth, ymin_depth + 20),
                        cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
                        

        
        cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
        #cv2.namedWindow('RealSense', cv2.WINDOW_NORMAL)   #cv2.Window normal -> window scaled mee met volgende lijn
        #cv2.resizeWindow('RealSense', 720,480)     #de 2 getallen geven de resolutie van de window weer (= de maximale camera resolutie)
        
        cv2.imshow('RealSense', crop_img)
        cv2.namedWindow('RealSense2', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('RealSense2',colorized_depth)
        cv2.waitKey(1)



    exit(0)
        
#except rs.error as e:
#    # Method calls agaisnt librealsense objects may throw exceptions of type pylibrs.error
#    print("pylibrs.error was thrown when calling %s(%s):\n", % (e.get_failed_function(), e.get_failed_args()))
#    print("    %s\n", e.what())
#    exit(1)
except Exception as e:
    print(e)
    pass