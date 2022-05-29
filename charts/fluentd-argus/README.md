# Argus Fluentd - Helm Chart

![Version: 1.0.0](https://img.shields.io/badge/Version-1.0.0-informational?style=flat-square&logo=helm)

The fluentd config that is tailored for argus.

**Homepage:** <https://github.com/WatcherWhale/SecProA>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| config | string | Fluentd config | A custom fluentd config to add to the deployment. |
| env | list | `[]` | Extra environment variables for fluentd pods. |
| image | string | `"fluent/fluentd-kubernetes-daemonset"` | The fluentd image to use |
| tag | string | `"v1-debian-elasticsearch"` | The image tag to use |

## Source Code

* <https://github.com/WatcherWhale/SecProA>

## Chart Maintainers

| Name | GitHub |
| ---- | ------ |
| Mathias Maes | [https://github.com/WatcherWhale](https://github.com/WatcherWhale)
| Cato van Hooijdonk | [https://github.com/vanHooijdonkC](https://github.com/vanHooijdonkC)
| Dimitriy Vassilchenko | [https://github.com/calle987](https://github.com/calle987)
| Arash Nouri | [https://github.com/arash-nouri-1](https://github.com/arash-nouri-1)
