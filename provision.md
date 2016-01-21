# Provisioning

This brief guide will serve as notes and work towards an actual provisioning script or ansible setup.
For the moment, we choose the paradigm of running ansible playbooks locally on the machine to be used.


## Acquire Hardware

Acquire a machine online somewhere. They only thing you will need is ssh access.

E.g. AWS Ubuntu 14.04.


## Bootstrap the system for ansible and the site

After fetching the box, these few steps should prepare the machine to run the web stack.
One can see we'll run it right out of a repo clone.

```
ssh -i IDENTITY ubuntu@HOST
sudo apt-get update
sudo apt-get install -y ansible git python-dev
git clone https://github.com/ksnavely/website.git
sudo ln -s /home/ubuntu/website/website /srv/website/website
```


## Run playbook

If you have the system set up, you can go ahead and start or update the machine's web service with:
```
cd ~/website
git pull --rebase origin master
cd ansible
sudo ansible-playbook -v -c local -i hosts website.yml
```
