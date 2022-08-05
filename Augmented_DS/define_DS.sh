#!/bin/bash
rm -r list.txt 

folders=$( bash <<EOF
ls ./foreground
ls ./background
EOF
)

echo $folders

counter=1
arr=("$@") #(0.67 0.12 4.33 2.33 12.36 0.53 0.13 4.02 0.62 2.05 4.02 4.02 4.02 4.18 0.78 2.12 4.47 41.02 4.06 0.13 4.02)  
tot="${arr[0]}"
for a in $folders;
do
        i="${arr[counter]}"
        j=$(expr $tot*$i/100 | bc)
        echo $a
        echo $j
        if [[ $a == gun_shot || $a == door_slamming || $a == fireworks || $a == clapping || $a == glass_breaking || $a == microphone_tap || $a == snapping || $a == car_horn || $a == crash || $a == dog_bark || $a == pothole || $a == scream || $a == tire ]]
        then
          find ./ -path "./foreground/$a/*.wav" | shuf -n $j > ./listes/list_$a.txt
          find ./ -path "./foreground/$a/*.wav" | shuf -n $j >> ./list.txt
        else
          find ./ -path "./background/$a/*.wav" | shuf -n $j > ./listes/list_$a.txt
          find ./ -path "./background/$a/*.wav" | shuf -n $j >> ./list.txt
        fi
        let counter++
done
