# COVID-19 Data Collection App

This Django application retrieves COVID-19 information from the public API [disease.sh](https://disease.sh/v3/covid-19/countries/usa?strict=true), stores the data locally in a SQLite database, and displays it in a simple web interface.

---

## 📂 Project Structure
- `covidapp/` → Django project
- `tracker/` → Django app with models, views, templates
- `requirements.txt` → Python dependencies
- `README.md` → Setup and usage instructions

---

## ⚙️ Environments

We use three environments to separate concerns:

- **Development (dev)** → Local development with debugging enabled.
- **Testing (test)** → For running unit tests and CI pipelines.
- **Production (prod)** → Deployment with optimized settings.

---

## 📦 Dependencies

Install dependencies with `pip`:

```bash
pip install -r requirements.txt

