The [all-partners.yaml](all-partners.yaml) file includes all partner allowlist paths listed in the docs:
https://cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners#allowlisted-partner-workloads

It effectively allows the [installation of partner software](https://cloud.google.com/kubernetes-engine/docs/how-to/run-autopilot-partner-workloads) in the new Autopilot workload allowlist system, and is also useful to see how the workloadallowlist resources are configured.

Create the AllowlistSynchronizer with all known allowlist paths:
```
kubectl create -f all-partners.yaml
```
or
```
kubectl create -f https://raw.githubusercontent.com/WilliamDenniss/autopilot-examples/refs/heads/master/workloadallowlist/all-partners.yaml
```

Wait for the AllowlistSynchronizer to be ready:
```
$ kubectl get AllowlistSynchronizer
NAME           READY   LASTSYNC
all-partners   True    117s
```

This causes GKE Autopilot to download CRDs of type WorkloadAllowlist that were supplied by the partners.

Then, you can view individual WorkloadAllowlists to see their config.

List all WorkloadAllowlists:
```
$ kubectl get workloadallowlist
NAME                                                  AGE
crowdstrike-falconsensor-cleanup-allowlist-v1.0.0     2m19s
crowdstrike-falconsensor-cleanup-allowlist-v1.0.1     2m19s
crowdstrike-falconsensor-cleanup-allowlist-v1.0.2     2m19s
crowdstrike-falconsensor-deploy-allowlist-v1.0.0      2m19s
crowdstrike-falconsensor-deploy-allowlist-v1.0.1      2m19s
crowdstrike-falconsensor-deploy-allowlist-v1.0.2      2m19s
crowdstrike-falconsensor-falconctl-allowlist-v1.0.0   2m19s
crowdstrike-falconsensor-falconctl-allowlist-v1.0.1   2m19s
datadog-datadog-daemonset-exemption-v1.0.0            2m18s
datadog-datadog-daemonset-exemption-v1.0.1            2m18s
dynatrace-csidriver-v1.4.1                            2m18s
dynatrace-csidriver-v1.4.2                            2m18s
dynatrace-csidriver-v1.5.0                            2m18s
dynatrace-csijob-v1.5.0                               2m18s
dynatrace-logmonitoring-v1.4.1                        2m18s
dynatrace-logmonitoring-v1.4.2                        2m18s
dynatrace-logmonitoring-v1.5.0                        2m18s
orca-security-orca-sensor-v1.0.0                      2m17s
orca-security-orca-sensor-v1.1.0                      2m17s
orca-security-orca-sensor-v1.2.0                      2m17s
palo-alto-networks-prisma-cloud-defender-v1.0.0       2m17s
sysdig-agent-v1.0.0                                   2m17s
sysdig-agent-v1.1.0                                   2m17s
upwind-agent-allowlist-v0.1.0                         2m16s
wiz-sensor-v1                                         2m16s
wiz-sensor-v2                                         2m16s
```

View a single configuration:
```
ALLOWLIST_NAME=wiz-sensor-v2
kubectl get workloadallowlist $ALLOWLIST_NAME -o yaml
```
