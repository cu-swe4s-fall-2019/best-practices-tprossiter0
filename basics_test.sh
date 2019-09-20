test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

#hw 2

(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

run test_no_stderr python3 get_column_stats.py --input_filename data.txt --column_number 2
assert_no_stderr

V=1
(for i in `seq 0 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

run test_correct_stdout python3 get_column_stats.py --input_filename data.txt --column_number 2
assert_stdout
assert_exit_code 0


#testing that we catch exceptions for wrong filename
run test_stderr_filename python3 get_column_stats.py --input_filename not_data.txt --column_number 2
assert_no_stderr
assert_exit_code 1


run test_correct_stdout python3 get_column_stats.py --input_filename data.txt --column_number 2
assert_exit_code 0

#for randoms

(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

run test_correct_stdout python3 get_column_stats.py --input_filename data.txt --column_number 2
assert_stdout
assert_exit_code 0


#testing that we catch exceptions for wrong filename
run test_stderr_filename python3 get_column_stats.py --input_filename not_data.txt --column_number 2
assert_no_stderr
assert_exit_code 1


run test_correct_stdout python3 get_column_stats.py --input_filename data.txt --column_number 2
assert_exit_code 0



#hw1

pycodestyle style.py

pycodestyle get_column_stats.py

(for i in `seq 1 100`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

python get_column_stats.py --input_filename data.txt --column_number 2


V=1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

python get_column_stats.py --input_filename data.txt --column_number 2

V=0
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

python get_column_stats.py --input_filename data.txt --column_number 2

V=-1
(for i in `seq 1 100`; do 
    echo -e "$V\t$V\t$V\t$V\t$V";
done )> data.txt

python get_column_stats.py --input_filename data.txt --column_number 2