file=$1
while read line
do
	mkdir $line
	mv $line'_'* $line
done <$file
