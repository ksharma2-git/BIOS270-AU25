# Write-up 2: Environment

**Name:** Krishna Sharma  
**Student ID:** ksharma2  
**Date:** 11/18/2025  

---

## Overview

Write-Up 3 for Data.

---

## Content

Database:

1. Create an SQL Database

How many tables will be created in the database?

3 tables will be created in the database.

In the insert_gff_table.py script you submitted, explain the logic of using try and except. Why is this necessary?

The script tries to insert some data from a table into the SQL database. If it fails, like if the database is locked, then the script will try again. If the error is due to another reason, then an error message will be raised. This is necessary because it wants to avoid raising an error and the table is very large, so it is trying to write in a lot of different entries at the same time. So, the “database is locked” error may appear. Hence, the script will sometimes wait for a moment and retry and only raise an error that is not caused by the above message.


2. Query the Created Database

Complete the TODO section in query_bacteria_db.py.

query = "SELECT DISTINCT record_id FROM gff"
query = "CREATE INDEX IF NOT EXISTS record_id_index2 ON gff(record_id)"

Record the runtime - if it takes too long, you may stop the session early. Then, uncomment db.index_record_ids() and note how the runtime changes. What do you observe, and why do you think this happens?

Without the index, the run time took about 8 minutes. With the index, the run time was much quicker and finished the job in about 30 seconds. The index allows SQL to not have to go through the entire GFF table and instead use the index of the desired column and search through each of the rows, without having to go through the entire table.;ets


3. Upload to Google BigQuery

Explain the role of CHUNK_SIZE and why it is necessary

CHUNK_SIZE divides the rows that are read from an SQL table into blocks, so that these can be uploaded to BigQuery. It is necessary because it is difficult for the machine, with limited RAM, to read in the whole table at once so it chunks into smaller pieces at a time. Otherwise, python may crash or you may run out of memory on the system.

4. HDF5 Data

Explain why the following chunk configuration makes sense - what kind of data access pattern is expected, and why does this align with biological use cases?

Data is chunked in sizes of 1000 rows at a time or 1000 proteins at a time. This aligns with biological use cases because we often want a chunk of proteins to be considered together for a particular pattern or cluster that are of particular interest.



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

