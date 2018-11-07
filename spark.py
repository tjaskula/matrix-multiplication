import sys

matrix_a_txt = spark.sparkContext.textFile("file:///users/huwe18/mapreduce/projet_matrices/matricequedes1.txt")

matrix_b_txt = spark.sparkContext.textFile("file:///users/huwe18/mapreduce/projet_matrices/matricequedes1.txt")

matrix_a_txt.take(20)
matrix_b_txt.take(20)

def mapper_zhushou_a(x):
    x = x.split()
    i = int(x[0])
    j = int(x[1])
    v = int(x[2])
    return (j,(i,v))

matrix_a = matrix_a_txt.map(lambda x: mapper_zhushou_a(x))

matrix_a.take(20)

def mapper_zhushou_b(x):
    x = x.split()
    j = int(x[0])
    k = int(x[1])
    v = int(x[2])
    return (j,(k,v))

matrix_b = matrix_b_txt.map(lambda x: mapper_zhushou_b(x))

matrix_b.take(20)

groupe_ab = matrix_a.cogroup(matrix_b)

groupe_ab.take(20)

def flatMap_zhushou(x):
    j = x[0]
    list_a = x[1][0]
    list_b = x[1][1]
    return([((a[0], b[0]), a[1]*b[1]) for a in list_a for b in list_b])

resultat_avant_addition = groupe_ab.flatMap(lambda x: flatMap_zhushou(x))

resultat_avant_addition.take(100)

resultat_final = resultat_avant_addition.reduceByKey(lambda x, y : x+y)

resultat_final.take(100)

def finalmap_zhushou(x):
    ((i, k), v) = x
    return (str(i) + ' ' + str(k) + ' ' + str(v))

resultat_txt = resultat_final.map(lambda x: finalmap_zhushou(x))

resultat_txt.take(100)

