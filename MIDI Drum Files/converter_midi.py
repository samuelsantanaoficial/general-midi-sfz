import os
import sys
from mido import MidiFile, MidiTrack, Message

# Mapeamento do Drum Map original para General MIDI
drum_map = {
    22: 49, # Hi Crash Choke
    23: 51, # Ride Choke
    24: 57, # Low Crash Choke
    25: 52, # China Choke
    26: 55, # Splash Choke
    27: 56, # WB Low
    28: 56, # WB Low (double)
    29: 56, # WB Hi
    30: 56, # WB Hi (double)
    31: 54, # Tamb Tap
    32: 54, # Tamb Shake
    33: 39, # Clap Solo
    34: 39, # Clap Multi
    35: 31, # Stick Hit
    36: 36, # Kick Dampened
    37: 37, # Snare Sidestick
    38: 38, # Snare Center L/R
    39: 40, # Snare Rimshot
    40: 40, # Snare Halfway L/R
    41: 41, # Tom 4 Center L/R
    42: 42, # Closed HHTip L/R
    43: 43, # Tom 3 Center L/R
    44: 44, # Closed HHPedal
    45: 45, # Tom 2 Center L/R
    46: 46, # Open HH Control
    47: 47, # Tom 1 Center L/R
    48: 49, # Hi Crash Tip
    49: 49, # Hi Crash Edge
    50: 49, # Hi Crash Bell
    51: 51, # Ride Tip
    52: 59, # Ride Edge
    53: 59, # Ride Bell
    54: 57, # Low Crash Tip
    55: 57, # Low Crash Edge
    56: 57, # Low Crash Bell
    57: 52, # China Edge
    58: 52, # China Tip
    59: 55, # Splash Edge
    60: 36, # Kick Open
    61: 37, # Snare Rim Only
    62: 38, # Snare Flam
    63: 40, # Snare Roll
    64: 38, # Snare Wires Off
    65: 41, # Tom 4 Rimshot
    66: 42, # Closed HH Tight Tip L/R
    67: 43, # Tom 3 Rimshot
    68: 42, # Closed HH Shank L/R
    69: 45, # Tom 2 Rimshot
    70: 46, # Open HH Pedal
    71: 47, # Tom 1 Rimshot
    72: 41, # Tom 4 Rim Only
    73: 43, # Tom 3 Rim Only
    74: 45, # Tom 2 Rim Only
    75: 47, # Tom 1 Rim Only
    76: 46, # Open HH 1/4
    77: 46, # Open HH 1/2
    78: 46, # Open HH 3/4
    79: 46, # Open HH Loose
    80: 46, # Open HH Full
    81: 38, # Snare Center L
    83: 38, # Snare Center R
    84: 40, # Snare Halfway L
    85: 42, # Closed HH Tight Tip L
    86: 40, # Snare Halfway R
    87: 42, # Closed HH Tight Tip R
    88: 41, # Tom 4 Center L
    89: 41, # Tom 4 Center R
    90: 42, # Closed HH Tip L
    91: 43, # Tom 3 Center L
    92: 42, # Closed HH Tip R
    93: 43, # Tom 3 Center R
    94: 42, # Closed HH Shank L
    95: 45, # Tom 2 Center L
    96: 45, # Tom 2 Center R
    97: 42, # Closed HH Shank R
    98: 47, # Tom 1 Center L
    100: 47, # Tom 1 Center R
}

# Função para processar cada arquivo MIDI
def processar_midi(arquivo_entrada, pasta_saida):
    midi = MidiFile(arquivo_entrada)
    novo_midi = MidiFile(ticks_per_beat=midi.ticks_per_beat)  # Mantém o PPQ original

    for track in midi.tracks:
        nova_track = MidiTrack()
        for msg in track:
            if msg.type in ['note_on', 'note_off']:
                # Ajusta a nota e o canal
                nova_nota = drum_map.get(msg.note, msg.note)
                nova_track.append(msg.copy(note=nova_nota, channel=9))  # Canal 10 (0-indexed é 9)
            else:
                nova_track.append(msg)
        novo_midi.tracks.append(nova_track)

    # Salva o arquivo na pasta de saída
    nome_arquivo = os.path.basename(arquivo_entrada)
    novo_caminho = os.path.join(pasta_saida, nome_arquivo)
    novo_midi.save(novo_caminho)
    print(f"Processado: {novo_caminho}")

# Caminhos
pasta_entrada = sys.argv[1]
pasta_saida = f"{pasta_entrada}"
# pasta_saida = "convertidos"

# Cria a pasta de saída, se necessário
os.makedirs(pasta_saida, exist_ok=True)

# Processa todos os arquivos MIDI na pasta de entrada
for arquivo in os.listdir(pasta_entrada):
    if arquivo.endswith(".mid"):
        caminho_arquivo = os.path.join(pasta_entrada, arquivo)
        processar_midi(caminho_arquivo, pasta_saida)

print("Processo concluído.")
