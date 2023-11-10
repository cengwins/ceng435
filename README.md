
Install docker and VSCode on your sytstem

Go to your favorite development folder on your local machine and run

```
   git clone https://github.com/cengwins/ceng435.git
```

Open this folder (ceng435) in VSCode

Open a terminal in VSCode, under the ceng435 directory where the Dockerfile resides run

```
   docker build -t ceng435 .
```

After the image is built

**In the same terminal**, run

```
   docker run -t -i --rm --privileged --cap-add=NET_ADMIN --name ceng435vm -v ./code:/app:rw ceng435:latest bash
```

and you will be in your virtual Ubuntu 22.04 machine (python installed). Note that if you develop code in this virtual machine, if you stop the machine your code will be lost. That is why I recommend you to use Github to store your code and clone in the machine, and push your code to Github before shutting the virtual machine down. The other option is to work in the /app folder in your virtual machine which is mounted to the "code" directory of your own machine...

**In another terminal** to attach to the same container, run

```
docker exec -it ceng435vm bash`
```

These two terminal will help you run your client and server applications.

After running the Ubuntu VM, you can type "ifconfig -a" to see your network configuration. Work on eth0.

Docker extension of vscode will be of great benefit to you.

In the server terminal, move to the objects folder and run

```
   chmod +x generateojects
   ./generateobjects
```

Some tc commands that may be of help to you can be found at https://man7.org/linux/man-pages/man8/tc-netem.8.html

**IMPORTANT** Note that the "code" folder on your local machine is mounted to the "/app" folder in the virtual machine (read/write mode). You can use these folders (they are the same in fact) to develop your code. Other than the /app folder this tool does not guarantee any persistent storage: if you exit the virtual machine, all data will be lost.



