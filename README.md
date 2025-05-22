# 🧮 Mechanical System Simulator with Runge-Kutta Solver

This Python project simulates a **mass-spring-damper system** using the **4th-order Runge-Kutta method**. It includes data visualization, exporting simulation results to various formats (Excel, text, `.dat`, SQLite database), and supports reading them back for inspection or further analysis.

---

## 📦 Features

- 📐 Numerical simulation of 2nd-order ODE systems
- 🧠 4th-order **Runge-Kutta** solver for high-accuracy results
- 📈 Matplotlib-based visualization (displacement & velocity vs time)
- 📁 Export results to:
  - Excel (.xlsx)
  - Plain text (.txt)
  - Dat file (.dat)
  - SQLite database (.db)
- 🔁 Reload results from stored files

---

### 🧪 Physical Model

Simulates a **mass-spring-damper** system governed by:

m * x'' + c * x' + k * x = F


Where:
- `m`: mass
- `c`: damping coefficient
- `k`: spring constant
- `F`: external force
- `x`: displacement

---

##### 🚀 How to Use

### 1. Run the Simulation

```bash
python simulation.py
```

This will:

Simulate the system for a given total time

Visualize displacement and velocity

Save results to files

**2. Files Generated**

simulation_data_runge_kutta.xlsx (Excel with sheets for results and parameters)

simulation_data_runge_kutta.txt

simulation_data_runge_kutta.dat

simulation_data_runge_kutta.db (SQLite)

###### ⚙️ Configurable Parameters

You can adjust the following in __main__:
```
solver = SystemSolver(
    mass=1.0,
    damping_coefficient=0.2,
    spring_constant=2.0,
    force=1.0,
    sampling_frequency=100,
    total_time=10.0
)
```
