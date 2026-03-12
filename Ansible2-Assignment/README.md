# Ansible Web Server Automation

## Author
Nirmalya Das

---

# Project Overview

This project demonstrates how Ansible can automate the installation and configuration of a web server.

The playbook installs Nginx, starts the service, and deploys a custom webpage automatically.

---

# Tools Used

| Tool | Purpose |
|-----|------|
| Ansible | Configuration Management |
| Ubuntu | Operating System |
| Nginx | Web Server |
| YAML | Playbook Language |

---


# Inventory Configuration

```
[webservers]
localhost ansible_connection=local
```

---

# Playbook

```yaml
---
- name: Setup nginx web server
  hosts: webservers
  become: yes

  tasks:

    - name: Install nginx
      apt:
        name: nginx
        state: present

    - name: Start nginx
      service:
        name: nginx
        state: started
        enabled: yes

    - name: Deploy custom webpage
      copy:
        dest: /var/www/html/index.html
        content: "<h1>Web Server Configured using Ansible</h1>"
```

---

# Run Playbook

```
ansible-playbook webserver_setup.yml --ask-become-pass
```

---

# Verify Deployment

```
curl localhost
```

or open browser:

```
http://localhost
```

---

# Conclusion

This project demonstrates how Ansible playbooks can automate web server setup and configuration, enabling faster and more reliable infrastructure provisioning.