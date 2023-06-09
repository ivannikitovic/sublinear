# sublinear

Python library implementing a subset of streaming algorithms. Includes variations of these algorithms (e.g. adversarially robust), as well as support for multiple data types.

## :computer: Installation

``pip install sublinear``

## :zap: Algorithms

Here is the list of the currently implemented streaming algorithms.

### F0 Estimation (Count of Distinct Elements)

- BJKST Sketch (basic, plus, adversarially robust) [1]

- HyperLogLog [2]

### F1 Estimation (Length of Stream)

- Morris (basic, plus, plus plus) [3][4]

### F2 Estimation (Estimate of Second Moment)

- AMS Sketch (basic, plus, plus plus) [5]

### Frequency Table Estimation

- Count Min Sketch [6]

### Heavy Hitters

- Misra-Gries Sketch [7]

### Other

- K Independent Hash Function [8]

## :book: Bibliography

[1] Bar-Yossef, Ziv, et al. "Counting distinct elements in a data stream." Randomization and Approximation Techniques in Computer Science. Springer Berlin Heidelberg, 2002.

[2] Flajolet, Philippe, et al. "HyperLogLog: the analysis of a near-optimal cardinality estimation algorithm." Conference on Analysis of Algorithms. Springer Berlin Heidelberg, 2007.

[3] Morris, R. "Counting large numbers of events in small registers". Communications of the ACM 21, 10, 1978.

[4] Flajolet, P. "Approximate Counting: A Detailed Analysis". BIT 25, 1985.

[5] Noga Alon, Yossi Matias, Mario Szegedy,
"The Space Complexity of Approximating the Frequency Moments".
Journal of Computer and System Sciences,
Volume 58, Issue 1,
1999.

[6] Cormode, Graham; S. Muthukrishnan. "An Improved Data Stream Summary: The Count-Min Sketch and its Applications". 2005.

[7] Misra, J.; Gries, David. "Finding repeated elements". Science of Computer Programming. 1982

[8] Wegman, Mark N., et al. "New Hash Functions and Their Use in Authentication and Set Equality". Journal of Computer and System Sciences. 1981.
