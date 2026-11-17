from music21 import *

def get_diatonic_chords(tonic):

    tonalidade = _como_tonalidade(tonic)
    escala = tonalidade.getScale()
    notas = list(escala.getPitches())
    # A escala concreta inclui a tônica uma oitava acima; os graus são os 7 primeiros.
    if len(notas) > 1 and notas[0].name == notas[-1].name:
        notas = notas[:-1]
    acordes = []
    quantidade = len(notas)
    for indice, fundamental in enumerate(notas):
        membros = [pitch.Pitch(fundamental.nameWithOctave)]
        # Dois saltos de terça diatônica: 3ª e 5ª do acorde.
        for salto in (2, 4):
            nota_da_escala = notas[(indice + salto) % quantidade]
            membros.append(_proxima_terca(nota_da_escala, membros[-1]))
        acordes.append(chord.Chord(membros))
    return acordes

def _como_tonalidade(tonic):
    pass