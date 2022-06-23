#!/bin/bash

#export yagis=(18 19 20 21)
#export ports=(25004 25005 25006 25007 25008 25009 25010 25011)
export yagis=(20 21)
export ports=(25008 25009 25010 25011)

export pcts=(0.5 0.7) # lambda adv

count=0
flag=0
yagi=20

for((i=0;i<${#pcts[@]};i++)) do

    export pct=${pcts[i]}
    export port=${ports[i]}
    config=sss_seg_${pct}

    bash akiu_train.sh $port $pct $yagi
    echo submitted $pct to $yagi port $port

    ((count++))
    if [ $(( $count % 2 )) = 0 ]
    then
        ((flag++))
        yagi=${yagis[flag]}
    fi

done;

echo submitted $count tasks
