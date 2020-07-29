<p align="center">
  <br /><img
    width="600"
    src="logo.png"
    alt="Kyouka - Remote control for your keyboard's media keys."
  />
</p>

---

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

**Kyouka** is a web application build with **FastAPI** and **Vue.js** used to control Windows Media Key remotely using your mobile device/browser.

Now You will be able to control your YouTube music playing from your desktop while laying in bed, how awesome is that!

> 👑 Currently tested only on Windows 10 machine, but because Kyouka works by simulating keyboard presses It should work on other systems too.

<br>

<p align="center">
	<img src="mockup.png" alt="Takagi - Mobile Mockup" width=800/>
</p>

<br>

**Kyouka** runs a single Python API process on your desktop that simulates media keyboard presses, which control interface you can access in your local network.

<br>

## 🔥 Getting Started

**It's easy to get started using Kyouka!**

This project uses **Python** as a backend language, so **install It** first!

- Download `.zip` package from the **Releases** tab and unpack It.

- Install all required dependence by running this command against the `requirements.txt` file.

  ```bash
  python -m pip install -r requirements.txt
  ```

- Run `kyouka.py` file by clicking on It or type:

  ```bash
  python kyouka.py
  ```

- Done! Now you can access the dashboard by entering your desktop's IP with default 7070 port.

<br>

## 🚧 Contributing

**You are more than welcome to help me improve Kyouka!**

Just fork this project from the `master` branch and submit a Pull Request (PR).

<br>

## 📃 License

This project is licensed under [GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/) .
