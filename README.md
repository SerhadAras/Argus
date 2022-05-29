<h1 align="center">
    <img src = "./.images/Argus.png" align = "center" height = 200px>
    <br>
    <a href="https://www.gnu.org/licenses/gpl-3.0"><img src="https://img.shields.io/badge/License-GPLv3-blue.svg"> </a>
</h1>


> Argus: the "all-seeing" primordial giant

<br>

Argus was a responsibility given to the students of "Security Project", a course at AP Hogeschool. <br>
The idea is to create a highly available, agile platform to execute checks that control a given domain or ip address.
We realised this by using different microservices that can be easily deployed with ansible scripts and dockerfiles.
A high selling point of our platform is the use of a Kubernetes cluster, which ensures the autoscaling of all services. <br>
This project is created with a security mindset, but can be used for other (non-security) purposes. The principle of "plug 'n play" is a definite here,
just remove / add / replace the checks with your own scripts and you're good to go.<br>
For more details about what lives in the environment, we refer you to our [wiki page](https://github.com/WatcherWhale/SecProA/wiki).<br>

<br>

## Available Checklists
A list of all checklists included:
| Name          | Description    |
| ------------- | -------------- |
| IP            | Does the GEOIP test, checks if ipv6 is supported and runs your ip against blocklists. |
| DNS           | Checks if DNSSEC is present and enabled. |
| Mail          | Gives scores based on the presence of 3 specific records: DKIM, DMARC AND SPF.|
| HTTPS         | Checks if there is a redirection from http to https, if there is a valid certificate present and what TLS version is supported. |
| Cookie        | Checks the website for illegal use of third party cookies according to the GDPR. |
| Headers       | Reads the headers looking for faulty or absent security headers. |
| Vulnerability | Looks for critical infrastructure on the outside with shodan and checks if there are CVEs found on the outside of the domain. |

<br>

## Getting Started

Ready to integrate our platform with your infrastructure or just to see if it's something you need? <br>
Everything you need to know for this will be in our [Getting Started](https://github.com/WatcherWhale/SecProA/wiki) page in the Arguswiki.


<br><br><br>
#
<p align = "center">
    Powered by
    <p align= "center">
        <a href="https://redis.io/"> <img src="https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white"> </a>
        <a href="https://kubernetes.io/"> <img src="https://img.shields.io/badge/kubernetes-326ce5.svg?&style=for-the-badge&logo=kubernetes&logoColor=white"> </a>
        <a href="https://www.docker.com/"> <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white"> </a>
        <a href="https://www.ansible.com/"> <img src="https://img.shields.io/badge/Ansible-000000?style=for-the-badge&logo=ansible&logoColor=white"></a>
        <a href="https://expressjs.com/"> <img src="https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white"> </a><br>
        <a href="https://www.npmjs.com/"> <img src="https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white"></a>
        <a href="https://nodejs.org/en/"> <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white"></a>
        <a href="https://www.javascript.com/"> <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E"></a>
        <a href="https://www.python.org/"> <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"></a><br>
        <a href="https://eslint.org/"> <img src="https://img.shields.io/badge/eslint-3A33D1?style=for-the-badge&logo=eslint&logoColor=white"></a>
        <a href="https://alpinelinux.org/"> <img src="https://img.shields.io/badge/Alpine_Linux-0D597F?style=for-the-badge&logo=alpine-linux&logoColor=white"></a>
    </p>
</p>