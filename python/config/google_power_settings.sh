#!/bin/bash
stop powerd
stop powerm
stop update-engine
stop bluetoothd
echo 375 > /sys/class/backlight/intel_backlight/brightness 
#backlight_tool --set_brightness_percent 40.0
backlight_tool --get_brightness_percent

#!/bin/bash
D3COLD_ALLOWED=1  # 0 or 1
CONTROL=auto    # auto or on

# enabel SATA PM
for i in /sys/class/scsi_host/host?/link_power_management_policy; do
  echo min_power > $i
done

# enable audio PM
echo 1 > /sys/module/snd_hda_intel/parameters/power_save 

# modify d3cold for PCI devices
for i in /sys/devices/pci*/00*; do cat $i/d3cold_allowed; done
for i in /sys/devices/pci*/00*; do echo $D3COLD_ALLOWED > $i/d3cold_allowed;
done

# enable runtime_pm for _all_ devices
all_devs=`find /sys/devices/ | grep "power/control"`

for i in $all_devs; do echo $CONTROL > $i; done

iw dev wlan0 set power_save on


echo done  
