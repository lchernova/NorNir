from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result
nr = InitNornir(config_file="config.yaml")

devices_sw = nr.filter(groups="switches")
devices_rtw = nr.filter(groups="routers")
rezult_port = ""
search_mac = 0000.0000.0001
result_arp = devices_sw.run(
    task=netmiko_send_command,
    command_string="show ip arp | inc %s" % search_mac 
               )
result_mac = devices_rt.run(
    task=netmiko_send_command,
    command_string="show mac addre | inc %s" % search_mac 
               )


for dev in ['sw1','sw2','sw3','sw4'] :
    for stroka in result_mac.dev.[0].result:
          int_s = re.search(' +\S+ *\+ +\S+ +(\S+)',result_mac)
          if int_s and int_s.group(0) not in nr.inventory.hosts.dev.ports :
              rezult_port = int_s.group(0)
              break
if rezult_port == ""
    for dev in ['r1','r2','r3'] :
      for stroka in result_arp.dev.[0].result:
          int_s = re.search('\.+(\w{4}\.\w{4}\.\w{4}) *\S+ *(\S+)',result_mac)          
          if int_s and int_s.group(1) not in nr.inventory.hosts.dev.ports :
              rezult_port = int_s.group(1)
              break
resultat = "МАС:%s - порт:%s" % (search_mac, rezult_port)
return(resultat)