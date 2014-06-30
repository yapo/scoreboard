#!/bin/bash

# check if the files exists
if [ ! -f scoreboard-control.sh ]
then
	echo "the scripts are missing!"
	exit -1
fi

# cleanup
rm -f /etc/init.d/scoreboard-control.sh
rm -f /etc/rc0.d/*scoreboard-control*
rm -f /etc/rc1.d/*scoreboard-control*
rm -f /etc/rc2.d/*scoreboard-control*
rm -f /etc/rc3.d/*scoreboard-control*
rm -f /etc/rc4.d/*scoreboard-control*
rm -f /etc/rc5.d/*scoreboard-control*
rm -f /etc/rc6.d/*scoreboard-control*

# install the raspy-control scripts
chmod +x scoreboard-control.sh
cp scoreboard-control.sh /etc/init.d/
update-rc.d scoreboard-control.sh defaults
