import math
from typing import List
import hashlib

from .hash_generator import HashGeneratorBJKST

class BJKSTSketch:
    """
    The BJKST sketch is a probabilistic data structure
    that serves as a distinct element counter in a stream of data.

    It uses two hash functions and a set to estimate the number of distinct elements.
    It operates in sub-linear space, at the expense of some approximation error.

    The BJKST algorithm was invented by Bar-Yossef, Jayram, Kumar, Sivakumar, and Trevisan.
    """

    def __init__(self, n: int, b: float, c: float, epsilon: float):
        """
        Initializes BJKST Sketch class.

        Parameters
        ----------
        n: int
            Size of the input universe.

        c: float
            Constant factor for size of set B.

        epsilon: float
            Approximation error factor.
        """
        self.n = n
        self.b = b
        self.c = c
        self.epsilon = epsilon
        self.z = 0
        self.B = set()
        self.g_size = int(b * n * (epsilon ** (-4)) * (math.log(n) ** 2))

    @staticmethod
    def zeros(p: int) -> int:
        """
        Returns the number of trailing zeros in the binary representation of p.

        Parameters
        ----------
        p: int
            Input integer.

        Returns
        -------
        int
            Number of trailing zeros in the binary representation of p.
        """
        count = 0
        while p % 2 == 0 and p > 0:
            count += 1
            p = p // 2
        return count

    def sha256_hash(self, s: str, m: int) -> int:
        """
        Hashes the input string using the SHA-256 algorithm and maps the result to a specified range.

        Parameters
        ----------
        s: str
            Input string to be hashed.
        m: int
            The size of the output range, where the hash value will be mapped to an integer in [0, m).

        Returns
        -------
        int
            The hash value of the input string modulo m, an integer in the range [0, m).
        """
        s = s.encode()  # Convert the string to bytes
        hash_object = hashlib.sha256()
        hash_object.update(s)
        hash_value = int(hash_object.hexdigest(), 16)  # Convert the hex digest to an integer
        return hash_value % m

    def process_stream(self, stream: List[object]) -> None:
        """
        Executes the BJKST algorithm on a stream (list) of elements.

        Parameters
        ----------
        stream: List[object]
            Stream of objects represented as a list.
        """
        for token in stream:
            h_j = self.sha256_hash(token, self.n)
            zeros_hj = self.zeros(h_j)
            if zeros_hj >= self.z:
                g_j = self.sha256_hash(token, self.g_size) 
                self.B.add((g_j, zeros_hj))

                while len(self.B) >= self.c / (self.epsilon ** 2):
                    self.z += 1
                    self.B = {(a, b) for (a, b) in self.B if b >= self.z}

    # def process_stream(self, stream: List[object]) -> None:
    #     for token in stream:
    #         h_j = self.h_generator.hash(token)
    #         zeros_hj = self.zeros(h_j)
    #         if zeros_hj >= self.z:
    #             g_j = self.g_generator.hash(token)
    #             self.B.add((g_j, zeros_hj))

    #             while len(self.B) >= self.c / (self.epsilon ** 2):
    #                 self.z += 1
    #                 self.B = {(a, b) for (a, b) in self.B if b >= self.z}

    def estimate_distinct_elements(self) -> int:
        """
        Returns the estimated number of distinct elements in the stream.

        Returns
        -------
        int
            Estimated number of distinct elements.
        """
        return len(self.B) * (2 ** self.z)
