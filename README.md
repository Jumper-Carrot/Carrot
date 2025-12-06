# 🥕 Carrot

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)


The Carrot project is the **open-source server component** that powers the 
[Jumper](https://github.com/Jumper-Carrot/Jumper) desktop application.


## 🚀 Getting Started (Deployment)

If you are looking to **install and run** Carrot locally as a final product, please refer to the dedicated deployment 
[repository](https://github.com/Jumper-Carrot/Carrot-deploy).

For more information about Carrot and Jumper setup and usage, 
see the official [Jumper documentation](https://jumper-app.com).



## 🤝 Contributing

For detailed guidelines on how to contribute to the Carrot project (submitting bugs, feature requests, and Pull Requests), please see the 
[CONTRIBUTING](./.github/CONTRIBUTING.md) file.



## 💻 Local Development

Carrot is built with:

[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

### ⚙️ Setup

> **Prerequisite:** We strongly recommend using [Docker](https://docs.docker.com/engine/install/) to manage the development environment for Carrot. You must have Docker installed on your machine to follow these steps.

#### TL;DR (Quick Setup)

```bash
git clone https://github.com/Jumper-Carrot/Carrot.git
cd Carrot
mv .env.sample .env
docker compose up -d --build
docker compose exec carrot python manage.py migrate
```

-----

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Jumper-Carrot/Carrot.git
    cd Carrot
    ```

2.  **Configure Environment Variables:**

    ```bash
    mv .env.sample .env
    ```

    *This file contains configuration settings for the application.*

3.  **Start the Services:**

    ```bash
    docker compose up -d --build
    ```

    *This command builds the necessary Docker images and starts the database and server containers.*

4.  **Apply Database Migrations:**

    ```bash
    docker compose exec carrot python manage.py migrate
    ```

### Access

The Carrot API server should now be accessible at: [`http://localhost:8000`](https://www.google.com/search?q=http://localhost:8000).

The default administrator user credentials are:

  * **Email:** `admin@mail.com`
  * **Password:** `admin`



## 📦 Managing Python Dependencies

### Adding a New Dependency

The Python dependencies are automatically managed by the Docker build process using the dependencies listed in the [*pyproject.toml*](https://www.google.com/search?q=./pyproject.toml) file.

To add a new dependency:

1.  Add the dependency to the list in `pyproject.toml`.
2.  Restart the containers and force the Docker image to be rebuilt: `docker compose up -d --build`.

### IDE Autocompletion

Since Python packages are installed **inside the Docker container**, your local IDE (Integrated Development Environment) may not automatically find them, resulting in missing autocompletion.

Two recommended solutions are available:

1.  **VS Code Extension:** Use the [Dev Container](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension. Select "*Reopen in container*" from the "Remote Host" menu. This opens your development environment *inside* the Docker container, granting full access to dependencies.
2.  **Local Virtual Environment:** Create and activate a local virtual Python environment, then install the dependencies manually:
    ```bash
    python -m venv .venv
    source .venv/bin/activate 
    pip install ".[dev]"
    ```
    *Note: Remember that adding a dependency to the virtual environment will **not** add it to the container; you must still update `pyproject.toml` and rebuild the Docker image.*

