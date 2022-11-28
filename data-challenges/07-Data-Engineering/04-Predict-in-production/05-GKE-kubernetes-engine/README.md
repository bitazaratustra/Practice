
## Objective

Use **Kubernetes Engine** in order to deploy a container at scale.

Go through the steps to deploy a Docker image for your API at scale.

## Context

Is the computing power of a single Cloud Run server not enough to server your customer base?

Let's scale massively using a cluster of hosts serving your API.

Using massive amounts of processing power comes at a cost 💸

⚠️ If you are playing with this exercise, make sure to **DELETE** the cluster as soon as you are done ⚠️

Also, keep an eye on the [billing in the GCP console](https://console.cloud.google.com/billing).

More on [Google Kubernetes Engine pricing](https://cloud.google.com/kubernetes-engine/pricing).

You may use [this calculator](https://cloud.google.com/products/calculator) in order to evaluate the monthly cost of running a cluster.

⚠️ Again, keep in mind to monitor the pricing, and delete the cluster once you are done ⚠️

## Push our prediction API image to Google Kubernetes Engine

Let's scale our image to a cluster of hosts using Kubernetes Engine 🤖🤖🤖

We will first create an environment variable containing the name of the cluster:

``` bash
export CLUSTER_NAME=define-some-cluster-name
echo $CLUSTER_NAME
```

And select a region from the [region list](https://cloud.google.com/compute/docs/regions-zones).

We can now create a cluster:

``` bash
gcloud container clusters create $CLUSTER_NAME --num-nodes 2 --region europe-west1
```

You should see a similar output indicating that the cluster is being created:

``` txt
Creating cluster wagon-data-tpl-cluster in europe-west1... Cluster is being health-checked (master is healthy)...done.
Created [https://container.googleapis.com/v1/projects/le-wagon-data/zones/europe-west1/clusters/wagon-data-tpl-cluster].
To inspect the contents of your cluster, go to: https://console.cloud.google.com/kubernetes/workload_/gcloud/europe-west1/wagon-data-tpl-cluster?project=le-wagon-data
kubeconfig entry generated for wagon-data-tpl-cluster.
NAME                    LOCATION      MASTER_VERSION   MASTER_IP     MACHINE_TYPE   NODE_VERSION     NUM_NODES  STATUS
wagon-data-tpl-cluster  europe-west1  1.16.13-gke.401  35.195.38.77  n1-standard-1  1.16.13-gke.401  6          RUNNING
```

You can [access the cluster](https://console.cloud.google.com/kubernetes/list?project=le-wagon-data) and [inspect the content of the cluster](https://console.cloud.google.com/kubernetes/workload_/gcloud/europe-west1-c/wag-data-tpl-cluster?project=le-wagon-data).

The started instances will be visible in [Compute Engine](https://console.cloud.google.com/compute/instances).

You can [delete the cluster](https://console.cloud.google.com/kubernetes/list) at anytime to stop it from running and preserve 💸.

Optionally, you may customize the parameters of the cluster in a `gke.yaml` file:

You may replace `ml-kube-deployment`:

``` bash
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: ml-kube-deployment
  name: ml-kube-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ml-kube-deployment
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: ml-kube-deployment
    spec:
      containers:
      - image: gcr.io/$GCP_PROJECT_ID/ml-kube-deployment
        name: ml-kube-deployment
        resources:
          requests:
            memory: "4G"
status: {}
```

And apply the configuration:

``` bash
echo gke.yaml | kubectl apply -f -
```

Now we can create an environment variable containing the name of our deployment:

``` bash
export DEPLOYMENT_NAME=define-some-deployment-name
echo $DEPLOYMENT_NAME
```

We can navigate to [Google Container Registry](https://console.cloud.google.com/gcr/) in order to copy the full name of the image we wish to deploy to the cluster.

Now we will deploy our image to the cluster:

``` bash
kubectl create deployment $DEPLOYMENT_NAME --image eu.gcr.io/$PROJECT_ID/$DOCKER_IMAGE_NAME
```

``` bash
kubectl expose deployment $DEPLOYMENT_NAME --type=LoadBalancer --port 80 --target-port 5000
```

Let's retrieve the external ip address that will allow users to connect to our cluster:

```bash
kubectl get service --watch
```

``` txt
NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)        AGE
kubernetes           ClusterIP      10.111.240.1     <none>          443/TCP        19m
ml-kube-deployment   LoadBalancer   10.111.246.169   35.240.48.112   80:32076/TCP   48s
```

Here the external IP address is `35.240.48.112`, and if the image contains a web server (for example the server servicing our prediction API), it will be accessible worldwide 🌍 and with a high capacity at `https://35.240.48.112/` 🚀

⚠️ Again, keep in mind that you are paying for the cluster, which means several machines, as long as it remains up 💸

## Troubleshoot

You may list the configuration of your cluster:

``` bash
gcloud container clusters list
kubectl get pods
kubectl describe pod ml-kube-deployment-67556cccc5-6ldwx
```

Look at the messages in the events in order to understand what is going on should an error occur.

## Delete Google Kubernetes Engine cluster once usage is done

Delete the application on the cluster:

```bash
kubectl delete deployment $DEPLOYMENT_NAME
```

Delete the cluster:

```bash
gcloud container clusters delete $CLUSTER_NAME --region europe-west1
```
