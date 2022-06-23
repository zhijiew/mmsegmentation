#!/usr/bin/env sh
#$-pe gpu 4
#$-l gpu=4
#$-j y
#$-cwd
#$-V

export CUDA_VISIBLE_DEVICES=$SGE_GPU
bash tools/dist_train.sh configs/fcn/${config}.py 4 --work-dir work_dirs/${config}_vocpxhere_pretrain/
