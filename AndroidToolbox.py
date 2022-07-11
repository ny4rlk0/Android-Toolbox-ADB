import time;from tkinter import *;from tkinter import Text;from tkinter import filedialog;from tkinter.ttk import *;from threading import Thread as core;import os;import subprocess as sp;import sys
#github.com/ny4rlk0 && nyarlko.com
#
nya=0
rlko=0
#Translation Variables
lang="tr" # en, tr Change UI language with this variable
a1="";a2="";a3="";a4="";a5="";a6="";a7="";a8="";a9="";a10=""
a11="";a12="";a13="";a14="";a15="";a16="";a17="";a18="";a19="";a20="";a21=""
a22="";a23="";a24="";a25="";a26="";a27="";a28="";a29="";a30="";a31="";a32="";a33="";a34=""
a32="";a36="";a37="";a38="";a39=""
if lang=="en":
    a1="Installed apks:"
    a2="Android Toolbox 『ny4rlk0』 |☾☆|"
    a3="Backup Apk"
    a4="Connected device:"
    a5="No device connected or ADB Driver is not installed."
    a6="If you connected via WiFi you can unplug the USB now, also connect 1 device only!"
    a7="Backup apk --->"
    a8="Backup All APK"
    a9="Restore Multiple APK"
    a10="Refresh Apk List"
    a11="Select Apk"
    a12="Install Apk (Adb Install)"
    a13="Select Folder"
    a14="Apk Remove"
    a15="Install Apk (Temp method)"
    a16="Reboot BL FastBoot"
    a17="Reboot Recovery"
    a18="Reboot System"
    a19="Unlock OEM/Flash"
    a20="Lock OEM/Flash"
    a21="Wipe Device! <!>"
    a22="Flash: boot.img"
    a23="Flash: recovery.img"
    a24="Flash: system.img"
    a25="Flash: userdata.img"
    a26="Flash: *.zip"
    a27="Boot: Temp kernel.img"
    a28="Device IP Adress:"
    a29="Connect"
    a30="Disconnect"
    a31="Do not connect Wifi and USB at same time! Once you connect USB hit disconnect for ADB WiFi!"
    a32="Later if you decide you wanna switch WiFi just hit connect while USB is plugged in."
    a33="Then unplug the USB. Everytime you reboot the device, "
    a34="if you wanna connect using wifi first you need to connect with cable then press connect."
    a35="Wifi Reverse Shell:"
    a36="Sideload Firmware (.zip)"
    a37="Firmware (.zip)"
    a38="Flash: Custom Partition"
    a39="Custom Partition Name:"
if lang=="tr":
    a1="Cihazda yüklü uygulamalar:"
    a2="Android Araç Kutusu 『ny4rlk0』 |☾☆|"
    a3="Apk Yedekle"
    a4="Bağlı cihaz:"
    a5="Bir cihaz bağlı değil ya da Cihazınızın ADB Sürücüsü yüklü değil."
    a6="Cihaza Wifi aracılığıyla bağlandıysanız USB çıkarabilirsiniz, aynı anda sadece 1 cihaz bağlayın!"
    a7="Apk yedekleniyor --->"
    a8="Tüm APK Yedekle"
    a9="Toplu APK Yükle"
    a10="Apk Liste Yenile"
    a11="Apk Seç"
    a12="Apk Yükle (Adb install)"
    a13="Klasör Seç"
    a14="Apk Kaldır"
    a15="Apk Yükle (Temp Metodu)"
    a16="Yeniden Başlat FastBoot"
    a17="Yeniden Başlat Recovery"
    a18="Yeniden Başlat System"
    a19="Kilidi aç: OEM/Flash"
    a20="Kilitle: OEM/Flash"
    a21="Aygıtı Sil <!>"
    a22="Flash: boot.img"
    a23="Flash: recovery.img"
    a24="Flash: system.img"
    a25="Flash: userdata.img"
    a26="Flash: *.zip"
    a27="Boot: Geçici kernel.img"
    a28="Cihazın IP Adresi:"
    a29="Bağlan"
    a30="Bağlantıyı Kes"
    a31="Wifi ve USBye aynı anda bağlanmayın! USB kablo ile bağlandığınız zaman ADB Wifi sekmesinde,"
    a32="bağlantıyı kes butonuna basın. Daha sonra tekrar Wifi ile bağlanmak isterseniz kabloyu bağlıyken,"
    a33="ADB Wifi sekmesindeki bağlan butonuna basın. Cihazı her yeniden başlattığınızda kablo ile bağlayıp"
    a34="ADB Wifi sekmesinde bağlan butonuna basmanız gerekmektedir eğer wifi üzerinden bağlanmak istiyorsanız."
    a35="Wifi Komut Satırı:"
    a36="Sideload Firmware (.zip)"
    a37="Firmware (.zip)"
    a38="Flash: Custom Partition"
    a39="Custom Partition Adı:"
#End Translation Variables
installed_apk_list=[]
apk_combobox_list=[]
apk_list=[] #APK File List
connected_device=""
last_device=""
device_mode=""#adb, fastboot, not_connected
adb_ip=""
sq="'" #{sq}
dq='"'#{dq}
temp_dir="/data/local/tmp/" #inside phone or android device
w=Tk();w.title(a2)#;w.configure(background='black')
apk_label1=Label (w, text=a4,font="none 12 bold");apk_label1.grid(row=1,column=0,sticky=W)
apk_label2=Label (w, text="",font="none 12 bold");apk_label2.grid(row=1,column=1,sticky=W)
apk_label=Label (w, text=a1,font="none 12 bold");apk_label.grid(row=2,column=0,sticky=W)
def scan_apks(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".APK") or file.endswith(".apk"):
                apk_list.append(os.path.join(file))
                #print(os.path.join(file))
                #print(file)
def reverse_shell():
    global device_mode
    adb_path=os.getcwd()+"\\"+'adb.exe'
    fastboot_path=os.getcwd()+"\\"+'fastboot.exe'
    if device_mode=="adb":
        cmd=adb_path+' '+ReverseShellBox.get()
    elif device_mode=="fastboot":
        cmd=fastboot_path+' '+ReverseShellBox.get()
    print(cmd)
    try:
        out=os.system(cmd)
        #out=sp.Popen([cmd],stdout=sp.PIPE,shell=True)
        #(out, err) = out.communicate()
        print("reverse_shell_log"+str(out))
    except Exception as e:print("reverse_shell_error_log:"+e)
def chk_device_connection():
    while True:
        global connected_device, last_device,device_mode,adb_ip
        #print("Checking the device connection...")
        out=sp.Popen(['adb','devices'],stdout=sp.PIPE,shell=True)
        (out, err) = out.communicate()
        #out=os.system('adb devices')
        devices=str(out)
        devices=devices.replace("List of devices attached","")
        devices=devices.replace("b'","")
        devices=devices.replace("'","")
        devices=devices.replace("\\tdevice","")
        devices=devices.split("\\r\\n")
        devices=list(filter(None, devices))
        how_many_devices=len(devices)
        connected_device=devices
        #print(devices)
        if how_many_devices>=2:
            apk_label2.config(text=a6)
            connected_device="none" #Multiple Dev Connected We do not support that for now!
            device_mode="not_connected"
        elif how_many_devices==0: # No ADB connection found. Lets check for fastboot?
            #Checking Fastboot status
            out=sp.Popen(['fastboot','devices'],stdout=sp.PIPE,shell=True)
            (out, err) = out.communicate()
            o=str(out)
            if 'fastboot' in o:
                device_mode="fastboot"
                o=o.replace("b'","")
                o=o.replace("'","")
                o=o.replace("\\t"," ")
                o=o.replace("\\r\\n"," ")
                apk_label2.config(text=o)
            else:
                apk_label2.config(text=a5)
                device_mode="not_connected"
            connected_device="none" #No ADB Installable Dev Connected or not in ADB mode
        else:
            apk_label2.config(text=str(devices)+" Android Debug Bridge") #Single Dev Connected
            device_mode="adb"
            if connected_device != last_device:
                try:         
                    out=sp.Popen(['adb','shell','ip','-f','inet','addr','show','wlan0'],stdout=sp.PIPE,shell=True)
                    (out, err) = out.communicate()
                    o=str(out)
                    o=o.replace("\\r\\n","")
                    o=o.replace("valid_lft forever preferred_lft forever'","")
                    o=o.replace("scope global wlan0","")
                    o=o.replace("32: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 3000","")
                    o=o.replace("b'","")
                    o=o.replace("/24 brd","")
                    o=o.replace("inet","")
                    o=o.split(" ")
                    o=list(filter(None, o))
                    o=str(o[0])
                    adb_ip=o
                    wifibox.delete(0,END)
                    wifibox.insert(0,adb_ip)
                    #print(o)
                except:pass
        if connected_device != last_device:
            last_device=connected_device
            fetch_installed_apks()
        time.sleep(2)
def fetch_installed_apks():
    global installed_apk_list,apk_combobox_list,live_apk_comboboxlist
    apk_combobox_list=[]
    installed_apk_list=[]
    live_apk_comboboxlist.set("")
    live_apk_comboboxlist["values"]=[]
    out=sp.Popen(['adb','shell','pm','list','packages'],stdout=sp.PIPE,shell=True)
    (out, err) = out.communicate()
    out=str(out)
    #print("APK_LIST:"+out)
    out=out.replace('package:','')
    out=out.replace("b'","")
    out=out.split("\\r\\n") #n
    for val in out:
        apk_combobox_list.append(val)
    apk_combobox_list.pop(-1)
    for a in apk_combobox_list:
        live_apk_comboboxlist["values"]=apk_combobox_list
def backup_apk():
    if connected_device != "none" and live_apk_comboboxlist.get() != "":
        current_dir=os.getcwd()+"\\"
        selected_apk_name=live_apk_comboboxlist.get()
        create_device_dir()
        export_dir=current_dir+str(connected_device)+"\\"+selected_apk_name+'\\'
        try:os.mkdir(export_dir)
        except Exception as e:print("Export dir already exists!");print(e)
        out=sp.Popen(['adb','shell','pm','path',f'{selected_apk_name}'],stdout=sp.PIPE,shell=True)
        (out, err) = out.communicate()
        path=str(out)
        path=path.replace("b'","")
        path=path.replace("\\r\\n'","")
        path=path.replace('package:','')
        try:
            path=path.split('\\r\\n')
            for paths in path:
                paths=str(paths)
                out2=sp.Popen(['adb','pull',f'{paths}',f'{export_dir}'],stdout=sp.PIPE,shell=True)
                (out2, err2) = out2.communicate()
            print(a7)
            print(str(paths))
            print(export_dir)
        except Exception as e:print(e)
        base_apk_dir=export_dir+'base.apk'
        new_apk_dir=export_dir+selected_apk_name+".apk"
        try:os.rename(f'{base_apk_dir}',f'{new_apk_dir}')
        except:pass
def multiple_apk_restore():
    if connected_device != "none":
        global apk_list
        apk_list=[]
        folder=None
        folder = filedialog.askdirectory()
        if folder != "":
            print(folder)
            folder=folder+"/"
            print(folder)
            scan_apks(folder)
            for apk in apk_list:
                apk_pathd=folder+apk
                print(apk_pathd)
                install_apk=sp.Popen(['adb','install',f'{apk_pathd}'],stdout=sp.PIPE,shell=True)
                (install_apk, install_apk_err) = install_apk.communicate()
                install_apk2=sp.Popen(['adb','install','-r',f'{apk_pathd}'],stdout=sp.PIPE,shell=True)
                (install_apk2, install_apk_err) = install_apk2.communicate()
                time.sleep(4)
        fetch_installed_apks()
def single_apk_restore():
    if connected_device != "none":
        file = filedialog.askopenfile(mode='r', filetypes=[(a11, '*.apk')])
        #print(type(file))
        if file is not None:
            print(file.name)
            install_apk=sp.Popen(['adb','install',f'{file.name}'],stdout=sp.PIPE,shell=True)
            (install_apk, install_apk_err) = install_apk.communicate()
            install_apk2=sp.Popen(['adb','install','-r',f'{file.name}'],stdout=sp.PIPE,shell=True)
            (install_apk2, install_apk_err) = install_apk2.communicate()
            fetch_installed_apks()
def alternative_single_apk_restore():
    if connected_device != "none":
        file = filedialog.askopenfile(mode='r', filetypes=[(a11, '*.apk')])
        #print(type(file))
        if file is not None:
            print(file.name)
            install_apk=sp.Popen(['adb','push',f'{file.name}',f'{temp_dir}'],stdout=sp.PIPE,shell=True)#copy apk to temp dir
            (install_apk, install_apk_err) = install_apk.communicate()
            install_apk2=sp.Popen(['adb','shell','pm','-t','-f',f'{temp_dir}'],stdout=sp.PIPE,shell=True)#install apk from temp dir
            (install_apk2, install_apk_err) = install_apk2.communicate()
            install_apk3=sp.Popen(['adb','shell','rm','-f',f'{temp_dir}'],stdout=sp.PIPE,shell=True)#delete apk in temp dir since we installed and no longer needed.
            (install_apk3, install_apk_err) = install_apk3.communicate()
def create_device_dir():
    current_dir=os.getcwd()+"\\"
    try:os.mkdir(current_dir+str(connected_device)+"\\")
    except Exception as e:print("Export dir already exists!");print(e)
def apk_remove():
    selected_apk_name=live_apk_comboboxlist.get()
    remove_apk=sp.Popen(['adb','uninstall',f'{selected_apk_name}'],stdout=sp.PIPE,shell=True)
    (remove_apk, install_apk_err) = remove_apk.communicate()
    fetch_installed_apks()
def multiple_apk_backup():
    fetch_installed_apks()
    current_dir=os.getcwd()+"\\"
    apk_list=apk_combobox_list
    create_device_dir()
    for apk in apk_list:
        export_dir=current_dir+apk+'\\'
        try:os.mkdir(export_dir)
        except Exception as e:print("Export dir already exists!");print(e)
        out=sp.Popen(['adb','shell','pm','path',f'{apk}'],stdout=sp.PIPE,shell=True)
        (out, err) = out.communicate()
        path=str(out)
        path=path.replace("b'","")
        path=path.replace("\\r\\n'","")
        path=path.replace('package:','')
        try:
            path=path.split('\\r\\n')
            for paths in path:
                paths=str(paths)
                out2=sp.Popen(['adb','pull',f'{paths}',f'{export_dir}'],stdout=sp.PIPE,shell=True)
                (out2, err2) = out2.communicate()
            print(a7)
            print(str(paths))
        except Exception as e:print(e)
        base_apk_dir=export_dir+'base.apk'
        new_apk_dir=export_dir+apk+".apk"
        try:os.rename(f'{base_apk_dir}',f'{new_apk_dir}')
        except:pass
#ADB_DEBUGGUNG
def reboot_bootloader():
    if device_mode=="adb":
        nya_x=sp.Popen(['adb','reboot-bootloader'],stdout=sp.PIPE,shell=True)
        (nya_x, x_err) = nya_x.communicate()
def reboot_recovery():
    if device_mode=="adb":
        nya_x=sp.Popen(['adb','reboot','recovery'],stdout=sp.PIPE,shell=True)
        (nya_x, x_err) = nya_x.communicate()
def reboot_system():
    if device_mode=="adb":
        nya_x=sp.Popen(['adb','reboot','system'],stdout=sp.PIPE,shell=True)
        (nya_x, x_err) = nya_x.communicate()
#FastBoot
def reboot_system_fastboot():
    if device_mode=="fastboot":
        nya_x=sp.Popen(['fastboot','reboot'],stdout=sp.PIPE,shell=True)
        (nya_x, x_err) = nya_x.communicate()
def reboot_recovery_fastboot():
    if device_mode=="fastboot":
        nya_x=sp.Popen(['fastboot','reboot','recovery'],stdout=sp.PIPE,shell=True)
        (nya_x, x_err) = nya_x.communicate()
def unlock_dev_fastboot():
    if device_mode=="fastboot":
        nya_x=sp.Popen(['fastboot','oem','unlock'],stdout=sp.PIPE,shell=True)
        (nya_x, x_err) = nya_x.communicate()
        nya_x2=sp.Popen(['fastboot','flashing','unlock'],stdout=sp.PIPE,shell=True)
        (nya_x2, x_err2) = nya_x2.communicate()
        nya_x3=sp.Popen(['fastboot','flashing','unlock_critical'],stdout=sp.PIPE,shell=True)
        (nya_x3, x_err3) = nya_x3.communicate()
        nya_x4=sp.Popen(['fastboot','oem','unlock'],stdout=sp.PIPE,shell=True)
        (nya_x4, x_err4) = nya_x4.communicate()
def lock_dev_fastboot():
    if device_mode=="fastboot":
        nya_x=sp.Popen(['fastboot','oem','lock'],stdout=sp.PIPE,shell=True)
        (nya_x, x_err) = nya_x.communicate()
        nya_x2=sp.Popen(['fastboot','flashing','lock'],stdout=sp.PIPE,shell=True)
        (nya_x2, x_err2) = nya_x2.communicate()
        nya_x3=sp.Popen(['fastboot','flashing','lock_critical'],stdout=sp.PIPE,shell=True)
        (nya_x3, x_err3) = nya_x3.communicate()
        nya_x4=sp.Popen(['fastboot','oem','lock'],stdout=sp.PIPE,shell=True)
        (nya_x4, x_err4) = nya_x4.communicate()
def wipe_device(): #Not tested since i dont have any device i can wipe!
    if device_mode=="fastboot":
        nya_x=sp.Popen(['fastboot','format','cache'],stdout=sp.PIPE,shell=True)
        (nya_x, x_err) = nya_x.communicate()
        nya_x2=sp.Popen(['fastboot','format','data'],stdout=sp.PIPE,shell=True)
        (nya_x2, x_err2) = nya_x2.communicate()
        nya_x3=sp.Popen(['fastboot','flashall','-w'],stdout=sp.PIPE,shell=True)
        (nya_x3, x3_err) = nya_x3.communicate()
        nya_x4=sp.Popen(['fastboot','erase','data'],stdout=sp.PIPE,shell=True)
        (nya_x4, x_err4) = nya_x4.communicate()
        nya_x5=sp.Popen(['fastboot','erase','system'],stdout=sp.PIPE,shell=True)
        (nya_x5, x_err5) = nya_x5.communicate()
        nya_x6=sp.Popen(['fastboot','erase','cache'],stdout=sp.PIPE,shell=True)
        (nya_x6, x_err6) = nya_x6.communicate()
        nya_x7=sp.Popen(['fastboot','erase','system','-w'],stdout=sp.PIPE,shell=True)
        (nya_x7, x_err7) = nya_x7.communicate()
        nya_x8=sp.Popen(['fastboot','format:ext4','userdata'],stdout=sp.PIPE,shell=True)
        (nya_x8, x_err8) = nya_x8.communicate()       
    if device_mode=="adb":
        nya_x=sp.Popen(['adb','shell','recovery','-wipe_data'],stdout=sp.PIPE,shell=True)
        (nya_x, x_err) = nya_x.communicate()
        nya_x2=sp.Popen(['adb','shell','recovery','-wipe'],stdout=sp.PIPE,shell=True)
        (nya_x2, x_err2) = nya_x2.communicate()
        nya_x3=sp.Popen(['adb','shell','wipe','data'],stdout=sp.PIPE,shell=True)
        (nya_x3, x_err3) = nya_x3.communicate()
        reboot_recovery()
def flash_boot_fastboot():
    if device_mode=="fastboot":
        file = filedialog.askopenfile(mode='r', filetypes=[("boot.img", '*.img')])
        #print(type(file))
        if file is not None:
            if ".img" in file.name:
                nya_x=sp.Popen(['fastboot','flash','boot',f'{file.name}'],stdout=sp.PIPE,shell=True)
                (nya_x, x_err) = nya_x.communicate()
def flash_recovery_fastboot():
    if device_mode=="fastboot":
        file = filedialog.askopenfile(mode='r', filetypes=[("recovery.img", '*.img')])
        #print(type(file))
        if file is not None:    
            if ".img" in file.name:
                nya_x=sp.Popen(['fastboot','flash','recovery',f'{file.name}'],stdout=sp.PIPE,shell=True)
                (nya_x, x_err) = nya_x.communicate()
def flash_system_fastboot():
    if device_mode=="fastboot":
        file = filedialog.askopenfile(mode='r', filetypes=[("system.img", '*.img')])
        #print(type(file))
        if file is not None:
            if ".img" in file.name:
                nya_x=sp.Popen(['fastboot','flash','system',f'{file.name}'],stdout=sp.PIPE,shell=True)
                (nya_x, x_err) = nya_x.communicate()
def flash_userdata_fastboot():
    if device_mode=="fastboot":
        file = filedialog.askopenfile(mode='r', filetypes=[("userdata.img", '*.img')])
        #print(type(file))
        if file is not None:
            if ".img" in file.name:
                nya_x=sp.Popen(['fastboot','flash','userdata',f'{file.name}'],stdout=sp.PIPE,shell=True)
                (nya_x, x_err) = nya_x.communicate()
def flash_zip_fastboot():
    if device_mode=="fastboot":
        file = filedialog.askopenfile(mode='r', filetypes=[("*.zip", '*.zip')])
        #print(type(file))
        if file is not None:
            if ".zip" in file.name:
                nya_x=sp.Popen(['fastboot','flash','zip',f'{file.name}'],stdout=sp.PIPE,shell=True)
                (nya_x, x_err) = nya_x.communicate()
def boot_kernel_fastboot():
    if device_mode=="fastboot":
        file = filedialog.askopenfile(mode='r', filetypes=[("boot.img", '*.img')])
        #print(type(file))
        if file is not None:
            if ".img" in file.name:
                nya_x=sp.Popen(['fastboot','boot',f'{file.name}'],stdout=sp.PIPE,shell=True)
                (nya_x, x_err) = nya_x.communicate()
def connect_adb_overwifi():
    if device_mode=="adb":
        ip=wifibox.get()
        nya_x=sp.Popen(['adb','tcpip','5555','&&','adb','connect',f'{ip}:5555'],stdout=sp.PIPE,shell=True)
        (nya_x, x_err) = nya_x.communicate()
def disconnect_adb_overwifi():
        ip=wifibox.get()
        nya_x=sp.Popen(['adb','disconnect',f'{ip}:5555'],stdout=sp.PIPE,shell=True)
        (nya_x, x_err) = nya_x.communicate()
def sideload_firmware():
    if device_mode=="adb":
        file = filedialog.askopenfile(mode='r', filetypes=[(a37, '*.zip')])
        if file is not None:
            if ".zip" in file.name or ".ZIP" in file.name:
                nya_x=sp.Popen(['adb','sideload',f'{file.name}'],stdout=sp.PIPE,shell=True)
                (nya_x, x_err) = nya_x.communicate()
def flash_custom_partition_fastboot():
    if device_mode=="fastboot":
        partition_name=PartitionFlash.get()
        file = filedialog.askopenfile(mode='r', filetypes=[("*.img", '*.img')])
        #print(type(file))
        if file is not None:
            if ".img" in file.name:
                nya_x=sp.Popen(['fastboot','flash',f'{partition_name}',f'{file.name}'],stdout=sp.PIPE,shell=True)
                (nya_x, x_err) = nya_x.communicate()
#User Interface Settings

#Combo_Box_Apk_Select_List    
live_apk_comboboxlist=Combobox(w,width=100,values=apk_combobox_list, state="readonly")# state="readonly"
live_apk_comboboxlist.grid(row=2,column=1)
#BackupButton
backupButton=Button(w,text=a3,width=24,command=backup_apk)
backupButton.grid(row=3,column=1,sticky=W)
#RefreshApkList
refreshApkList=Button(w,text=a10,width=24,command=fetch_installed_apks)
refreshApkList.grid(row=3,column=0,sticky=W)
#MultipleApkBackup
MultipleApkBackup=Button(w,text=a8,width=24,command=multiple_apk_backup)
MultipleApkBackup.grid(row=4,column=0,sticky=W)
#MultipleApkRestore
MultipleApkRestore=Button(w,text=a9,width=24,command=multiple_apk_restore)
MultipleApkRestore.grid(row=4,column=1,sticky=W)
#SingleApkRestore
SingleApkRestore=Button(w,text=a12,width=24,command=single_apk_restore)
SingleApkRestore.grid(row=5,column=0,sticky=W)
#ApkRemove
ApkRemove=Button(w,text=a14,width=24,command=apk_remove)
ApkRemove.grid(row=5,column=1,sticky=W)
#ApkInstall2
SingleApkRestore2=Button(w,text=a15,width=24,command=alternative_single_apk_restore)
SingleApkRestore2.grid(row=6,column=0,sticky=W)

#MenuAyracı
ayrac=Label (w, text="ADB",font="none 12 bold");ayrac.grid(row=7,column=0,sticky=W)

#RebootBootloader
rebootboot=Button(w,text=a16,width=24,command=reboot_bootloader)
rebootboot.grid(row=8,column=0,sticky=W)
#RebootRecovery
RebootRecovery=Button(w,text=a17,width=24,command=reboot_recovery)
RebootRecovery.grid(row=8,column=1,sticky=W)
#RebootSystem
RebootSystem=Button(w,text=a18,width=24,command=reboot_system_fastboot)
RebootSystem.grid(row=9,column=0,sticky=W)
#SideloadFirmware
SideloadFirmware=Button(w,text=a36,width=24,command=sideload_firmware)
SideloadFirmware.grid(row=9,column=1,sticky=W)
#MenuAyracı
ayrac=Label (w, text="FAST BOOT",font="none 12 bold");ayrac.grid(row=10,column=0,sticky=W)

#Unlock_Dev_FastBoot
unlock_Dev=Button(w,text=a19,width=24,command=unlock_dev_fastboot)
unlock_Dev.grid(row=11,column=0,sticky=W)
#RebootRecovery_FastBoot
RebootRecoveryFastBoot=Button(w,text=a17,width=24,command=reboot_recovery_fastboot)
RebootRecoveryFastBoot.grid(row=11,column=1,sticky=W)
#RebootSystem_FastBoot
RebootSystemFastBoot=Button(w,text=a18,width=24,command=reboot_system_fastboot)
RebootSystemFastBoot.grid(row=12,column=0,sticky=W)
#Lock_Dev
lock_Dev=Button(w,text=a20,width=24,command=lock_dev_fastboot)
lock_Dev.grid(row=12,column=1,sticky=W)

#MenuAyracı
ayrac=Label (w, text="FAST BOOT / Flash",font="none 12 bold");ayrac.grid(row=13,column=0,sticky=W)

#FlashBootFastBoot
FlashBootFastBoot=Button(w,text=a22,width=24,command=flash_boot_fastboot)
FlashBootFastBoot.grid(row=14,column=0,sticky=W)
#FlashRecoveryFastBoot
FlashRecoveryFastBoot=Button(w,text=a23,width=24,command=flash_recovery_fastboot)
FlashRecoveryFastBoot.grid(row=14,column=1,sticky=W)
#FlashSystemFastBoot
FlashSystemFastBoot=Button(w,text=a24,width=24,command=flash_system_fastboot)
FlashSystemFastBoot.grid(row=15,column=0,sticky=W)
#FlashUserdataFastBoot
FlashUserdataFastBoot=Button(w,text=a25,width=24,command=flash_userdata_fastboot)
FlashUserdataFastBoot.grid(row=15,column=1,sticky=W)
#FlashZipFastBoot
FlashZipFastBoot=Button(w,text=a26,width=24,command=flash_zip_fastboot)
FlashZipFastBoot.grid(row=16,column=0,sticky=W)
#FlashKernelFastBoot
FlashKernelFastBoot=Button(w,text=a27,width=24,command=boot_kernel_fastboot)
FlashKernelFastBoot.grid(row=16,column=1,sticky=W)
#FastbootCustomPartitionFlashLabel
ayrac=Label (w, text=a39,font="none 12 bold");ayrac.grid(row=17,column=0,sticky=W)
#FastbootCustomPartitionFlashBox
PartitionFlash=Entry(w,textvariable='',width=40);PartitionFlash.grid(row=17,column=1,sticky=W)
#FastbootCustomPartitionFlash
FastbootCustomPartitionFlash=Button(w,text=a38,width=24,command=flash_custom_partition_fastboot)
FastbootCustomPartitionFlash.grid(row=18,column=1,sticky=W)
#MenuAyracı
ayrac=Label (w, text="FAST BOOT / ADB",font="none 12 bold");ayrac.grid(row=19,column=0,sticky=W)
#Wipe_Device
lock_Dev=Button(w,text=a21,width=24,command=wipe_device)
lock_Dev.grid(row=20,column=0,sticky=W)
#MenuAyracı
ayrac=Label (w, text="ADB WiFi",font="none 12 bold");ayrac.grid(row=21,column=0,sticky=W)
#WifiLabel
ayrac=Label (w, text=a28,font="none 12 bold");ayrac.grid(row=22,column=0,sticky=W)
#WifiBox
wifibox=Entry(w,textvariable="",width=40);wifibox.grid(row=22,column=1,sticky=W)
#WifiOverADB #Make sure usb is connected at pairing everytime device reboots!
WifiOverAdb=Button(w,text=a29,width=24,command=connect_adb_overwifi)
WifiOverAdb.grid(row=23,column=0,sticky=W)
#WifiOverADB #Make sure usb is connected at pairing everytime device reboots!
WifiOverAdb2=Button(w,text=a30,width=24,command=disconnect_adb_overwifi)
WifiOverAdb2.grid(row=23,column=1,sticky=W)
#ReverseShellLabel
ayrac=Label (w, text=a35,font="none 12 bold");ayrac.grid(row=24,column=0,sticky=W)
#ReverseShellBox
ReverseShellBox=Entry(w,textvariable='',width=80);ReverseShellBox.grid(row=24,column=1,sticky=W)
#ReverseShellCommandSendButton
ReverseShellCommandSendButton=Button(w,text='>',width=25,command=reverse_shell)
ReverseShellCommandSendButton.grid(row=25,column=1,sticky=W)

#Warning
ayrac=Label (w, text=a31,font="none 10");ayrac.grid(row=26,column=1,sticky=W)
#Warning
ayrac=Label (w, text=a32,font="none 10");ayrac.grid(row=27,column=1,sticky=W)
#Warning
ayrac=Label (w, text=a33,font="none 10");ayrac.grid(row=28,column=1,sticky=W)
#Warning
ayrac=Label (w, text=a34,font="none 10");ayrac.grid(row=29,column=1,sticky=W)
#Warning
ayrac=Label (w, text="Written by github.com/ny4rlk0 with『❤』",font="none 16");ayrac.grid(row=30,column=1,sticky=W)
#Constantly_chk_for_device_connection_in_side_proccess
chk_dev = core(target=chk_device_connection)
chk_dev.daemon=True
chk_dev.start()
#Check_installed_apks_from_start
fetch_installed_apks()
if nya!=0 or rlko!=0:
    sys.exit(0)
#Start_Drawing_UI
w.mainloop()
#Exit_App_With_Success_Code
sys.exit(0)
