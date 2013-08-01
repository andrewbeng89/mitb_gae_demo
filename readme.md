mitb_gae_demo
=============

# MITB Cloud Computing Lab for Google App Engine development and CI with Koding and Travis-CI

This tutorial will cover the steps for using a virtual maching (VM) on [koding.com](https://koding.com) to code python web apps and use Travis-CI as a test and deploy tool to push updates to Google App Engine.

Once you have signed up and received an invitation for Koding.com, you will have access to a persional Koding VM. Open the terminal shell of your VM which will look like this:

![koding terminal](/images/koding_vm.png)


## Install Travis Ruby Gem

The Travi-CI gem will be used to encrypt a OAuth2 token that will be used to push updates to Google App Engine from the Travis build.

1. From the terminal, install the gem by entering `sudo gem install travis`
2. Enter your Koding password when prompted


## Install Google App Engine - Python

The Google App Engine python SDK is required to retrieve the OAuth2 token which will be encrypted by travis

1. From the terminal, download the GAE python SDK `wget http://googleappengine.googlecode.com/files/google_appengine_1.8.2.zip`
2. Unzip `unzip google_appengine_1.8.2.zip`
3. `rm google_appengine_1.8.2.zip`
4. Move GAE sdk to lib `sudo mv google_appengine /lib/`
5. `cd /bin/`
6. Create symbolic links to GAE modules `ln -s ../lib/google_appengine/*.py .`
7. `cd ~/`


## Configuring Git and GitHub

Generate a new ssh key pair on the VM to use to sync with GitHub and Travis-CI.

1. Follow the instructions [here](https://help.github.com/articles/generating-ssh-keys)
2. When "Enter file in which to save the key (/home/you/.ssh/id_rsa):" is prompted, enter  `/home/<you>/.ssh/koding_id_rsa`
3. Once the key pair has been generated, open the public key koding_id_rsa.pub using the ACE editor
4. Copy the public key and add it to your [GitHub keys](https://github.com/settings/ssh) with a new key name, e.g. koding.com
5. Create a new config file in the .ssh folder and enter these lines below:
```text
# Default GitHub user
Host github.com
 HostName github.com
 PreferredAuthentications publickey
 IdentityFile ~/.ssh/koding_id_rsa
```