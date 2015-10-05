FROM ansible/ubuntu14.04-ansible:stable

MAINTAINER Kyle Snavely

ADD website /srv/website/website
ADD ansible /srv/ansible
WORKDIR /srv/ansible

RUN ansible-playbook playbook.yml -c local

EXPOSE 22 80

ENTRYPOINT ["/bin/bash"]
