import pretty_midi

# MIDI dosyasını yükleme
midi_data = pretty_midi.PrettyMIDI('Desert-Caravan-Aaron-Kenny(chosic.com).mid')

# Yeni bir MIDI dosyası oluşturma
new_midi = pretty_midi.PrettyMIDI()

# Sadece piyano ve gitar notalarını yeni MIDI dosyasına ekleyelim
for instrument in midi_data.instruments:
    if instrument.program in [0, 24]:  # 0: Piyano, 24: Gitar
        new_midi.instruments.append(instrument)

# Yeni MIDI dosyasını kaydedelim
new_midi.write('output_piano_guitar.mid')
print("'output_piano_guitar.mid' dosyası başarıyla oluşturuldu.")
