### Hey Willkommen auf unserer Seite zur 8 x 8 LED matrix
Mehr Infos: http://codingworld.io/project/8x8-led-matrix-anschliessen-und-programmieren
Hardware zum Kaufen:


```bash
git clone https://github.com/rm-hull/max7219.git
```

```bash
cd max7219
```

```bash
sudo python setup.py install
```

```bash
cd
```

```bash
sudo apt-get install python-dev python-pip
```

```bash
sudo pip install spidev
```

![8x8 LED Matrix am Raspberry Pi](http://image.codingworld.eu/storage/1122/show)


| Anschlüsse Raspberry Pi | Anschlüsse LED Matrix |
| ----- |  ----- |
| 5V | 1 - VCC |
| GND | 2 - GND |
| GPIO 10 (MOSI) | 3 - DIN |
| GPIO 8 (SPI CE0) | 4 - CS |
| GPIO 11 (SPI CLK) | 5 - CLK |

