from modules import system_info
from modules import suid_scan
from modules import permission_scan
from modules import cron_scan
from modules import sudo_scan
from modules import service_scan
from modules import capability_scan
from modules import kernel_scan

system_info.run()
suid_scan.run()
permission_scan.run()
cron_scan.run()
sudo_scan.run()
service_scan.run()
capability_scan.run()
kernel_scan.run()
