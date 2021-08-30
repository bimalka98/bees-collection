## *Installing Chisel and FPGA Tools*

### ======= Installing Quartus =======

To build hardware for an FPGA, you need a synthesize tool. The two major FPGA vendors, Intel and Xilinx, provide free versions of their tools that cover small to mediumsized FPGAs. Those medium-sized FPGAs are large enough to build multicore RISC style processors. Intel provides the Quartus Prime Lite Edition and Xilinx the Vivado Design Suite, WebPACK Edition.

🔴 **In order to download the below mentioned files you need to have a user account with intel! When you try to download one of them it will be automatically prompted to create one. This registration process is little slow and you may have to wait like a day sometimes!**

#### 1. Download Quartus Prime Lite Edition from [here](https://fpgasoftware.intel.com/?edition=lite). There are several methods to download and install Intel® FPGA software:

- The bundled set of software and device files in .tar format
- Individual executable files for customized download and installation: I will be doing this as it is good enough and costs minimum data charges.

#### 2. Choose `Individual Files` tab in the above download web page and download the following files. ***Wait for all of the files to completely download before beginning the installation process.*** ⚠ 
- Quartus Prime Lite Edition (Free) (Quartus Prime (includes Nios II EDS) and ModelSim-Intel FPGA Edition (includes Starter Edition))
- Devices: You must install device support for at least one device family to use the Quartus Prime software. I will be installing the device support for `DE0-Nano board` which contains an `Altera Cyclone® IV EP4CE22F17C6N FPGA` as it is the one we are provided at university for laboratory exercises. The file to be downloaded as `Cyclone IV device support`.

#### 3. Run the `QuartusLiteSetup-<version>` file to begin the installation process. 

- The main Quartus Prime software installer launches and ***automatically detects all other software and device support installation files in the same directory*** and installs the software and device support.

You can add additional device support to an existing Quartus Prime software installation without having to reinstall the entire software package. Use the `Install Devices` command on the Tools menu in the Quartus Prime software to get started.

### ======= Installing Chisel =======

As Chisel is a Scala library, all IDEs that support Scala are also good IDEs for Chisel. It is possible in Eclipse and IntelliJ to generate a project from the sbt project configuration in build.sbt. I found that configuring IntelliJ IDEA for chisel is much easier and faster. 

Scala itself depends on the installation of the Java JDK 1.8. which is also known as Java SE Development Kit 8 (https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html) You need to install this first.

1. [Install IntelliJ](https://youtu.be/EMLTOMdIz4w) here in this guide you will be installing the latest JDK. But chisel requires JDK 1.8.! We can configure the required JDK version for a given project  maually throgh the IntelliJ IDE later. So nothing to worry at all!
2. [Setup Scala on IntelliJ](https://youtu.be/u0FLmrnAm5k)
3. Install sbt[Scala built tool](https://www.scala-sbt.org/release/docs/Setup.html). This is a common link for all the Operating systems. So navigate to `Installing sbt on Windows` from the left side drop down menu, Download msi installer and install it. 
4. Make sure to include all the JDKs in your environment path variables!
5. Restart your PC; and open the required project in IntelliJ. It will first download some files automatically. Let it do its job! 
6. Configure the required project JDK(SDK version 8) following the steps mentioned [here](https://www.jetbrains.com/help/idea/sdk.html#change-project-sdk)
7. Open the terminal in IntelliJ and try executing `sbt run`.
8. That's it.! If it's not working simply restart the IntelliJ IDEA and give it a try again.


### ======= Installing Verilator =======

> ***Using WSL2***

```shell
bimalka98@LAP-BIMALKA98:~$ sudo apt-get install verilator  #to install verilator
bimalka98@LAP-BIMALKA98:~$ verilator
Usage:
        verilator --help
        verilator --version
        verilator --cc [options] [source_files.v]... [opt_c_files.cpp/c/cc/a/o/so]
        verilator --sc [options] [source_files.v]... [opt_c_files.cpp/c/cc/a/o/so]
        verilator --lint-only -Wall [source_files.v]...

bimalka98@LAP-BIMALKA98:~$ dpkg --listfiles verilator #find the directories of the verilator to change the directory
bimalka98@LAP-BIMALKA98:~$ cd /usr/share/doc/verilator/examples #changing directory to examples 
```
