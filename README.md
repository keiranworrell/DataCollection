# DataCollection
Construct a database of edges and nodes that will represent character interactions in a text

## Setting up the Kubernetes Cluster (Mac)
* Install Docker Desktop
 * Click the Docker menu bar item and access preferences
 * Access the Kubernetes tab and click the checkbox to enable Kubernetes. Click apply
* Install Kubernetes kubectl-cli tool using Homebrew
 * In your terminal, run `brew install kubernetes-cli`
 * Check everything is installed by running `kubeclt get pods --all-namespaces`