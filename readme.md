# MITB Cloud Computing Lab for Google App Engine development and CI with Koding and Travis-CI

This tutorial will cover the steps for using a virtual maching (VM) on [koding.com](https://koding.com) to code python web apps and use Travis-CI as a test and deploy tool to push updates to Google App Engine. This tutorial will also allow you to push 'static' files (e.g. HTML, JavaScripts etc.) to the GitHub pages brance of your repository

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
<pre>
  <code>
# Default GitHub user
 Host github.com
 HostName github.com
 PreferredAuthentications publickey
 IdentityFile ~/.ssh/koding_id_rsa
  </code>
</pre> 


## Clone and Configure Demo App

1. Clone this repository `git clone https://github.com/andrewbeng89/mitb_gae_demo.git`
2. `cd mitb_gae_demo`
3. Reomve the .git directory `rm -rf .git`
4. Create a new GitHub repository with your account
5. Initialise the demo app as a git repo on the VM `git init`
6. Add the remote to the newly create GitHub repository `git remote add origin git@github.com:<your_username>/<your_new_repo>.git`
7. Create a new GAE application [here](https://appengine.google.com/)
8. Open the app.yaml file and edit the following line: `application: <new-gae-app-id>`


## First Deploy to GAE

The very first deployment to GAE has to be made from the Koding VM in order to retrieve the OAuth2 refresh_token which Travis-CI will use later

1. From the VM terminal, enter `appcfg.py --noauth_local_webserver --oauth2 update ./`
2. A link will be displayed, followed by a promt to enter an access code. Open the link in a new browser tab and allow Google to grant access. Copy the access code displayed to the clipboard
3. Paste the access code in the VM terminal and hit return
4. Open the .appcfg_oauth2_tokens (JSON) file and copy the value of the refresh_token field
5. Remove this line from the .travis.yml file `secure: <existing secure token>`
6. Encrypt this token as a secure global variable in the .travis.yml file `travis encrypt MY_GAE_TOKEN="<paste_token_from_clipboard>" --add -r <your_github_username/your_github_repo>`
7. Check the .travis.yml file to see whether the new secure variable has been added


## Add GitHub Personal API Access Token

1. Create a new Personal API Access Token [here](https://github.com/settings/applications)
2. Copy the token to clipboar and encrypt it with travis
3. `travis encrypt MT_GITHUB_TOKEN="<paste_token from_clipboard>" --add -r <your_github_username/your_github_repo>`
4. Edit this line of the .travis.yml file: `- git push https://$MY_GITHUB_TOKEN@github.com/<your_username>/<your_repo>.git gh-pages`


## Setup and Build with Travis-CI

1. Register for [Travis-CI](https://travis-ci.org) using your GitHub account
2. From your Travis-CI [profile](https://travis-ci.org/profile) page, enable the newly created GitHub repository
3. Edit this line of the .travis.yml file: `- git clone https://github.com/<your_username>/<your_repo>.git deploy`
4. Add all file and folders `git add -A .`
5. Commit with message `git commit -a -m 'created GAE project'`
6. Push the update `git push origin master`
7. You can track the build progress at the Travis-CI website

* updated to include public folder push to gh-pages branch
* coming soon: challenging tasks