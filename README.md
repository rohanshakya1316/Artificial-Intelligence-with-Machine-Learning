# Artificial Intelligence & Machine Learning Repository

Welcome to this repository! This project contains clean Python implementations of classic Artificial Intelligence (AI) search algorithms, Constraint Satisfaction Problems (CSPs), game-playing heuristics, and fundamental Machine Learning (ML) models.

The code is organized into two primary categories: foundational **Problem Solving** techniques and basic **Machine Learning and Neural Networks**.

---

## 📁 Repository Structure

```text
├── 📂 Machine Learning and Neural Network
│   ├── 🐍 and_or_not_xor_gates.py              # Implementation of basic logic gates using perceptrons
│   ├── 🐍 complex_back_propagation_algorithm.py # Advanced neural network with backpropagation
│   └── 🐍 simple_back_propagation_algorithm.py  # Foundational backpropagation learning model
│
└── 📂 Problem Solving
    ├── 🐍 simple_A_asterisk.py                 # Basic A* Search implementation
    ├── 🐍 improved_A_asterisk.py               # Optimized A* Search algorithm
    ├── 🐍 advanced_A_asterisk.py               # High-efficiency A* Search variant
    │
    ├── 🐍 simple_bfs.py                        # Standard Breadth-First Search
    ├── 🐍 advanced_bfs.py                      # Advanced/optimized Breadth-First Search
    │
    ├── 🐍 simple_dfs.py                        # Standard Depth-First Search
    ├── 🐍 advanced_dfs.py                      # Advanced/optimized Depth-First Search
    │
    ├── 🐍 simple_uniform_cost_search.py        # Baseline Uniform Cost Search (Dijkstra variant)
    ├── 🐍 advanced_uniform_cost_search.py      # Optimized Uniform Cost Search
    │
    ├── 🐍 simple_greedy_best_first_search.py   # Baseline Greedy Best-First Search
    ├── 🐍 advanced_greedy_best_first_search.py # Optimized Greedy Best-First Search
    │
    ├── 🐍 simple_alpha_beta_pruning.py         # Standard Alpha-Beta pruning technique
    ├── 🐍 advanced_alpha_beta_pruning.py       # Advanced Alpha-Beta heuristic tree pruning
    ├── 🐍 minimax_algo_with_alpha_beta_pruning.py # Classic Minimax adversarial search tree
    │
    ├── 🐍 simple_graph_coloring_problem.py    # Basic CSP graph coloring approach
    ├── 🐍 advanced_graph_coloring_problem.py  # Heuristic-driven graph coloring solution
    │
    ├── 🐍 n_queens_problem.py                  # Standard N-Queens puzzle solver
    ├── 🐍 simple_n_queens_problem.py           # Alternative baseline N-Queens approach
    ├── 🐍 improved_n_queens_problem.py         # Optimized backtracking N-Queens algorithm
    │
    ├── 🐍 simple_tic_tac_toe.py                # Text-based / Basic Tic-Tac-Toe AI
    ├── 🐍 advanced_tic_tac_toe.py              # Unbeatable Tic-Tac-Toe AI using Minimax
    │
    ├── 🐍 simple_vacuum_cleaner_simulation.py  # Basic reflex vacuum cleaner agent
    └── 🐍 advanced_vacuum_cleaner_simulation.py# Smart/state-based vacuum cleaner simulation
```

---

## 🚀 Getting Started

### Prerequisites
Make sure you have **Python 3.x** installed on your system. 

### Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com
   ```
2. Navigate into the project directory:
   ```bash
   cd your-repo-name
   ```

### Running the Scripts
You can execute any of the Python files directly from your terminal. For example, to run the graph coloring problem solver:
```bash
python "Problem Solving/simple_graph_coloring_problem.py"
```

---

## 🧠 Algorithmic Concepts Covered

* **Uninformed Search:** Breadth-First Search (BFS), Depth-First Search (DFS), and Uniform Cost Search (UCS).
* **Informed (Heuristic) Search:** A* Search and Greedy Best-First Search.
* **Adversarial Search (Game Theory):** Minimax Decision Tree and Alpha-Beta Pruning optimized for Tic-Tac-Toe.
* **Constraint Satisfaction Problems (CSPs):** Backtracking algorithms for Graph Coloring and the N-Queens Problem.
* **Intelligent Agents:** Reflex and state-based simulations (Vacuum Cleaner Problem).
* **Neural Foundations:** Linear classifiers for logic gates (AND, OR, NOT, XOR) and gradient descent via Backpropagation.

---

## 📝 License
This repository is open-source and available under the [MIT License](LICENSE).
