# CloudStack reboot stopper
## CloudStack
If CloudStack agent cannot access to primary storage between 5 minutes, it do auto-rebooting.

This program is monitoring primary storage connection and stop rebooting.

## Usage
$ git clone https://github.com/palloc/cloudstack-safe-rebooter

$ cd cloudstack-safe-rebooter

$ sudo python stop-reboot.py [primary_storage_ip_address] &
