import pixellib
from pixellib.torchbackend.instance import instanceSegmentation
import os

def count_in_image(loc_image):
    ins = instanceSegmentation()
    ins.load_model(os.getcwd()+"/traincrud/pointrend_resnet101.pkl", network_backbone="resnet101")
    target_classes = ins.select_target_classes(person = True)
    ins.segmentImage(loc_image, segment_target_classes = target_classes, show_bboxes=True, output_image_name="media/images/output_"+loc_image.split('/')[-1])
    return "/media/images/output_"+loc_image.split('/')[-1]