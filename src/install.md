# Installation Steps 

1. Create a kubernetes namespace for the deployment

```bash
kubectl create namespace <NAMESPACE>
```

2. Update and run scripts/az-setup.sh

This will create the application's Managed Identity and Federated Credential and grant them permission to Key Vault

```bash
./scripts/az-setup.sh
```

3. Update demo801b/values.yaml and install the helm chart

This will create all the application artifacts in Kubernetes.

```bash
helm install demo801b demo801b -n <NAMESPACE>
```

## Notes

The report-writer is configured to run once per day at midnight.  You can run it on demand using the following technique:

```bash
kubectl create job --from=cronjob/report-writer <NEW-JOB-NAME> -n <NAMESPACE>
```