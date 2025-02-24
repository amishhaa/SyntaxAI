# SyntaxAI  
**Spend your time creating, not correcting.**

---

## Project Overview  
SyntaxAI is an **Intelligent IDE** powered by an AI model trained on **Abstract Syntax Trees (ASTs)** to provide accurate, bug-free code generation and auto-completion. Unlike traditional Large Language Models (LLMs) that rely on surface-level tokenization, SyntaxAI focuses on the **backbone of code** (ASTs) to eliminate biases caused by variable naming and formatting. This approach ensures higher accuracy, fewer bugs, and increased developer productivity.

---

## Problem Statement  
Developers today rely heavily on LLMs for code completion, but these models often generate code with **syntactical and logical errors**, leading to frustration and wasted time debugging. This happens because LLMs are trained on code as if it were prose, ignoring the structural and logical nuances that make code unique. 
SyntaxAI addresses this by training AI models on **ASTs**, the structural representation of code, to provide more accurate and context-aware suggestions. This reduces errors, improves code quality, and allows developers to focus on solving problems rather than fixing bugs.

---

## Key Features  
- **AST-Based Code Generation**:  
  Generates code based on the structural backbone of programs, ensuring logical correctness.  
  Ignores superficial differences like variable names, focusing on the code's true meaning.
  Uses Python's 'ast' module to parse the code into ASTs.

- **Self-Learning Model**:  
  Uses a **reward-based system** to learn from user interactions.  
  Assigns positive weights to successful code snippets and negative weights to buggy ones, improving over time.

- **Lightweight and Customizable**:  
  Designed to be lightweight and easy to integrate with existing IDEs with the training data only being ~1000 lines and model of ~50 lines. 
  Supports automatic code formatting in accordance with style guides.

- **Real-Time Suggestions and Learning**:  
  Provides context-aware code suggestions as you type, reducing the need for manual corrections and learns from your code in real time.

---

## How It Works  
1. **Training Data**:  
   The model is trained on a dataset of Python code converted into ASTs using Python's built-in `ast` module.  

2. **AST Parsing**:  
   Code is broken down into nodes and subnodes, representing its logical structure.  

3. **Graph-Based Learning**:  
   Nodes are connected in a graph-like structure, with weights assigned based on their likelihood of appearing together.  
   The model uses a **greedy reward system** to suggest the most probable and profitable code snippets.  

4. **User Interaction**:  
   As users write code, the model learns from their actions, improving its suggestions over time.  

---

## Screenshots  
![Screenshot 2025-02-23 170411](https://github.com/user-attachments/assets/800af1a3-d4d0-42b1-8321-7ba2b897d088)
![Screenshot 2025-02-23 173323](https://github.com/user-attachments/assets/1eb5db94-3449-4c96-b68c-9250dba10308)

## Dependencies  
- **Python** (pre-installed)  
- **Flask**: Install using pip:  
  ```bash  
  pip install flask  
---

## Getting Started  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/amishhaa/SyntaxAI.git  
