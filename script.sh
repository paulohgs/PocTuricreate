#!/bin/sh

echo "Verificando versão do python..."
pyv="$(python3 --version)"

if [ "$pyv"!="Python 3.8.8" ]; then
    echo "Versão não condizente, instalando versão necessária..."
    echo "Instalando pyenv...";
    curl https://pyenv.run | bash;

    echo "Instalando python 3.8.8...";
    pyenv install 3.8.8;

    echo "Tornando versão 3.8.8 versão global...";
    pyenv global 3.8.8;

    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc;
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc;
    echo 'eval "$(pyenv init -)"' >> ~/.zshrc;
else
    echo "Iniciando preparação de arquivos...";
    cd bitmaps
    echo "Baixando dataset de bitmap..."
    curl https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap/square.npy > square.npy;
    curl https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap/triangle.npy > triangle.npy;

    echo "Baixando dataset de strokes..."
    cd ../strokes
    curl https://storage.googleapis.com/quickdraw_dataset/full/raw/square.ndjson > square.ndjson
    curl https://storage.googleapis.com/quickdraw_dataset/full/raw/triangle.ndjson > triangle.ndjson

    cd ../..

    chmod +x main.py
    python3 main.py
fi




