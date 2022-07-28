data=$( bash <<EOF
find $1 -name "*.wav"
find $2 -name "*.wav"
find $3 -name "*.wav"
find $4 -name "*.wav"
EOF
)
rm -r ./SNR
mkdir ./SNR
for i in $data
do 
   echo $i
   sox $i -r 22050 -b 16 -c 1 ./SNR/$(basename $i)
done
