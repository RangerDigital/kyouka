<p align="center">
  <br /><img
    width="600"
    src="logo.png"
    alt="Kyouka - Remote control for your keyboard's media keys."
  />
</p>

---

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

**Kyouka** is a web application build with **FastAPI** and **Vue.js** used to control Windows Media Keys remotely using your smartphone or any browser.

> 💡 Currently tested only on Windows 10 machine, but should work on Linux too!

Run as a single Python process on your desktop that simulates media button presses and provides you with a web interface that can be accessed in your local network.

This allows you to control music playing from YouTube  *(Or any other media player)* on your desktop while in bed and away from the keyboard. How awesome is that!

<br>

<p align="center">
	<img src="mockup.png" alt="Takagi - Mobile Mockup" width=800/>
</p>

<br>

## 🛠 Getting Started

**It's easy to get started using Kyouka!**

This project uses **Python** as a backend language, so make sure you have It installed!

> 💡 Execute every command in the `./Kyouka` directory!
<br>

- Download `Kyouka_v1.x.x.zip` package from the **Releases** tab on the right and unpack It.

- Install all required dependencies by running this command against the provided `requirements.txt` file:

  ```bash
  python -m pip install -r requirements.txt
  ```

- Run `kyouka.py` file by clicking on It or by typing:

  ```bash
  python kyouka.py
  ```

- **Done!** Now you can access the dashboard by entering your desktop's **local IP** with default **7070** port:
  ```bash
  http://127.0.0.1:7070
  ```

<br>

## 🚧 Contributing

**You are more than welcome to help me improve Kyouka!**

Just fork this project from the `master` branch and submit a Pull Request (PR).

<br>

## 📃 License

This project is licensed under [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/) .
