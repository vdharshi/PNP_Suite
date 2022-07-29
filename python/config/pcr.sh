#!/bin/bash
. /home/OSPM-Test-Suite/global_variables.sh
echo "---------------------------------------------"
echo "Package C states Residency calculation script"
echo "---------------------------------------------"
rm /$(pwd)/pcr_log.txt
touch /$(pwd)/pcr_log.txt
log_file=/$(pwd)/pcr_log.txt
now=$(date +"%T")
echo "----------------------------------------------" >>$log_file
echo "Package C state Residency Summary (in %)" >>$log_file
echo "----------------------------------------------" >>$log_file
echo "----------------------------------------------" >>$log_file
echo "Start time: "$now >>$log_file
overall_time=$1
declare -a msr_pc1='()'
declare -a msr_pc2='()'

set_governor() {
	mount -o remount,exec /home/
	for((i=0;i<$max_no_of_cores;i++))
	do
		echo "performance" > /sys/devices/system/cpu/cpu$i/cpufreq/scaling_governor
	done
}

tick1() {
	i=1
	if [[ $board_name = "octopus" || $board_name = "glkrvp" ]]
	then
	 for ((i = 1; i <= 10; i++))
                do
                msr_pc1[1]=
                msr_pc1[2]=
                msr_pc1[3]=
                msr_pc1[4]=
                msr_pc1[5]=
                msr_pc1[6]=`./msr/rdmsr 0x60b -X`
                msr_pc1[7]=`./msr/rdmsr 0x60c -X`
                msr_pc1[8]=`./msr/rdmsr 0x633 -X`
                msr_pc1[9]=`./msr/rdmsr 0x634 -X`
                msr_pc1[10]=`./msr/rdmsr 0x635 -X`
                tick1_time=$(date +"%T")
                t="$(date +%s%3N)"
                tsc1[i]=${msr_pc1[i]}
                done
	elif [[ $board_name = "nami" || $board_name = "soraka" || $board_name = "sarien" || $board_name = "kblrvp" || $board_name = "nocturne" || $board_name = "hatch" ]]
	then
		for ((i = 1; i <= 10; i++))
	   	do
		msr_pc1[1]=
		msr_pc1[2]=`./msr/rdmsr 0x60d -X`
		msr_pc1[3]=`./msr/rdmsr 0x3f8 -X`
		msr_pc1[4]=
		msr_pc1[5]=
		msr_pc1[6]=`./msr/rdmsr 0x3f9 -X`
		msr_pc1[7]=`./msr/rdmsr 0x3fa -X`
		msr_pc1[8]=`./msr/rdmsr 0x630 -X`
		msr_pc1[9]=`./msr/rdmsr 0x631 -X`
		msr_pc1[10]=`./msr/rdmsr 0x632 -X`
		tick1_time=$(date +"%T")
		t="$(date +%s%3N)"
		tsc1[i]=${msr_pc1[i]}
		done
    elif [[ $board_name = "blackwall" ]]
     then
         for ((i = 1; i <= 10; i++))
         do
         msr_pc1[1]=
         msr_pc1[2]=`./msr/rdmsr 0x60d -X`
         msr_pc1[3]=
         msr_pc1[4]=
         msr_pc1[5]=
         msr_pc1[6]=
         msr_pc1[7]=
         msr_pc1[8]=`./msr/rdmsr 0x630 -X`
         msr_pc1[9]=`./msr/rdmsr 0x631 -X`
         msr_pc1[10]=`./msr/rdmsr 0x632 -X`
         tick1_time=$(date +"%T")
         t="$(date +%s%3N)"
         tsc1[i]=${msr_pc1[i]}
         done
	fi
}

tick2() {
	j=1
        if [[ $board_name = "octopus" || $board_name = "glkrvp" ]]
        then
         for ((j = 1; j <= 10; j++))
                do
                msr_pc2[1]=
                msr_pc2[2]=
                msr_pc2[3]=
                msr_pc2[4]=
                msr_pc2[5]=
                msr_pc2[6]=`./msr/rdmsr 0x60b -X`
                msr_pc2[7]=`./msr/rdmsr 0x60c -X`
                msr_pc2[8]=`./msr/rdmsr 0x633 -X`
                msr_pc2[9]=`./msr/rdmsr 0x634 -X`
                msr_pc2[10]=`./msr/rdmsr 0x635 -X`
                tick2_time=$(date +"%T")
                p="$(date +%s%3N)"
                tsc2[j]=${msr_pc2[j]}
                done
        elif [[ $board_name = "nami" || $board_name = "soraka" || $board_name = "sarien" || $board_name = "kblrvp" || $board_name = "hatch" ]]
        then
                for ((j = 1; j <= 10; j++))
                do
                msr_pc2[1]=
                msr_pc2[2]=`./msr/rdmsr 0x60d -X`
                msr_pc2[3]=`./msr/rdmsr 0x3f8 -X`
                msr_pc2[4]=
                msr_pc2[5]=
                msr_pc2[6]=`./msr/rdmsr 0x3f9 -X`
                msr_pc2[7]=`./msr/rdmsr 0x3fa -X`
                msr_pc2[8]=`./msr/rdmsr 0x630 -X`
                msr_pc2[9]=`./msr/rdmsr 0x631 -X`
                msr_pc2[10]=`./msr/rdmsr 0x632 -X`
                tick2_time=$(date +"%T")
                p="$(date +%s%3N)"
                tsc2[j]=${msr_pc2[j]}
                done
        elif [[ $board_name = "blackwall" ]]
        then
                for ((i = 1; i <= 10; i++))
                do
                msr_pc2[1]=
                msr_pc2[2]=`./msr/rdmsr 0x60d -X`
                msr_pc2[3]=
                msr_pc2[4]=
                msr_pc2[5]=
                msr_pc2[6]=
                msr_pc2[7]=
                msr_pc2[8]=`./msr/rdmsr 0x630 -X`
                msr_pc2[9]=`./msr/rdmsr 0x631 -X`
                msr_pc2[10]=`./msr/rdmsr 0x632 -X`
                tick2_time=$(date +"%T")
                p="$(date +%s%3N)"
                tsc2[i]=${msr_pc2[i]}
          done
        fi
}
pcr_calc() {
	total_residency=100
	tsc_freq=`cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq`
	run_time=$(awk -v p=$p -v t=$t 'BEGIN{ print ((p - t) / 1000)}')
	for ((k = 1; k <= 10; k++))
	do
		x=$(( ($((16#${tsc2[k]})) - $((16#${tsc1[k]})))))
		y=$(awk -v a=$run_time -v b=$tsc_freq 'BEGIN{ print (a * b * 10)}')
		pc[k]=$(awk -v x=$x -v y=$y 'BEGIN{ print (x / y)}')
#		pc[k]=$(bc <<< "scale = 10; ($x / $y)") #This command works with Linux. For chrome need to use "awk"
	done
	sum=$(awk 'BEGIN {t=0; for (i in ARGV) t+=ARGV[i]; print t}' "${pc[@]}")
	pc[0]=$(awk -v x=$total_residency -v y=$sum 'BEGIN{ print (x - y)}')
	echo "PC0 = "${pc[0]} >>$log_file
	j=1
	for ((k = 1; k <= 10; k++))
	do
		echo "PC$k = "${pc[k]} >>$log_file
	done
}
pc_residency() {
	echo " Started capturing data ..... "
	set_governor
	tick1
	sleep $overall_time
	tick2
	end_time=$(date +"%T")
	echo "End time:" $end_time >>$log_file
	echo "----------------------------------------------" >>$log_file
	pcr_calc
	echo "----------------------------------------------" >>$log_file
	echo "Total captured time:"$run_time >>$log_file
	echo "----------------------------------------------" >>$log_file
	echo " Completed successfully"
}
pc_residency
