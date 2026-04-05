## AI-Powered Self-Healing CI/CD Pipeline with DevSecOps

> Autonomous DevSecOps system that detects failures, diagnoses root causes, and heals production systems in under 90 seconds.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Docker](https://img.shields.io/badge/Docker-Container-blue?style=flat-square&logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-blue?style=flat-square&logo=kubernetes)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI/CD-blue?style=flat-square&logo=githubactions)
![SonarQube](https://img.shields.io/badge/SonarQube-SAST-red?style=flat-square&logo=sonarqube)
![Trivy](https://img.shields.io/badge/Trivy-Scan-red?style=flat-square)
![OWASP ZAP](https://img.shields.io/badge/OWASP%20ZAP-DAST-red?style=flat-square)
![OPA](https://img.shields.io/badge/OPA-Policy-red?style=flat-square)
![Prometheus](https://img.shields.io/badge/Prometheus-Metrics-orange?style=flat-square&logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-Dashboard-orange?style=flat-square&logo=grafana)
![LangChain](https://img.shields.io/badge/LangChain-Agent-amber?style=flat-square)
![OpenAI](https://img.shields.io/badge/OpenAI-LLM-amber?style=flat-square&logo=openai)
![Slack](https://img.shields.io/badge/Slack-Alerts-purple?style=flat-square&logo=slack)
![Terraform](https://img.shields.io/badge/Terraform-IaC-purple?style=flat-square&logo=terraform)
![MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![PRs](https://img.shields.io/badge/PRs-Welcome-green?style=flat-square)

---

## Project tagline

> **Detects:** real-time deployment failures, CVEs, and runtime anomalies across logs, metrics, and traces  
> **Fixes:** production issues automatically via rollback, AI-driven patching, and policy enforcement  
> **Replaces:** manual debugging, delayed security reports, and reactive on-call firefighting  

---

## Architecture diagram

```mermaid
graph TD

subgraph CODE
A[GitHub Push] --> B[Gitleaks Pre-commit] --> C[GitHub Actions]
end

subgraph SECURITY
C --> D[SonarQube SAST]
C --> E[Trivy Scan]
C --> F[OWASP ZAP]
C --> G[OPA Policy]
end

subgraph BUILD
G --> H[Docker Build] --> I[ECR Push]
end

subgraph DEPLOY
I --> J[Argo Rollouts] --> K[ArgoCD]
end

subgraph OBSERVE
K --> L[Prometheus]
K --> M[ELK]
K --> N[OpenTelemetry]
end

subgraph AI
L --> O[LangChain]
M --> O
N --> O
O --> P[OpenAI]
end

subgraph HEAL
P --> Q[Rollback]
P --> R[Patch PR]
P --> S[Slack Alert]
end

style D fill:#fee2e2
style E fill:#fee2e2
style F fill:#fee2e2
style G fill:#fee2e2

style O fill:#fef3c7
style P fill:#fef3c7

style Q fill:#dcfce7
style R fill:#dcfce7
style S fill:#dcfce7

style L fill:#f1f5f9
style M fill:#f1f5f9
style N fill:#f1f5f9

style J fill:#dbeafe
style K fill:#dbeafe



Screenshots
Session 1 — Flask app running locally


Flask app on localhost:5000 — all 3 routes returning healthy responses

Session 2 — GitHub Actions CI pipeline


Coming in Session 2 — CI pipeline with test, build, and scan stages

Session 10 — AI agent root cause diagnosis


Coming in Session 10 — LangChain agent JSON output with root cause and fix

Session 12 — Self-healing event timeline


Coming in Session 12 — Slack message showing 90-second auto-recovery

Session 13 — Grafana unified dashboard


Coming in Session 13 — security events, deployment status, AI decisions

Adding your Session 1 screenshot:

Run docker compose up --build
Open browser to http://localhost:5000/health
Screenshot terminal (left) + browser (right)
Save as docs/screenshots/app-running.png
Run git add docs/screenshots/app-running.png && git commit -m "docs: add session 1 app screenshot"
Tech stack
Layer	Tool	Purpose	Version	Status
App	Flask	API	2.3	✅ Complete
Security	Gitleaks	Secret scan	8.x	✅ Complete
Container	Docker	Build image	latest	✅ Complete
Local	Docker Compose	Run app	v2	✅ Complete
CI/CD	GitHub Actions	Pipeline	latest	🔄
SAST	SonarQube	Code scan	latest	🔄
Scan	Trivy	CVE scan	latest	🔄
DAST	OWASP ZAP	Runtime scan	latest	🔄
Policy	OPA	Enforcement	latest	🔄
Deploy	Kubernetes	Orchestration	latest	🔄
GitOps	ArgoCD	Sync	latest	🔄
Monitoring	Prometheus	Metrics	latest	🔄
Logs	ELK	Logging	latest	🔄
AI	LangChain	Agent	latest	⏳
LLM	OpenAI	RCA	gpt-4o-mini	⏳
The problem this solves

At 2 AM, a deployment fails. Alerts fire, logs are noisy, dashboards are inconsistent, and engineers scramble to find the root cause. Recovery takes 30–60 minutes, often involving guesswork.

Security makes it worse. Vulnerabilities are discovered days later in reports that nobody prioritizes. Secrets leak silently. Misconfigurations slip into production.

This system flips the model. Failures are detected instantly, analyzed by an AI agent using logs, metrics, and traces, and resolved automatically through rollback or patching.

The result: MTTR drops from 45 minutes to under 90 seconds. Security issues are triaged in real time. Engineers wake up to a resolved incident instead of a crisis.

Project structure
ai-devsecops-platform/
├── app/                # Flask application
├── k8s/                # Kubernetes manifests
├── .github/workflows/  # CI/CD pipelines
├── terraform/          # Infrastructure as Code
├── security/           # Security configs
├── monitoring/         # Observability configs
├── docs/
│   └── screenshots/    # Visual proof
├── docker-compose.yml
├── .pre-commit-config.yaml
└── README.md
Self-healing flow
Bad image deployed
Canary release starts (20% traffic)
Prometheus detects error spike at T+45s
Alert triggered at T+60s
AI analyzes logs + metrics
Root cause identified in <5s
Rollback triggered at T+70s
System restored at T+90s

A human would take 30–60 minutes to debug logs, identify the issue, and rollback manually.

Contributing
Fork the repo
Create a feature branch
Commit changes
Ensure pre-commit passes
Open PR
License

MIT License

Built with obsession by Ashish Mondal
