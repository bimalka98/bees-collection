> ***“Always Strive for Excellence before you Chase  Success.”***



---

## *Research*

1. Landing an Impactful Research Project by Mr. Ashwin De Silva [[video]](https://youtu.be/qNz2S5G8GuM) [[pdf]](https://laknath1996.github.io/docs/talks/kickstarting_projects_2021.pdf)
2. [Convert PDFs to Audiobooks with Machine Learning](https://konfido.github.io/Convert-PDFs-to-Audiobooks-with-Machine-Learning/)

---


## *AI*

1. Papers & tech blogs by companies sharing their work on data science & machine learning in production [eugeneyan/applied-ml](https://github.com/eugeneyan/applied-ml)

---

## *Installing Chisel and FPGA Tools*

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

