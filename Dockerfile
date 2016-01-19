FROM ansible/ubuntu14.04-ansible:stable

MAINTAINER Kyle Snavely

ADD website /srv/website/website
ADD ansible /srv/ansible
WORKDIR /srv/ansible

RUN ansible-playbook playbook.yml -c local -v -i hosts

EXPOSE 22 80 5000

ENTRYPOINT ["/srv/website/docker_start.sh"]
