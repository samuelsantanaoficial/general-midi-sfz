 #!/bin/bash

# Verifica se FFmpeg está instalado
if ! command -v ffmpeg &> /dev/null; then
    echo "FFmpeg não está instalado. Instale-o com: sudo apt install ffmpeg"
    exit 1
fi

# Processa todos os arquivos WAV na pasta
for file in *.wav; do
    if [ -f "$file" ]; then
        echo "Convertendo para mono: $file"
        temp_file="${file%.wav}_temp.wav"
        ffmpeg -i "$file" -ac 1 "$temp_file" -y
        mv "$temp_file" "$file"
        echo "Arquivo convertido: $file"
    fi
done

echo "Conversão concluída!"
