# mlflow-project-template
mlflow project template

## STEPS -

### STEP 01- Create a repository by using template repository

### STEP 02- Clone the new repository

### STEP 03- Create a conda environment after opening the repository in VSCODE

```bash
conda create --prefix ./env python=3.7 -y
```

```bash
conda activate ./env
```
OR
```bash
source activate ./env
```

### STEP 04- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 05-create conda.yaml file
```bash
conda env export > conda.yaml
```

### STEP 06- commit and push the changes to the remote repository


### MLflow command 

#### Command to run MLproject file 
```bash
mlflow run . --no-conda
```
### Run any specific entry point in MLproject file 
```bash
mlflow run . -e get_data --no-conda 
or mlflow run . -e get_data -P config=configs/your_config.yaml --no-conda 
```

