#!/bin/bash

#!/bin/bash
LOG="/home/law/smart-finance-hub/logs/server.log"
mkdir -p /home/law/smart-finance-hub/logs

# CPU - read directly from /proc/stat (reliable on all Linux)
CPU=$(awk '/^cpu / {idle=$5; total=$2+$3+$4+$5+$6+$7+$8; usage=100*(total-idle)/total; printf "%.1f", usage}' /proc/stat)

# RAM - same as before (this one works)
RAM=$(free -m | awk 'NR==2{printf "%s/%s MB (%.2f%%)", $3,$2,$3*100/$2}')

# Disk - use grep to be safe instead of relying on NR==2
DISK=$(df -h / | grep -v Filesystem | awk '{print $5}')

# Flask status
FLASK=$(pgrep -f run.py > /dev/null && echo RUNNING || echo STOPPED)

echo "--------------------------------------------------" >> "$LOG"
echo "Timestamp: $(date)"       >> "$LOG"
echo "CPU Usage: ${CPU}%"       >> "$LOG"
echo "RAM Usage: $RAM"          >> "$LOG"
echo "Disk Usage: $DISK"        >> "$LOG"
echo "Flask Status: $FLASK"     >> "$LOG"
