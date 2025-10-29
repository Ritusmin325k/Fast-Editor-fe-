# fe (Fast Editor)
<p align="center">
  <img src="https://github.com/Ritusmin325k/Fast-Editor-fe-.git/logo.png" alt="fe Fast Editor Logo" width="200"/>
</p>

`fe` (Fast Editor) is a lightweight terminal tool that helps you open and edit files faster in **Termux**, **Proot**, or **Linux**.  
Instead of typing commands like `nano filename` or `vim file.txt`, just type:

```bash
fe
```

Then select a file and choose your preferred editor — all within the same terminal window.

---

## 🔧 Features
- Works directly in the same terminal window.
- Arrow key navigation for file selection.
- Supports **nano**, **vim**, and **nvim** editors.
- Lightweight and fast.
- Works perfectly on **Termux** and **Proot distros**.

---

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Ritusmin325k/fe.git
cd fe
```

### 2. Install dependencies
```bash
pip install simple-term-menu
```

If your system shows “externally-managed-environment” error (e.g. Arch/Proot), use a virtual environment:

```bash
python -m venv ~/.venv
source ~/.venv/bin/activate
pip install simple-term-menu
```

### 3. Make the tool executable
```bash
chmod +x fe
sudo mv fe /usr/local/bin/
```

Now you can run `fe` from anywhere in the terminal.

---

## 🧠 Usage

Type:
```bash
fe
```

Then follow the prompts:
1. Use arrow keys to select a file.
2. Press **Enter** to confirm.
3. Choose your preferred editor (**nano**, **vim**, or **nvim**).
4. The selected file opens instantly.

---

## 📂 Example

```bash
❯ fe
Select a file:
> main.py
  readme.md
  script.sh

Choose editor:
> nano
  vim
  nvim
```

---

## ⚙️ Requirements
- Python 3.7 or newer  
- `simple-term-menu` module

---

## 📁 Folder Structure
```
fe/
 ├── fe               # Main script
 ├── README.md        # Documentation
 ├── requirements.txt # Dependencies
```

---

## 🧑‍💻 Author
Developed by **Ritusmin Saikia**  
GitHub: [https://github.com/Ritusmin325k](https://github.com/Ritusmin325k)

---
