# Argus - Helm Chart

![Version: 0.2.1](https://img.shields.io/badge/Version-0.2.1-informational?style=flat-square&logo=helm)

An automated security checking platform that is highly extensible.

**Homepage:** <https://github.com/WatcherWhale/SecProA>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| https://charts.bitnami.com/bitnami | redis | 16.8.5 |
| https://smallstep.github.io/helm-charts/ | autocert | 1.16.3 |

## Values

### App

General app settings/metadata.
| Key | Type | Default | Description |
|-----|------|---------|-------------|
| app.host | string | `"argus.local"` | The hostname used in the ingress. |
| app.name | string | `"argus"` | The name of the deployment. |

### Autoscaling

Autoscaling configuration.
| Key | Type | Default | Description |
|-----|------|---------|-------------|
| autoscaling.enabled | bool | `true` | Enable/Disable autoscaling. |
| autoscaling.tag | string | `"v1.0.0"` | The image tag for the custom pod autoscaler. |

### Checklists

A list of all available checklists that you are able to deploy. If desired, it is possible to add your own checks here. <br> Default available checklists: `cookie`, `dns`, `headers`, `https`, `ip` and `mail`.
| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | Affinity for pod assignment. |
| annotations | object | `{}` | Deployment annotations. |
| env | object | `{}` | Custom environment variables to add to the checklist. |
| interval | int | `10000` | The throughput interval, the interval to periodically check the current queue size (in ms). |
| nodeSelector | object | `{}` | Node Labels for pod assignment. |
| podAnnotations | object | `{}` | Pod annotations. |
| replicas.max | int | `5` | Maximum replicas. |
| replicas.min | int | `1` | Minimum replicas. |
| stabilization | int | `200` | The stabilization interval, used for down scaling (in s). |
| tag | string | `"v1.0.0"` | The image tag of the checklist container. |
| throughput | int | `100` | Check throughput. <br> The amount of request the checklist can handle in a specified interval. |
| tolerations | list | `[]` | Tolerations for pod assignment. |

### Image

Container image settings.
| Key | Type | Default | Description |
|-----|------|---------|-------------|
| image.imagePullSecrets | list | `[{"name":"ghcr-io"}]` | A list of image pull secrets to use. <br> Docker credentials secrets. |
| image.pullPolicy | string | `"IfNotPresent"` | Default pullPolicy. |
| image.registry | string | `"ghcr.io/watcherwhale"` | The image registry to use. |

### Redis

Bitnami Redis configuration. <br> See https://github.com/bitnami/charts/tree/master/bitnami/redis for more config options.
| Key | Type | Default | Description |
|-----|------|---------|-------------|
| redis.auth | object | `{"enabled":true,"sentinel":true}` | Authentication settings. |
| redis.master | object | `{"persistence":{"enabled":false}}` | Master settings. |
| redis.replica.replicaCount | int | `3` | Amount of replicas. |
| redis.sentinel.enabled | bool | `true` | Enable/Disable sentinels. <br> Must be enabled, to work correctly. |

### Security

Security Settings.
| Key | Type | Default | Description |
|-----|------|---------|-------------|
| security.cluster.tls | bool | `false` | Enable mTLS & TLS throughout the cluster. |
| security.ingress.caSecret | string | `"argus-ca"` | The CA Certificate secret. |
| security.ingress.clientAuth | bool | `true` | Enable mTLS at the ingress. |
| security.ingress.tlsSecret | string | `"argus-tls"` | The TLS secret for https. |

### Selenium

The Selenium deployment configuration.
| Key | Type | Default | Description |
|-----|------|---------|-------------|
| selenium.affinity | object | `{}` | Affinity for pod assignment. |
| selenium.enabled | bool | `true` | Enable the Selenium deployment. |
| selenium.nodeSelector | object | `{}` | Node Labels for pod assignment. |
| selenium.replicas.max | int | `5` | Maximum node replicas. |
| selenium.replicas.min | int | `1` | Minimum node replicas. |
| selenium.tag | string | `"latest"` | The selenium hub/Chrome image tag. |
| selenium.tolerations | list | `[]` | Tolerations for pod assignment. |

### Services

Configuration for all services.

#### Cert-Master

Cert-master service configuration. Only necessary when `security.cluster.tls` is enabled.

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | Affinity for pod assignment. |
| annotations | object | `{}` | Deployment annotations. |
| basePath | string | `"/api/v1/certificate"` | Base path of the service. |
| env | object | `{}` | Custom environment variables to add to the service. |
| loglevel | string | `"info"` | Log level. (`silly`, `debug`, `verbose`, `http`, `info`, `warn`, `error`) |
| nodeSelector | object | `{}` | Node Labels for pod assignment. |
| podAnnotations | object | `{}` | Pod annotations. |
| replicas.max | int | `10` | Maximum replicas. |
| replicas.min | int | `1` | Minimum replicas. |
| resources | object | Kuberenetes resource config. | Pod resources. |
| securityContext | object | `{}` | Pod security context. |
| tag | string | `"v1.0.0"` | Image tag. |
| tolerations | list | `[]` | Tolerations for pod assignment. |

#### Descriptions

Descriptions service configuration.

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | Affinity for pod assignment. |
| annotations | object | `{}` | Deployment annotations. |
| basePath | string | `"/descriptions"` | Base path of the service. |
| env | object | `{}` | Custom environment variables to add to the service. |
| nodeSelector | object | `{}` | Node Labels for pod assignment. |
| podAnnotations | object | `{}` | Pod annotations. |
| replicas.max | int | `10` | Maximum replicas. |
| replicas.min | int | `1` | Minimum replicas. |
| resources | object | Kuberenetes resource config. | Pod resources. |
| securityContext | object | `{}` | Pod security context. |
| tag | string | `"v1.0.0"` | Image tag. |
| tolerations | list | `[]` | Tolerations for pod assignment. |

#### Gateway

Gateway service configuration.

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | Affinity for pod assignment. |
| annotations | object | `{}` | Deployment annotations. |
| basePath | string | `"/api/v1/checks"` | Base path of the service. |
| env | object | `{}` | Custom environment variables to add to the service. |
| loglevel | string | `"info"` | Log level. (`silly`, `debug`, `verbose`, `http`, `info`, `warn`, `error`) |
| nodeSelector | object | `{}` | Node Labels for pod assignment. |
| podAnnotations | object | `{}` | Pod annotations. |
| replicas.max | int | `10` | Maximum replicas. |
| replicas.min | int | `1` | Minimum replicas. |
| resources | object | Kuberenetes resource config. | Pod resources. |
| securityContext | object | `{}` | Pod security context. |
| tag | string | `"v1.0.0"` | Image tag. |
| tolerations | list | `[]` | Tolerations for pod assignment. |

#### Metrics

Metrics service configuration.

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | Affinity for pod assignment. |
| annotations | object | `{}` | Deployment annotations. |
| basePath | string | `"/api/v1"` | Base path of the service. |
| env | object | `{"SELENIUM_URL":"http://selenium-hub:4444"}` | Custom environment variables to add to the service. |
| loglevel | string | `"info"` | Log level. (`silly`, `debug`, `verbose`, `http`, `info`, `warn`, `error`) |
| nodeSelector | object | `{}` | Node Labels for pod assignment. |
| podAnnotations | object | `{}` | Pod annotations. |
| replicas.max | int | `10` | Maximum replicas. |
| replicas.min | int | `1` | Minimum replicas. |
| resources | object | Kuberenetes resource config. | Pod resources. |
| securityContext | object | `{}` | Pod security context. |
| tag | string | `"v1.0.0"` | Image tag. |
| tolerations | list | `[]` | Tolerations for pod assignment. |

#### Sequencer

Sequencer service configuration.

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | Affinity for pod assignment. |
| annotations | object | `{}` | Deployment annotations. |
| basePath | string | `"/api/v1"` | Base path of the service. |
| env | object | `{}` | Custom environment variables to add to the service. |
| loglevel | string | `"info"` | Log level. (`silly`, `debug`, `verbose`, `http`, `info`, `warn`, `error`) |
| nodeSelector | object | `{}` | Node Labels for pod assignment. |
| podAnnotations | object | `{}` | Pod annotations. |
| replicas.max | int | `10` | Maximum replicas. |
| replicas.min | int | `1` | Minimum replicas. |
| resources | object | Kuberenetes resource config. | Pod resources. |
| securityContext | object | `{}` | Pod security context. |
| tag | string | `"v1.0.0"` | Image tag. |
| tolerations | list | `[]` | Tolerations for pod assignment. |

## Source Code

* <https://github.com/WatcherWhale/SecProA>

## Chart Maintainers

| Name | GitHub |
| ---- | ------ |
| Mathias Maes | [https://github.com/WatcherWhale](https://github.com/WatcherWhale)
| Cato van Hooijdonk | [https://github.com/vanHooijdonkC](https://github.com/vanHooijdonkC)
