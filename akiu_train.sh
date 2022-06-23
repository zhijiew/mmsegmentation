sbatch <<EOT
#!/bin/bash
#SBATCH --job-name="S"$2"R"
###########RESOURCES###########
#SBATCH --nodelist="yagi"$3""
#SBATCH --partition=11-8
#SBATCH --gres=gpu:4
#SBATCH --mem=32G
#SBATCH --cpus-per-task=16
###############################
#SBATCH --output=/home/zhijie/logs/SonyAI/sss_seg_"$2".out
#SBATCH --error=/home/zhijie/logs/SonyAI/sss_seg_"$2".err
#SBATCH -v

module load cuda/11.3
source ~/.opt/miniconda/etc/profile.d/conda.sh

PORT="$1" bash tools/dist_train.sh configs/mobilenet_v2/sss_seg_"$2".py 4 --work-dir work_dirs/sss_seg_"$2"

EOT
