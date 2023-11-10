1. Install docker and VSCode on your sytstem
2. Go to your favorite development folder 
3. Run "git clone https://github.com/cengwins/ceng435.git"
4. Open this folder in VSCode
5. Open a terminal and run "docker build -t ceng435 ."
6. After the image is built, run "docker run --rm -it  ceng435:latest" and you will be in your virtual Ubuntu 22.04 machine which run python code. Note that if you develop code in this virtual machine, if you stop the machine your code will be lost. That is why I recommend you to use Github to store your code and clone in the machine.
7. After running the Ubuntu VM, you can type "ifconfig -a" to see your network configuration. Work on eth0.
8. In VSCode install docker extension.
9. In the docker extension of VSCode, right click on your container and choose attach shell. Do this two times for having to terminals attached to Ubuntu VM. In one terminal, you can run the client and in the other terminal you can run the server. # ceng435
10. In the server terminal, move to the objects folder and run 
    10.1. chmod +x generateojects
    10.2. ./generateobjects
