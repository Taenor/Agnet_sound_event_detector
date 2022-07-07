data=$( bash <<EOF
find $1 -name "*.wav"
EOF
)
rm -r ./bruit
mkdir ./bruit
for i in $data
do 
   echo $i
   sox $i -r 22050 -b 16 -c 1 ./bruit/$(basename $i)
done
