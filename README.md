# Kubernetes Enterprise Deployment with CI/CD

An end-to-end DevOps project demonstrating automated CI/CD of a containerized Flask application to Kubernetes using GitHub Actions, Docker, GitHub Container Registry (GHCR), and a self-hosted runner.

## Architecture

The pipeline follows this flow:

Developer → GitHub → GitHub Actions CI → Docker Build → GHCR → Self-Hosted Runner → Kubernetes → NGINX Ingress → Application

## Tech Stack

- Python / Flask
- Docker
- Kubernetes
- GitHub Actions
- GitHub Container Registry (GHCR)
- NGINX Ingress Controller
- Kubernetes Metrics Server
- Horizontal Pod Autoscaler (HPA)

## CI/CD Pipeline

Every push to the `main` branch triggers the pipeline:

1. Checkout source code
2. Configure Python
3. Install dependencies
4. Run automated tests with Pytest
5. Build the Docker image
6. Tag the image using the Git commit SHA
7. Push the image to GHCR
8. Trigger the Windows self-hosted runner
9. Apply Kubernetes manifests
10. Deploy the exact commit SHA image
11. Wait for the Kubernetes rolling update
12. Verify the running pods