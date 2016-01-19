# Hardware

E.g. AWS Ubuntu 14.04

# Set up environment

ssh -i IDENTITY ubuntu@HOST
sudo apt-get update
sudo apt-get install -y ansible git python-dev
git clone https://github.com/ksnavely/website.git
sudo ln -s /home/ubuntu/website/website /srv/website/website

# Run playbook
cd ~/website
git pull --rebase origin master
sudo ansible-playbook -v -c local -i ansible/hosts ansible/playbook.yml
