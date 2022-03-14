# Hadoop

## Summary
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