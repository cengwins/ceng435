
1. Install docker and VSCode on your sytstem
2. Go to your favorite development folder
3. Run "git clone https://github.com/cengwins/ceng435.git"
4. Open this folder in VSCode
5. Open a terminal and run "docker build -t ceng435 ."
6. In one terminal, you can run your client and in the other terminal you can run your server. For doing this, after the image is built:
   1. **in one terminal**, run "docker run -t -i --rm --privileged --cap-add=NET_ADMIN --name ceng435vm -v ./code:/app:rw ceng435:latest bash" and you will be in your virtual Ubuntu 22.04 machine (python installed). Note that if you develop code in this virtual machine, if you stop the machine your code will be lost. That is why I recommend you to use Github to store your code and clone in the machine, and push your code to Github before shutting the virtual machine down. The other option is to work in the /app folder in your virtual machine which is mounted to the "code" directory of your own machine...
   2. **in another terminal** to attach to the same container, run "docker exec -it ceng435vm bash"
7. After running the Ubuntu VM, you can type "ifconfig -a" to see your network configuration. Work on eth0.
8. In VSCode install docker extension.
9. In the docker extension of VSCode, right click on your container and choose attach shell. Do this two times for having to terminals attached to Ubuntu VM. In one terminal, you can run the client and in the other terminal you can run the server.
10. In the server terminal, move to the objects folder and run
    10.1. chmod +x generateojects
    10.2. ./generateobjects

Some tc commands that may be of help to you can be found at https://man7.org/linux/man-pages/man8/tc-netem.8.html

