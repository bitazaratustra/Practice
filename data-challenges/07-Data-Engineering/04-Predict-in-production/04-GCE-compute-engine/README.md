
## Objective

Use **Compute Engine** in order to play with a virtual machine in the cloud.

Go through the **Le Wagon Setup** on your virtual machine in order to code and build Docker images in the cloud.

## Context

This exercise is optional.

Do you have a internet connection with a limited bandwitdh or does your computer suffer in any way when building Docker images? Let's use Google Compute Engine in order to have a server in the cloud do the hard work for us.

The goal here is do demonstrate the usage of a **Google Compute Engine** instance.

Google Compute Engine allows to create **Virtual Machines** (VM) in the cloud. You can think of a virtual machine as your laptop in the cloud. The machine remains **ON** as long as you do not turn it **OFF** even if it is doing no actual work - just like your machine ☕️

Why would you want to use a virtual machine (VM) ?
- The VM in the cloud has access to a **top notch internet** connection, while you might not. You may want to have it perform network intensive tasks, such as building **Docker** images and for example pushing them to **Google Container Registry**
- You will be able to play with machines up to **160 VCPU and 3.75TB of memory** 😱

However, using monstrous amounts of processing power comes at a cost 💸

⚠️ If you are playing with this exercise, make sure to **STOP** the virtual machine as soon as you are done ⚠️

Also, keep an eye on the [billing in the GCP console](https://console.cloud.google.com/billing).

If you choose the default virtual machine size, the cost should be very light. But anyways, remember to stop the virtual machine once you are done working on it.

In order to play with a VM, first we need to configure it, select an operating system, install the python stack, and a developer environment. You can think of this step as building a dedicated Docker image that will only get instantiated into a single Docker container. This is an analogy, the **VM** do not use Docker at all.

But wait... Configuring a machine with a developer environment... We already did that! 💡 That is the **Le Wagon data setup**! 👌

In this exercise we will configure a VM instace, run the Le Wagon data setup on it. Then we will see how to drive it 🚀

## Create a Compute Engine instance

We are going to create a virtual machine based on a [Debian](https://en.wikipedia.org/wiki/Debian) (Linux) operating system.
We will be able to use this machine in order to build Docker image or even train models.

Go to the [Google Cloud Platform console](https://console.cloud.google.com/).

In Compute Engine / VM instances, select CREATE INSTANCE:
- Name: instance-name
- Region: europe-west1 (Belgium)
- Allow HTTP traffic
- Allow HTTPS traffic
- Create

We now have a machine that needs to be turned on and off when it is not used.

⚠️ Keep in mind that you pay for the machine as long as it is up 💸

## Run Le Wagon data setup

Now that we have a machine, let's configure it using the [Le Wagon Data Setup](https://github.com/lewagon/data-setup/blob/master/LINUX.md).
Since Debian is a [Linux distribution](https://en.wikipedia.org/wiki/Linux_distribution), we will run the Linux setup.

The virtual machine does not have a graphical user interface such as the ones that MacOS, Linux or Windows propose.
But we can connect to it remotely and execute command lines using [SSH](https://en.wikipedia.org/wiki/SSH_(Secure_Shell)).
SSH is a secure protocol allowing us to connect to a machine remotely and to run a remote command line shell.

Let's connect to the machine.

Connect
- click on SSH

### Git

Let's install git.

``` bash
sudo apt install -y git
```

### Oh-my-zsh

Install your favorite shell: leave the root password blank.

``` bash
sudo apt install -y zsh curl vim
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

### GitHub

Now we will generate a new public private key pair in order to allow the machine to access to your GitHub account.
This will allow us to clone your project on the machine and even push code from the machine to your repositories.

``` bash
mkdir -p ~/.ssh && ssh-keygen -t ed25519 -o -a 100 -f ~/.ssh/id_ed25519 -C "TYPE_YOUR_EMAIL@HERE.com"
cat ~/.ssh/id_ed25519.pub
```

Once the key are generated, let's copy the public key [to your GitHub account](https://github.com/settings/keys).

In your account settings
- SSH and GPG keys
- New SSH key
- Title
- Key: replace the email if you did not previously

You can now make sure that the key is correctly configured by running:

``` bash
ssh -T git@github.com
```

### Dotfiles

We will now proceed will the automated part of the Le Wagon Data setup.

⚠️ Do not forget to replace `username` with your GitHub account username in the following command

``` bash
export GITHUB_USERNAME=username
```

``` bash
mkdir -p ~/code/$GITHUB_USERNAME && cd $_ && git clone git@github.com:$GITHUB_USERNAME/dotfiles.git
cd ~/code/$GITHUB_USERNAME/dotfiles
zsh install.sh
cd ~/code/$GITHUB_USERNAME/dotfiles
zsh git_setup.sh
```

We will now edit your [zsh](https://en.wikipedia.org/wiki/Z_shell) ressource file using [vim](https://en.wikipedia.org/wiki/Vim_(text_editor)).
This might proove to be quite an adventure since vim uses an old school graphical interface 😱
Here are a few commands that will help you along the way...

Remember the specific way your [Jupyter Notebook](https://jupyter.org/) has to allow you to edit cells ?
When you press `Esc`, you enter the `Command Mode` (the cells are highlighted in blue), and you are able to insert cells above (`A`) or below (`B`) the current cell.
Then when you press `Enter` on a specific cell, you enter the `Edit Mode` (the cells are highlighted in green), and you can type markdown or code in the cell...

Well this behavior is pretty oldschool, and is actually the way vim works.
Please note that vim also features a third mode: the `Escape Mode` 😨

Here are the rules of the vim club 🤺:
- you start in `Command mode`
- press `i` and enter `Edit Mode`
- type in whatever you need, pasting text even works with your favourite shortcut
- once you are done editing, press `Esc` to go back to the `Command Mode`
- you are now about to enter the dreaded `Escape Mode`: take a deep breath and press `:`
- type to tell vim to save your file and let you exit: press `wq` then `Enter`

Press anything else or in any other order, and you will be [on your own](https://www.geeksforgeeks.org/vi-editor-unix/)... 😉

We will now use this new skill in order to add a few characters to our zsh ressource file.
You may have crossed the path of this file already. The `.zshrc` is the file, located in your home, that gets executed every time you open a new terminal window.
This is the file responsible for activating your python virtual environment on each new window.

``` bash
vi ~/.zshrc
```

Add the following line before the line `# Actually load Oh-My-Zsh`:

``` bash
ZSH_DISABLE_COMPFIX=true
```

Modify the following line (add `git` and `ssh-agent`):

``` bash
plugins=(git gitfast last-working-dir common-aliases sublime zsh-syntax-highlighting history-substring-search ssh-agent)
```

You're done! 🏅

### Python

Let's add a few missing libraries

``` bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

``` bash
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
  libreadline-dev libsqlite3-dev llvm libncurses5-dev libncursesw5-dev \
  xz-utils tk-dev libffi-dev liblzma-dev python-openssl
```

And we will proceed with the regular python setup

## Complete python setup

With the help of [this article](https://www.programmersought.com/article/12164671542/)...

``` bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt-get install build-essential python-dev python-setuptools python-pip python-smbus
sudo apt-get install build-essential libncursesw5-dev libgdbm-dev libc6-dev
sudo apt-get install zlib1g-dev libsqlite3-dev tk-dev
sudo apt-get install libssl-dev openssl
sudo apt-get install libffi-dev
```

An [this one](https://www.cyberciti.biz/faq/debian-linux-install-gnu-gcc-compiler/)...

``` bash
sudo apt-get update
sudo apt-get install build-essential
sudo apt-get install gcc
```

Let's make sure everything is in order:

``` bash
whereis gcc make
```

And check the installed versions of [gcc](https://en.wikipedia.org/wiki/GNU_Compiler_Collection) and make (remember the `Makefiles` ?)

``` bash
gcc -v
make -v
```

## Resume Le Wagon data setup

### Python

Let's create a new shell (so that the `~/.zshrc` gets executed and our python virtual environment gets activated).

``` bash
/bin/zsh
```

Let's install python 3.8.5...

``` bash
pyenv install 3.8.5
pyenv global 3.8.5
```

``` bash
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
```

And create our python virtual environment...

``` bash
pyenv virtualenv 3.8.5 lewagon
```

``` bash
/bin/zsh
```

``` bash
pyenv activate lewagon
```

``` bash
pip install --upgrade pip
pip install pytest pylint ipdb pyyaml
pip install requests bs4
pip install jupyterlab pandas matplotlib seaborn plotly scikit-learn
```

## Install Docker

Now we will install `Docker` thanks to [this article](https://tomroth.com.au/gcp-docker/)...
And we will be able to build images in the cloud! 🤘

``` bash
sudo apt update
sudo apt install --yes apt-transport-https ca-certificates curl gnupg2 software-properties-common
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
sudo apt update
sudo apt install --yes docker-ce
sudo usermod -aG docker $USER
```

All docker commands still require sudo (in order to be executed as root).

## Change root password to get zsh by default

``` bash
sudo passwd
```

Set the default shell to /bin/zsh (for Oh My Zsh).

``` bash
sudo chsh
```

## New connection

``` bash
/bin/zsh
```

## Conclusion

You might notice that you need to type `exit` a few times before the ssh window closes.
This is because we have been working in a zsh shell inside of a zsh shell inside of a...

You are now able to switch on a machine on which you will be able to build docker images even if your internet connection is very slow.
All the layers required in order to build the image will not need to transit through your machine in order for the image to build in the VM 👍

Thanks Compute Engine 🎸

⚠️ Again, keep in mind that you are paying for the VM as long as it remains up 💸
