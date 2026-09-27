# DevOps Lab

Laboratorio de práctica personal con las herramientas más usadas de DevOps, DevSecOps y AIOps a nivel global, construido de forma incremental como parte de un plan de aprendizaje.

## Estructura del repositorio

- src/promedio.py              -> Codigo de ejemplo con pruebas unitarias
- tests/test_promedio.py       -> Pruebas con pytest
- requirements.txt             -> Dependencias de Python
- .github/workflows/ci.yml     -> Pipeline de CI en GitHub Actions
- .gitlab-ci.yml               -> Pipeline de CI en GitLab CI
- Jenkinsfile                  -> Pipeline de CI en Jenkins (con webhook automatico)
- k8s/deployment.yaml          -> Manifiesto desplegado por Argo CD (GitOps)
- k8s/service.yaml             -> Manifiesto desplegado por Argo CD (GitOps)

## CI/CD: tres motores, un mismo caso de prueba

El mismo conjunto de pruebas (pytest) se ejecuta automaticamente en cada push a traves de:

- GitHub Actions: pipeline como servicio, gatillado nativamente por GitHub.
- GitLab CI: mismo enfoque, sintaxis distinta, espejado en un repo paralelo de GitLab.
- Jenkins: servidor propio en Docker, con webhook de GitHub via tunel ngrok, demostrando el modelo "CI que administras tu" frente a "CI como servicio".

## GitOps con Argo CD

La carpeta k8s/ es monitoreada por una instancia de Argo CD corriendo en un cluster local de kind. Cualquier cambio en estos manifiestos se despliega automaticamente al cluster, sin intervencion manual, incluyendo reversion automatica de cambios hechos fuera de Git (Self Heal).

## Como correr las pruebas localmente

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest -v

## Otros laboratorios relacionados (fuera de este repo)

- Terraform (terraform-lab): ciclo de vida completo de IaC contra el proveedor de Docker - init, plan, apply, gestion de drift, destroy.
- Ansible (ansible-lab): 3 VMs con Vagrant/VirtualBox, inventario dinamico, playbooks idempotentes.
- Kubernetes (k8s-lab): cluster local con kind, despliegues con Helm, GitOps con Argo CD.
