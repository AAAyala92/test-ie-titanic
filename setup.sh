#bash script
#to run it bash setup.sh

echo "Installing miniforge3..."
pyenv install miniforge3

export PYENV_VERSION=miniforge3

echo "Creating environment..."
conda create -n titanic39 python=3.9 --yes

#Because of how conda activate works this is har do make work in script
#conda activate titanic39
#pip install -e .[dev]

