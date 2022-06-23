_base_ = './pascal_voc12.py'
# dataset settings
data = dict(
    train=dict(
        ann_dir=['SegmentationClassAug'],
        split=[
            'ImageSets/Segmentation/aug_0.7.txt'
        ]))
