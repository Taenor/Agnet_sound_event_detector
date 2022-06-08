#!/bin/bash
rm -r list_test.txt 

folders=$( bash <<EOF
ls ./foreground
ls ./background
EOF
)

echo $folders

counter=1
arr=("$@") #(12.36 4.02 0.62 2.05 4.02 0.67 4.02 0.12 4.02 4.18 4.33 0.78 2.33 2.12 4.47 0.53 41.02 4.06 0.13 0.13 4.02)  
tot="${arr[0]}"
for a in $folders;
do
        i="${arr[counter]}"
        j=$(expr $tot*$i/100 | bc)
        echo $a
        echo $j
        if [[ $a == gun_shot || $a == door_slamming || $a == fireworks || $a == clapping || $a == glass_breaking || $a == microphone_tap || $a == snapping ]]
        then
          find ./ -path "./foreground/$a/*.wav" | shuf -n $j > ./listes/list_$a.txt
          find ./ -path "./foreground/$a/*.wav" | shuf -n $j >> ./list_test.txt
        else
          find ./ -path "./background/$a/*.wav" | shuf -n $j > ./listes/list_$a.txt
          find ./ -path "./background/$a/*.wav" | shuf -n $j >> ./list_test.txt
        fi
        let counter++
done
