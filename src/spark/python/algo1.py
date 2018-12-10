#! /usr/bin/env python
import sys
import pyspark
from pyspark.sql import SparkSession
from pyspark.mllib.linalg.distributed import CoordinateMatrix, MatrixEntry
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

def to_matrix_a(x):
    i, j, v = x.split(',')
    return (j, (i, v))

def to_matrix_b(x):
    j, k, v = x.split(',')
    return (j, (k, v))

def to_matrix_entry(x):
    i, j, v = x.split()
    return MatrixEntry(i, j, v)

def multiply_mat(x):
    left = x[1][0]
    right = x[1][1]
    i, v = left
    k, w = right
    return ((i, k), (int(v) * int(w)))

sc = pyspark.SparkContext(appName="Matrix Multiplication")

for i in range(1, 10):
    with time_usage("temps matrix multiplication"):
        matrix_a_raw = sc.textFile(sys.argv[1])
        matrix_b_raw = sc.textFile(sys.argv[2])

        spark = SparkSession(sc)

        entries_a = matrix_a_raw.map(to_matrix_a)
        entries_b = matrix_b_raw.map(to_matrix_b)

        product_entries = entries_a \
            .join(entries_b) \
            .map(multiply_mat) \
            .reduceByKey(operator.add) \
            .map(lambda x:  (x[0][0], x[0][1], x[1]))

        result = product_entries.collect()

#for t in result:
    #print('%s, %s, %s' % (t[0], t[1], t[2]))