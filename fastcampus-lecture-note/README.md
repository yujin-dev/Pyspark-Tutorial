# Hadoop
HDFS라는 분산 파일 시스템으로 구성되며 내부적으로 name node - data node로 이루어진다. 
name node에서 전체 클러스터를 총괄하고 각 data node는 block으로 이루어진다.  
MapReduce라는 각 data node에서 병렬로 데이터를 필터링하거나 처리(Map)하고, 전체를 정렬하거나 집계(Reduce)한다. 각 data node에서 처리하여 네트워크 병목 현상을 방지하고 병렬로 실행하여 보다 빠르게 실행될 수 있도록 한다.  
Hive는 HDFS 시스템에서 보다 편리한 쿼리 실행이 가능하도록 한다.

### Summary
**How many ways can you import a large file to HDFS?**  
- Ambari or CLI

**I have a spark job in Hadoop that I can not stop and don’t know what to do. Can you find out what’s going on with the spark job and kill persistent spark jobs through YARN?**
- Yarn application –list
- Yarn logs –applicationId [ ] –log_files [ ]
- Yarn application –kill AppID

**Explain MapReduce**
- Programing framework that allow us to perform distributed and parallel processing on a large data set in multiple servers

**What happends when two clients try to access the same file in the HDFS?**  
- HDFS supports exclusive writes only. The file is locked by Namenode which grants a lease to the first client who opened it.

**How do you define <i>block</i> in HDFS? What is the default block size in Hadoop 1 and in Hadoop 2? Can it be changed?**  
- Blocks are smallest location on your HD. 
- Files in HDFS are broken down into block-sized chunks. Default blocksize is 128MB. The block size can be configured.

**What will you do when NameNode is down?**  
- Use the file sytem metadata replica to start a new NameNode
(Configure datanodes so that they can acknolowedge the new namenode)

**What does jps command do?**  
- The ‘jps’ command helps us to check if the Hadoop daemons are running or not. It shows all the Hadoop daemons that are running on the machine

**State the reason why we can’t perform <i>aggregation</i>(addition) in mapper? Why do we need the <i>reducer</i> for this?**  
- We cannot perform “aggregation” (addition) in mapper because sorting does not occur in the “mapper” function. Sorting occurs only on the reducer side

**Explain <i>Distributed Cache</i> in a MapReduce Framework**  
- A facility provided by the MapReduce framework to cache files needed by applications

**How do <i>reducers</i> communicate with each other?**  
- They don't communicate with each other. They run in isolation

**What does a <i>MapReduce Partitioner</i> do?**  
- It make sure that all the values of a single key go to the same **reducer**, thus allowing even distribution of the map output over the reducers

**What do you know about <i>SequenceFileInputFormat</i>?**  
- It is a specific compressed binary file format which is optimized for passing the data between the outputs of one MR job to the input of some other MRjob

# Spark 
Spark는 데이터 처리 엔진이다.  
스토리지와 컴퓨팅 리소스를 분리하여 자원 낭비를 방지한다.
### Summary
**What is spark engine's responsibility?**  
- It's responsible for scheduling and distributing and monitoring application across the clusters

**How does Spark partition the data?**  
- Spark uses MR API to do the data partitioning. In input format, you can create number of partitions.

**What are common Spark Ecosytems?**  
- Spark SQL, Spark streaming, MLLib, GraphX, SparkR, BlinkDB


**How Spark store the data?**
- Spark is a processing engine. It can retrieve data from any storage engine like HDFS or S3, and others


**What is SparkContext?**  
- It's a master driver program and sets up internal services and establishes a connection to a Spark execution environment. When creating RDDs, SparkContext connect to the spark cluster to create new spark context object.

**What is SparkCore functionalities?** 
- Spark core is base engine of spark FW. It controls memory mgmt, fault tolarance, scheduling, and monitoring jobs, interacting with data stores.

**How SparkSQL is different from HQL and SQL?**
- SparkSQL is a component of SparkCore engine that support SQL. and HQL without changing any syntax. It's possible to join SQL tables and HQL tables
 
**When did we use Spark Streaming?**
- ßIs a real-time processing of streaming data API. Spark streaming gather streaming data from different sources

**Why partitions are immutable?**
- Every transformation creates new partitions. Partitions use HDFS API so they are immutable, distributed, and fault tolerant.

**What is Spark MLlib?**
- Mahout is a ML library for hadoop, similarly MLlib is a Spark library. MLlib provdies algorithms that can scale out on the cluster for data processing

**How Spark Streaming API works?**
- We configure specific time window, all data collected during this time window, data seperates as a batch. The input stream goes into spark streaming

**What are broadcast variable?**
- Broadcast variable keep a readonly variable cached on each machine, rather than shipping a copy with a task