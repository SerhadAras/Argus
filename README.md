
<h1 align="center">
    <img src = "./.images/onetrustLogo.png" align = "center" height = 200px> <br> <br>
    HowSamI
</h1>

> How Safe am I? Really?

HowSamI was a responsibility given to the students of "Security Project", a course at AP Hogeschool.  
The idea is to create a highly available, agile platform to execute checks that control a given domain.  
We realised this by using different microservices that can be easily deployed with ansible scripts and dockerfiles.  
A high selling point of our platform is the use of a Kubernetes cluster, which ensures the autoscaling of all services.  
This project is created with a security mindset, but can be used for other (non-security) purposes. The principle of "plug 'n play" is a definite here, just remove / add / replace the checks with your own scripts and you're good to go.
For more details about what lives in the environment, we refer you to our [wiki page](https://github.com/WatcherWhale/SecProA/wiki).  


<!-- ## Getting started

### prerequisites
To be able to set up the environment, make sure you have installed [Docker](https://www.docker.com) on you machine.  
### Environment -->


## Available checks
A list of all checks included:
| Name         | Description                                                           |
| ------------ | --------------------------------------------------------------------- |
| IP           | Does the GEOIP test and checks if ipv6 is supported.                  |
| DNS          | Checks if DNSSEC is present and enabled.                              |
| Mail         | Gives a score based on the presence of 3 specific records.            |
| Https        | Checks if there is a redirection from http to https.                  |
|              |                                                                       |


## Developing
### Libraries
A list of the libraries used in this project:
| Library             | Version      |
| ------------------- | ------------ |
| IoRedis             | 4.28.5       |
| Express             | 4.17.3       |
| Redlock             | 5.0.0-beta.1 |
| Winston             | 3.6.0        |
| Morgan              | 1.10.0       |


<br><br><br>
#
<p align = "center">
    Powered by
    <p align= "center">
        <img src="https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white">
        <img src="https://img.shields.io/badge/kubernetes-326ce5.svg?&style=for-the-badge&logo=kubernetes&logoColor=white">
        <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white">
        <img src="https://img.shields.io/badge/Ansible-000000?style=for-the-badge&logo=ansible&logoColor=white">
        <img src="https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white"> <br>
        <img src="https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white">
        <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white">
        <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E">
        <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"><br>
        <img src="https://img.shields.io/badge/eslint-3A33D1?style=for-the-badge&logo=eslint&logoColor=white">
        <img src="https://img.shields.io/badge/Alpine_Linux-0D597F?style=for-the-badge&logo=alpine-linux&logoColor=white">
    </p>
</p>