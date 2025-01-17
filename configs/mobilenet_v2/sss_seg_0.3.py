_base_ = '../fcn/fcn_r101-d8_512x1024_80k_cityscapes.py'
model = dict(
    pretrained='/home/zhijie/codes/SonyAI/pretrained/mocov2_sss_mobilenetv2_f01_05_ks_mmseg.pth',
    backbone=dict(
        _delete_=True,
        type='MobileNetV2',
        widen_factor=1.,
        strides=(1, 2, 2, 1, 1, 1, 1),
        dilations=(1, 1, 1, 2, 2, 4, 4),
        out_indices=(1, 2, 4, 6)),
    decode_head=dict(in_channels=320, num_classes=5, num_convs=2, concat_input=False),
    auxiliary_head=dict(in_channels=96, num_classes=5, num_convs=2, concat_input=False))

img_norm_cfg = dict(mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(960, 540),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=False),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img', 'filename', 'gt_semantic_seg']),
        ])
]

dataset_type = 'CustomDataset'
data_root = '/home/zhijie/datasets/SonyAI/kaggle_seg/0.3'
data = dict(
    train=dict(
        type='CustomDataset',
        data_root=data_root,
        img_dir='img/train',
        ann_dir='ann/train',),
    val=dict(
        pipeline=test_pipeline,
        type='CustomDataset',
        data_root=data_root,
        img_dir='img/val',
        ann_dir='ann/val',),
    test=dict(
        pipeline=test_pipeline,
        type='CustomDataset',
        data_root=data_root,
        img_dir='img/val',
        ann_dir='ann/val',)
)
runner = dict(type='IterBasedRunner', max_iters=12000)
checkpoint_config = dict(by_epoch=False, interval=2000)
evaluation = dict(interval=2000, metric='mIoU', pre_eval=True)
