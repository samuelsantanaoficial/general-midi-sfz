# General Midi SFZ

## About
an expandable collection of virtual instruments in **SFZ format**, compatible with the **General MIDI (GM)** standard. This project is dedicated to providing a diverse and up-to-date library of sounds for musicians, composers and producers.

## Player
- [Sfizz](https://sfztools.github.io/sfizz/downloads/)

## Details
- 10 to 22 velocity layers
- 2 to 3 round robin
- wav 48000 Hz, mono, s16, 768 kb/s

## MIDI Drum folder
All files edited for channel 10, and with the general midi drum map.
- 01 Pop
- 02 Funk
- 03 Jazz
- 04 Hard Rock
- 05 Metal
- 08 Ballad


## Instruments List
|Bank  |Preset|Instrument                |
|:-----|:-----|:-------------------------|
|000   |024   |Acoustic Guitar (Nylon)   |
|000   |025   |Acoustic Guitar (Steel)   |
|000   |026   |Electric Guitar (Les Paul)|
|000   |032   |Acoustic Upright Bass     |
|000   |033   |Electric Bass (finger)    |
|000   |036   |Electric Bass (Slap)      |
|128   |000   |Acoustic Drum Kit         |

## Development
- [x] Add Electric Bass (finger)
- [x] Add Electric Bass (Slap)
- [x] Add Acoustic Drum Kit
- [x] 3 round robin
- [x] Add Acoustic Guitar (Steel)
- [x] multiple outputs on the drum kit
- [x] Add Upright Bass
- [x] separate microphones for drum kit: kick In, Kick Out, Snare Top, Snare Bot, Dir, OH
- [x] Add Acoustic Guitar (Nylon)
- [x] Add Electric Guitar (Les Paul)
- [x] separate midi cc tune knob for kick, snare and toms
- [x] standardize all audio samples in wav 48000 Hz, mono, s16, 768 kb/s
- [x] kick snare toms and hihat samples for overhead
- [ ] separete mics midi cc volume for drum kit
- [ ] customize pitch bend and vibrato for guitars and basses
