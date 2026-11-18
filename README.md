<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:4A0D2E,50:C2185B,100:FF8FC7&height=200&section=header&text=State%20of%20the%20Heart&fontSize=50&fontColor=FFFFFF&fontAlignY=36&desc=A%20mood-based%20Quran%20player&descSize=16&descAlignY=58" width="100%" alt="State of the Heart"/>

<p>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/License-MIT-FF4FA3?style=for-the-badge" alt="MIT License"/>
</p>

**[Open the web player](https://21afnan.github.io/State_of_Heart_Quran_Player/)**

</div>

---

## The idea

Some days you know exactly how you feel but not what to listen to. **State of the Heart** asks one question, *how is your heart right now?*, and plays a Surah with translation (Tarjama) that speaks to that feeling. There is nothing to configure and nothing to sign up for: pick a mood, press play.

<p align="center"><img src="Images/quran.png" width="520" alt="App preview"/></p>

## Moods and Surahs

| State of heart | Surah played |
|---|---|
| Sad | Ad-Duha (93) |
| Anxious | Ash-Sharh (94) |
| Grateful | Ar-Rahman (55) |
| Calm | Al-Kahf (18) |
| Lost | Al-Fatiha (1) |
| Motivated | Al-Asr (103) |
| Angry | Aal-e-Imran (3) |
| Lonely | Maryam (19) |

## Two versions in one repo

| | Web player | Desktop player |
|---|---|---|
| File | `index.html` | `main.py` |
| Built with | HTML, CSS, JavaScript (no framework, no backend) | Python, Tkinter, pygame, Pillow |
| Flow | Choose a mood, then Play, Pause or Replay | Welcome screen with Bismillah, then mood picker and icon controls |
| Extras | Shows the Surah name while it plays | Pause resumes from the same position; can be packaged as a Windows `.exe` with PyInstaller (`main.spec`) |

## Run it

**Web:** open `index.html` in any browser, or use the [live page](https://21afnan.github.io/State_of_Heart_Quran_Player/).

**Desktop:**

```bash
pip install pygame pillow
python main.py
```

Optional Windows build:

```bash
pip install pyinstaller
pyinstaller main.spec
```

## Project structure

```
State_of_Heart_Quran_Player/
├── index.html     # web player
├── main.py        # Tkinter desktop player
├── main.spec      # PyInstaller build file
├── Images/        # background, Bismillah and control icons
└── audio/         # Surah recitations with translation (mp3)
```

## License and credits

The code is released under the [MIT License](LICENSE). The Quran recitation audio is included only for personal, educational and spiritual use; all rights stay with the reciters and their publishers, and the audio is not covered by the MIT License.

---

<div align="center">

Made by **Afnan Shoukat**

<a href="mailto:afnanshoukat35@gmail.com"><img src="https://img.shields.io/badge/Email-afnanshoukat35%40gmail.com-FF4FA3?style=for-the-badge&logo=gmail&logoColor=white&labelColor=4A0D2E" alt="Email"/></a>
<a href="https://www.linkedin.com/in/afnanshoukat"><img src="https://img.shields.io/badge/LinkedIn-Afnan%20Shoukat-FF4FA3?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=4A0D2E" alt="LinkedIn"/></a>
<a href="https://github.com/21Afnan"><img src="https://img.shields.io/badge/GitHub-21Afnan-FF4FA3?style=for-the-badge&logo=github&logoColor=white&labelColor=4A0D2E" alt="GitHub"/></a>

</div>
