# Unclosed File Bug in Python

This repository demonstrates a common error in Python: forgetting to close a file after opening it.  This can lead to resource leaks and potential performance problems, particularly in applications that handle many files.

The `bug.py` file shows the code with the unclosed file, while `bugSolution.py` demonstrates the corrected version with proper file closure.

**How to Reproduce the Bug:**

1. Run `bug.py`.  You might not immediately see an error, but if the script is run many times, or with files that are very large, resources are not being released correctly which could cause a significant issue.  You can use task manager (or similar system monitor) to see that files are held open by the process.
2. Observe the behavior, then compare to the corrected version.

**Solution:**

Always close files using the `close()` method or use a context manager (`with open(...) as f:`). The `bugSolution.py` demonstrates the corrected code using a context manager. 