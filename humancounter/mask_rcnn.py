# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 10:05:37 2021

@author: sachit
"""

import pixellib
from pixellib.instance import instance_segmentation
import cv2

def count_in_image(loc_image):
    segment_image = instance_segmentation()
    segment_image.load_model("/human_counter/mask_rcnn_coco.h5")
    target_classes = segment_image.select_target_classes(person=True)
    segment_image.segmentImage(loc_image, segment_target_classes=target_classes, extract_segmented_objects=True,
    save_extracted_objects=True, show_bboxes=True,  output_image_name="media/images/output_"+loc_image.split('/')[-1])
    return "/media/images/output_"+loc_image.split('/')[-1]

def count_in_video(loc_video):
    segment_video = instance_segmentation()
    segment_video.load_model("/human_counter/mask_rcnn_coco.h5")
    target_classes = segment_video.select_target_classes(person=True)
    segment_video.process_video("/content/drive/MyDrive/Colab Notebooks/peeps.jpg", segment_target_classes=target_classes, extract_segmented_objects=True,
    save_extracted_objects=True, show_bboxes=True,  frames_per_second= 5,  output_video_name="media/videos/output_"+loc_video.split('/')[-1])
    return "/media/videos/output_"+loc_video.split('/')[-1]

def count_in_feed():
    capture = cv2.VideoCapture(0)
    segment_camera = instance_segmentation()
    segment_camera.load_model("/human_counter/mask_rcnn_coco.h5")
    target_classes = segment_camera.select_target_classes(person=True)
    seg, out = segment_camera.process_camera(capture, show_bboxes=True, show_frames=True, segment_target_classes=target_classes,
    extract_segmented_objects=True, save_extracted_objects=True,frame_name="frame", frames_per_second=5, output_video_name="media/videos/output_feed.mp4")
    return "/media/videos/output_feed.mp4"