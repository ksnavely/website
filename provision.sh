ssh -i IDENTITY ubuntu@HOST
sudo apt-get update
sudo apt-get install -y ansible git python-dev
git clone https://github.com/ksnavely/website.git
sudo ansible-playbook -v -c local -i website/ansible/hosts website/ansible/playbook.yml

deal with ansible hosts config?
 - added localhost

sudo ln -s . /srv/website/website
sudo ln -s /home/ubuntu/website/website /srv/website/website

turned off some default nginx noise? sv stop, fix, sv start


# Refresh state
git pull --rebase origin master
sudo ansible-playbook -v -c local playbook.yml
