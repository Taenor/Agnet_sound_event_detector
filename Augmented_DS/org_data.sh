#!/bin/bash

fr=$( bash <<EOF
find ./original/ -name "gun_shot.*.wav"
EOF
)
#echo $fr
#echo "hello"
rm -r ./foreground
mkdir -p ./foreground/gun_shot
for i in $fr
do 
   #echo $i
   #tag="gun_shot."
   #name=$(basename $i)
   #echo $name
   #sox $i -r 16000 ./Wav/$name
   cp $i ./foreground/gun_shot
done 

bck=$( bash <<EOF
find ./original/ ! -name "gun_shot.*.wav"
EOF
)
#echo $bck
rm -r ./background
mkdir ./background
#echo "hello"
for i in $bck
do 
   #echo $i
   name=$(basename $i)
   step=${name%.*}
   tag=${step%.*}
   #echo $tag
   #sox $i -r 16000 ./Wav/$name
   mkdir -p ./background/$tag && cp $i ./background/$tag
done 
