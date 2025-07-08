[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Sfeyt03D)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19884477&assignment_repo_type=AssignmentRepo)
# Lab 2

*Course:* Intro to Data & Computing  
*Session date:* **July 2, 2025 – Afternoon (4 h)**  
*Environment:* `lab_2` (conda/mamba)

---

## 1  Learning objectives

1. Write Python functions using loops, conditionals, and data structures.
2. Introduced to unit tests with **pytest** to verify correctness.
3. Figure out what pre-written code does (comment _validate_numeric)
4. Track changes with **Git** and publish to **GitHub**. 

---

## 2  Repository layout

| Path | Purpose |
|------|---------|
| `assignment.py` | **Your code** — implement 4 statistics utilities. |
| `test_assignment.py` | Autograder & local tests (do **not** edit). |
| `requirements.txt` | Package list used by GitHub Actions & mamba env. |
| `.github/workflows/autograding.yaml` | CI workflow that runs tests on every push. |

---

## 3  Setup ( one‑time)

Make sure you have accepted the assignemnt and you have cloned the repo locally and you can push it back to github to turn it in. 

Open a terminal and run:

### 3.1 Create isolated env
```bash
mamba create -n lab_2 python=3.11 -y
```

### 3.2 Activate it
```bash
mamba activate lab_2
```
### 3.3 Install required pkgs
```bash
mamba install --file requirements.txt -y
```
#### Why mamba? Faster dependency resolution and the environment.yml you export later will be portable across platforms.


## 4  Assignment tasks

All edits happen only in assignment.py.

| Function | Description |
|------|---------|
| `mean_loop(nums)` | Compute arithmetic mean **without** built‑in sum. |
| `median_loop(nums)` | Compute median (manual sort allowed). |
| `summary_stats(nums)` | Return {"mean": …, "median": …, "min": …, "max": …}. |
| `quantile(nums, q)` | Generic quantile (0 ≤ q ≤ 1) using linear interpolation. |


### 4.1  Implementation rules

- Accept any sequence‑like object (list, tuple, numpy.ndarray).
- Raise ValueError on empty input; raise TypeError if a non‑numeric value is found.
- Add Google‑style docstrings and type hints.

### 4.2  Run tests locally

```bash
pytest -q
```
A green check means all tests pass.

###  4.3  Commit & push
```bash
git add assignment.py
git commit -m "Finish mean_loop and median_loop"
git push origin main
```
GitHub Actions will run pytest automatically (see the Checks tab).

###  4.4  Reflect

Please write a reflection (1-2 paragraphs is fine) on what was the most challenging part of today and push it as a .txt file. 

Remember: GitHub Actions will run pytest automatically (see the Checks tab).
