from Lib_space import Local_UI as A
import time
A.init_ssh()
# A.cmd_ssh("app")  # login as root
# A.cmd_ssh("7uR!\!2dxp*t$")  # root Password
A.cmd_ssh("login root")
A.cmd_ssh("X*rD8u!6nk")
A.cmd_ssh("cd /home/sdk/")
A.cmd_ssh("mount -o remount rw /home/sdk/")
A.cmd_ssh("mv auto_disable_sshd.sh auto_disable_sshd.sh.bak")
A.cmd_ssh("mv disable_ssh.sh disable_ssh.sh.bak")
A.cmd_ssh("cd /home/data/global/")
A.cmd_ssh("mount -o remount rw /home/data/global/")
A.cmd_ssh("mv sshd_disable.txt sshd_disable.txt.bak")
time.sleep(3)
A.cmd_ssh("reboot")
A.close_ssh()