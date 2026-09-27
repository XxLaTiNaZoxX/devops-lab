# DevOps Lab

Laboratorio de práctica personal con las herramientas más usadas de DevOps, DevSecOps y AIOps a nivel global, construido de forma incremental como parte de un plan de aprendizaje.

## Estructura del repositorio

## CI/CD: tres motores, un mismo caso de prueba

El mismo conjunto de pruebas (`pytest`) se ejecuta automáticamente en cada push a través de:

- **GitHub Actions** — pipeline como servicio, gatillado nativamente por GitHub.
- **GitLab CI** — mismo enfoque, sintaxis distinta, espejado en un repo paralelo de GitLab.
- **Jenkins** — servidor propio en Docker, con webhook de GitHub vía túnel ngrok, demostrando el modelo "CI que administras tú" frente a "CI como servicio".

## GitOps con Argo CD

La carpeta `k8s/` es monitoreada por una instancia de Argo CD corriendo en un clúster local de `kind`. Cualquier cambio en estos manifiestos se despliega automáticamente al clúster, sin intervención manual — incluyendo reversión automática de cambios hechos fuera de Git (Self Heal).

## Cómo correr las pruebas localmente

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest -v
```

## Otros laboratorios relacionados (fuera de este repo)

- **Terraform** (`terraform-lab`): ciclo de vida completo de IaC contra el proveedor de Docker — init, plan, apply, gestión de drift, destroy.
- **Ansible** (`ansible-lab`): 3 VMs con Vagrant/VirtualBox, inventario dinámico, playbooks idempotentes.
- **Kubernetes** (`k8s-lab`): clúster local con `kind`, despliegues con Helm, GitOps con Argo CD.
