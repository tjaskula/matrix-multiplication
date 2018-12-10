#! /usr/bin/env python
import sys
import pyspark
from pyspark.sql import SparkSession
from pyspark.mllib.linalg.distributed import CoordinateMatrix, MatrixEntry, BlockMatrix
import operator
from contextlib import contextmanager
import time
import logging

import os
os.environ['PYSPARK_PYTHON'] = '/usr/local/anaconda3/envs/spark/bin/python3'

@contextmanager
def time_usage(name=""):
    """log the time usage in a code block
    prefix: the prefix text to show
    """
    start = time.time()
    yield
    end = time.time()
    elapsed_seconds = float("%.4f" % (end - start))
    logging.info('%s: elapsed seconds: %s', name, elapsed_seconds)


logging.getLogger().setLevel(logging.INFO)

def to_matrix_entry(x):
    i, j, v = x.split(',')
    return MatrixEntry(i, j, v)

sc = pyspark.SparkContext(appName="Matrix Multiplication")

for i in range(1, 10):
    with time_usage("temps matrix multiplication"):
        matrix_a_raw = sc.textFile(sys.argv[1])
        matrix_b_raw = sc.textFile(sys.argv[2])

        spark = SparkSession(sc)

        entries_a = matrix_a_raw.map(to_matrix_entry)
        entries_b = matrix_b_raw.map(to_matrix_entry)

        mat_a = CoordinateMatrix(entries_a).toBlockMatrix()
        mat_b = CoordinateMatrix(entries_b).toBlockMatrix()

        product = mat_a.multiply(mat_b)
        product.toLocalMatrix()

#for t in result:
    #print('%s, %s, %s' % (t[0], t[1], t[2]))