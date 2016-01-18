ssh -i IDENTITY ubuntu@HOST
sudo apt-get install -y ansible git python-dev
git clone https://github.com/ksnavely/website.git
deal with ansible hosts config?
 - added localhost
pinned nginx and runit versions, geez
sudo ln -s . /srv/website/website
sudo ln -s /home/ubuntu/website/website /srv/website/website
set modes to 06400
perms are off, set to 0764
turned off some default nginx noise? sv stop, fix, sv start
sudo ansible-playbook -v -c local playbook.yml -- refresh state
