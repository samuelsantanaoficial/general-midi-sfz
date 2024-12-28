#!/bin/bash

# Verifica se FFmpeg está instalado
if ! command -v ffmpeg &> /dev/null; then
    echo "FFmpeg não está instalado. Instale-o com: sudo apt install ffmpeg"
    exit 1
fi

# Processa todos os arquivos WAV na pasta
for file in *.wav; do
    if [ -f "$file" ]; then
        echo "Processando: $file"
        temp_file="${file%.wav}_temp.wav"
        ffmpeg -i "$file" -af silenceremove=start_periods=1:start_duration=0.1:start_threshold=-48dB "$temp_file" -y
        mv "$temp_file" "$file"
        echo "Arquivo atualizado: $file"
    fi
done

echo "Processamento concluído!"
