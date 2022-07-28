fr=$( bash <<EOF
#find ./background/ -name "*.wav"
#find ./foreground/ -name "*.wav"
cat list.txt
find ./bruit/ -name "*.wav"
find ./SNR/ -name "*.wav"
# find ./lower_vol/ -name "*.wav"
# find ./shift_pitch/ -name "*.wav"
# find ./time_shift/ -name "*.wav"
# find ./shift_time/ -name "*.wav"
EOF
)
echo $fr

rm -r ./augmentedDS
mkdir ./augmentedDS

for i in $fr
do 
   cp $i ./augmentedDS
done
