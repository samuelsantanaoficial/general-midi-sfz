#!/bin/bash

# Verifica se FFmpeg está instalado
if ! command -v ffmpeg &> /dev/null; then
    echo "FFmpeg não está instalado. Instale-o com: sudo apt install ffmpeg"
    exit 1
fi

# Processa todos os arquivos WAV na pasta
for file in *.wav; do
    if [ -f "$file" ]; then
        echo "Normalizando: $file"
        temp_file="${file%.wav}_temp.wav"
        ffmpeg -i "$file" -af "loudnorm=I=-18:TP=-3:LRA=11" -ar 48000 -b:a 768k "$temp_file" -y
        mv "$temp_file" "$file"
        echo "Arquivo processado: $file"
    fi
done

echo "Normalização concluída!"


