# Nuclear Merging

Nuclear Merging is a particle-dodging game where you collect protons and neutrons to build up your atomic nucleus while avoiding photons.

**[Play in your browser](https://eunhosode.github.io/nuclear_merging/)**

## How to Play

You start as a hydrogen nucleus and absorb particles as they fall. The particles you collect determine your element and isotope.

| Color | Particle | Effect on Contact |
| :--- | :--- | :--- |
| Red | Proton | Increases your atomic number by 1, changing your nucleus to the next element. |
| Blue | Neutron | Adds one neutron, changing your nucleus to another isotope of the same element. |
| Green | Photon | Your nucleus decays instantly, ending the game. |

- Each time you absorb a proton or neutron, the game checks whether you survive based on the resulting isotope's decay probability.
- The game supports element symbols from **hydrogen (H, 1) to oganesson (Og, 118)**.
- Isotopes are displayed as **element symbol–mass number**, such as `He-4` and `U-238`.
- The mass number is the total number of protons and neutrons.

## Controls

| Platform | Movement | Menu Selection |
| :--- | :--- | :--- |
| Python | ← / → | Mouse click |
| Web (desktop) | ← / → or A / D | Mouse click |
| Web (mobile) | Left and right buttons at the bottom of the screen | Tap |

## Game Modes

The game offers **12 modes** with different particle speeds, spawn weights, and special effects.

| Mode | Proton and Neutron Speed | Photon Speed | Spawn Weights | Special Rules |
| :--- | ---: | ---: | :---: | :--- |
| Easy | 3 | — | 1:2:0 | No photons spawn. |
| Normal | 3 | 6 | 3:6:1 | Default mode. |
| Hard | 3 | 9 | 3:6:1 | Photons move faster than in Normal mode. |
| Speedy | 6 | 12 | 6:12:1 | All particles move faster than in Normal mode. |
| Is it snail? | 1 | 18 | 3:6:1 | Slow protons and neutrons, fast photons. |
| Choking | 3 | 1 | 1:2:3 | Slow photons stay on screen longer. |
| Miserable | 3 | 9 | 1:2:3 | Photons have a high spawn weight. |
| Schrödinger's particle | 3 | 12 | 1:1:0 | Each proton or neutron has a 75% chance to turn into a photon. |
| Midgley's Gas | 3 | 18 | 1:2:3 | Photons have a high spawn weight, and each proton or neutron has a 75% chance to turn into a photon. |
| Permian | 18 | 18 | 1:1:1 | All particles move very fast, and each proton or neutron has a 90% chance to turn into a photon. |
| Fog | 3 | 6 | 3:6:1 | Fog in the middle of the screen obscures particles. |
| Paralysis | 3 | 6 | 3:6:1 | Every 10 seconds, there is a 50% chance that you lose the ability to move for 3 seconds. |

**How to read the table**

- Speeds are measured in **pixels per frame at 60 FPS**.
- Spawn weights are listed in **proton : neutron : photon** order. They determine which particle type is selected at each spawn event.
- When photons are selected, **3–6 photons** spawn at once, depending on your atomic number. The actual ratio of spawned particles can therefore differ from the listed weights.
- The photon conversion chance applies to each spawned proton and neutron individually. It is separate from the nucleus's decay probability.

## Installation and Setup

**Web version:** Play directly from the [game page](https://eunhosode.github.io/nuclear_merging/) without installing anything. You can also download `nuclear_merging.html` and open it in your browser.

**Python version:** Requires Python and Pygame. Run the following commands from the folder containing the game file.

```bash
python -m pip install pygame
python nuclear_merging.py
```

## License

MIT License
