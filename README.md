# website

This repo holds a web application stack I use for managing my website. I chose
a stack based on Docker, Ansible, Nginx, and Python Flask is used. Some hooks
for Vagrant are also included.

## Stack

I've strived to pick the right tool for the job at each layer of the stack.
Also, I've only used open source projects. Sweet! Each element here is
powerful enough to be used in production. If we make the base web-bit stateless
or otherwise able to be distributed, we can easily scale the whole
service/website.

### Flask

I picked [Flask](http://flask.pocoo.org/) because it's dead simple to use, and
yet can support a complex web application.

### Nginx

Nginx is used as an HTTP proxy layer. It's very lightweight with a large body
of information online around configuration.

### Ansible

After my professional experience with Chef I feel in love with configuration
management. Ansible is used here because it's Python (neato) and simple
Ansible playbooks can do quite a bit of heavy lifting. It's very easy to get
started.

### Docker

Containers are still new to me, but are quickly taking the development world
by storm. Being DevOps, the idea of immutable infrastructure is greatly
appealing to me. Docker has a pretty good online community and a simple
Dockerfile and start-script were all that was needed to put the web app
stack together in a container.

### Vagrant

Alongside the ansible playbook you'll also find a short VagrantFile. This can
be used to play with the stack with having to jump into Docker. However, I'm
now using Docker for local development too and the VF is not guaranteed to
be up to day.
