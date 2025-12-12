# Write-up 4: Pipeline

**Name:** Krishna Sharma  
**Student ID:** ksharma2  
**Date:** 11/20/2025  

---

## Overview

Write-Up 4 for Pipeline.

---

## Content

SLURM Pipeline

How could you add a differential expression analysis (DESeq2) step to the rnaseq_pipeline_array_depend.sh script so that it runs only after all salmon jobs have finished?

I would add an afterok dependency that waits for all Salmon Jobs to be completed. This will wait for all the tasks in the array to be complete and will not run if a task fails. First submit the Samon array with sbatch and the output will be a job ID. Use that job ID to write the dependency with afterok when submitting the DESeq2 script. Thus, DESeq2 will only run its script after all salmon jobs are finished successfully.

Made edits to rna_seq_nf pipeline as outlined in pipeline.md


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

