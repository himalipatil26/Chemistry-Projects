<h1 align="center">pH Indicator Visualizer</h1>

<p align="center">
  <b>A colorful chemistry mini-project to visualize the relationship between pH, solution color, and hydrogen ion concentration.</b><br>
  Built using <b>Python</b> and <b>Matplotlib</b> for Class 11 Chemistry.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge&logo=plotly">
  <img src="https://img.shields.io/badge/Project-pH_Visualizer-green?style=for-the-badge&logo=atom">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge">
</p>

---

## 🧪 Overview

The **pH Indicator Visualizer** is a simple educational tool designed to help students understand:

* How **pH relates to solution color**
* How **[H⁺] (hydrogen ion concentration)** changes across the pH scale
* How acids, bases, and neutral solutions differ visually & numerically

It displays:

* A **color block** representing the pH value (0 = red, 7 = green, 14 = blue)
* A **semilog graph** of Hydrogen ion concentration vs pH
* A highlighted marker showing the entered pH value

---

> ⚠️ **Academic Use Only**
> This project is designed for **learning, demonstration, and practical submission** purposes.
> Not intended for chemical analysis or lab instrumentation.

---

## 🎨 Features

### 🔹 Color Representation

Maps pH → RGB color:

* **Acidic (0–7)** → Red → Yellow → Green
* **Neutral (7)** → Pure Green
* **Basic (7–14)** → Green → Cyan → Blue

### 🔹 Classification

Automatically labels input as:

* **Acidic** (pH < 7)
* **Neutral** (pH = 7)
* **Basic** (pH > 7)

### 🔹 Scientific Plot

* Smooth curve of `10^(-pH)`
* Semilog scale for readability
* Highlights chosen pH value

---

## 📂 Project Structure

```
ph_indicator_visualizer/
├── ph_visualizer.py
└── README.md
```

---

## 🚀 Getting Started

### 🧰 Requirements

* Python 3.8+
* Matplotlib
* NumPy

### 📥 Installation

```bash
pip install matplotlib numpy
```

### ▶️ Run the Program

```bash
python ph_visualizer.py
```

Enter a pH value between **0 and 14** when prompted.

---

## 📊 Visualization Examples

The program displays:

* A **color preview block** representing the pH
* A **Hydrogen Ion Concentration vs pH** graph
* Automatic classification (Acidic / Neutral / Basic)
<p aling="center">
<img width="896" height="544" alt="image" src="https://github.com/user-attachments/assets/0a944f9b-314d-4eb0-98b2-8426832ebd36" />
</p> 

<p aling="center">  
<img width="899" height="535" alt="image" src="https://github.com/user-attachments/assets/7c94693a-6526-47c9-9b82-c36620900cbd" />
</p>

<p aling="center">  
<img width="901" height="547" alt="image" src="https://github.com/user-attachments/assets/7c60da76-b6c3-400a-a0da-ad5e08b219e8" />
</p>




---

## 🧑‍💻 Author

**Himali Patil**


---

<h2 align="center">✨ Learn • Visualize • Understand — with <b>pH Indicator Visualizer</b> ✨</h2>
<p align="center">
<i>Made with ❤️ & Python for science students</i><br><br>
<img src="https://img.shields.io/badge/Chemistry-Learning-green?style=for-the-badge&logo=beaker"> 
<img src="https://img.shields.io/badge/Student_Project-Ready-blue?style=for-the-badge&logo=graduation-cap"> 
<img src="https://img.shields.io/badge/Open--Source-Contributions%20Welcome-orange?style=for-the-badge&logo=open-source-initiative"> 
</p>
