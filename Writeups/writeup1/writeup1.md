# Write-up 1: Setup

**Name:** Krishna Sharma  
**Student ID:** ksharma2  
**Date:** 11/11/2025  

---

## Overview

Write-up 1 questions from the Setup assingment (11/12).

---

## Content


1. How many slurm job will be submitted?

3 slurm jobs will be submitted, as noted by the array of 0-2.

2. What is the purpose of the if statement?

The if statement serves to divide the lines of the data.txt file between each of the 3 jobs.

3. What is the expected output in each *.out file?

The expected output in each file is “$i: $value” which is each job printing its results. Each job will have 2 lines to process.
So, 
SLURM_ARRAY_TASK_ID=0 will have 0:12, 3:8
SLURM_ARRAY_TASK_ID=1 will have 1:7, 4:27
SLURM_ARRAY_TASK_ID=2 will have 2:91, 5:30

---

This is the main part of your write-up.  
You can include explanations, examples, and notes 

You can use some text formating, lists, and tables to imporve the write-up readability
#### **Text Formatting**

You can make text **bold**, *italic*, or even ***bold and italic*** for emphasis.

#### **Lists**

**Unordered list:**
- Apple  
- Banana  
- Cherry  

**Ordered list:**
1. First step  
2. Second step  
3. Third step  

#### **Table Example**

| Tool | Description         | Example Command        |
|------|---------------------|------------------------|
| `ls` | Lists files         | `ls -la`               |
| `grep` | Searches text     | `grep "pattern" file.txt` |
| `wc` | Counts words/lines  | `wc -l filename.txt`   |

Code snippets and images are highly recommended to document your work.

#### **Code Examples**

**Inline code example:** Use the `print()` function to display text.  

**Code block example:**

```bash
# Example command line code
echo "Hello, Markdown!"
```

```python
# Example Python code
for i in range(3):
    print("Iteration:", i)
```

For longer script, you can say something like, `script1.py` contains functions for reading fasta file. Ideally, all codes you run should be saved in corresponding files. 


#### **Image Example**

![Example placeholder image](./snyderlab.png)

#### **Link Example**

Learn more about Markdown syntax here:  
[Markdown Guide](https://www.markdownguide.org/basic-syntax/)

---


## Acknowledgement

