#!/bin/bash
# /etc/init.d/scoreboard-control.sh

### BEGIN INIT INFO
# Provides:          scoreboard-control
# Required-Start:    $syslog
# Required-Stop:     $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: scoreboard service init script
# Description:       This service is used to manage a poweroff button
### END INIT INFO

PIDFILE=/tmp/.scoreboard.pid
PYTHON=/usr/bin/python
PYSCRIPT=/home/devel/git/schibsted/scoreboard/scoreboard.py

. /lib/lsb/init-functions

case "$1" in
	start)
		log_action_msg "starting scoreboard service"
		if [ -f $PIDFILE ]
		then
			log_failure_msg "the service seems to be running"
			exit -1
		fi
		$PYTHON $PYSCRIPT &
		sleep 1
		PID=$(ps -fA | grep scoreboard.py | grep -v grep | awk '{ print $2 }')
		echo "$PID" > $PIDFILE
		log_success_msg "service started"
		;;
	stop)
		log_action_msg "stopping scoreboard service"
		if [ -f $PIDFILE ]
		then
			PID=`cat $PIDFILE`
			rm -f $PIDFILE
			kill -15 $PID
			log_success_msg "service stopped"
		else
			log_failure_msg "the service seems to be already stopped"
		fi
		;;
	status)
		PID=$(ps -fA | grep scoreboard.py | grep -v grep | awk '{ print $2 }')
		if [ -f $PIDFILE -a -n "$PID" ]
		then
			PIDF=$(cat $PIDFILE)
			if [ "$PID" = "$PIDF" ]
			then
				log_success_msg "the service is running"
			else
				log_warning_msg "the service seems to be running"
			fi
		else
			log_failure_msg "service seems to be stopped"
		fi
		;;
	restart)
		stop
		start
		;;
	*)
		echo $"Usage: $prog {start|stop|restart|status}"
esac

