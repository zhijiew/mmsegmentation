export yagi=14
export pcts=(0.1)

for((i=0;i<${#pcts[@]};i++)) do

    pct=${pcts[i]}
    config=sss_seg_${pct}_random

    qsub -N S${pct} \
         -o /home/zhijie/logs/SonyAI/${config}.log \
         -q main.q@yagi${yagi}.vision.is.tohoku \
         -v config=$config \
         train_sss.sh

done;
