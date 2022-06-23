# Copyright (c) OpenMMLab. All rights reserved.
import torch
from mmseg.models.backbones import MobileNetV2

def main():
    src_checkpoint = torch.load('/home/zhijie/codes/SonyAI/pretrained/mocov2_sss_mobilenetv2_f01_05_ks.pth')
    state_dict = src_checkpoint['state_dict']
    model = MobileNetV2()
    new_state_dict = {}
#     pop_keys = []
#     import ipdb;ipdb.set_trace()
#         state_dict.pop(key, None)
    
#     for key in model.state_dict().keys():
#         if key not in state_dict.keys():
#             pop_keys.append(key)
    
    count = 0 
    for (key_src, key_tgt) in zip(state_dict.keys(), model.state_dict().keys()):
        new_state_dict[key_tgt] = state_dict[key_src]
        print('{} -> {}'.format(key_src, key_tgt))

    src_checkpoint['state_dict'] = new_state_dict

    torch.save(src_checkpoint, 'output.pth')

if __name__ == '__main__':
    main()
