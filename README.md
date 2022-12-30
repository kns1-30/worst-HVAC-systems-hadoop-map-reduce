# worst-HVAC-systems-hadoop-map-reduce
To find 
1. The 3 worst HVAC systems, based on all available data (where “worst” means the greatest difference between desired temperature and actual temperature) 
2. The 3 hottest buildings, based on all available data, during normal business hours.

Replacing existing heating/cooling (“HVAC”) systems can have a significant impact on the environment
(as well as saving some money!) But in the absence of an outright failed system, identifying the specific
system to replace can be challenging – one must consider years in service, efficiency of the unit,
maintenance cost/records, general comfort level, user complaints, tax benefits, etc. We are going to do some analysis that could help us make such a decision. You are given a dataset of
measurements from a small collection of buildings. Used Hadoop to find
1. The 3 worst HVAC systems, based on all available data (where “worst” means the greatest difference between desired temperature and actual temperature) 
2. The 3 hottest buildings, based on all available data, during normal business hours.

Steps:
Part 1: Create an account for Google Cloud Platform

Part 2: Create an Ubuntu 18.04 VM instance from Google Cloud Platform

Part 3: Install/Configure Hadoop on GCP Ubuntu 18.04 Server

Part 4: Initialize and boot Hadoop

Part 5: Analyze HVAC dataset (python)
Using Python, two separate Map/Reduce programs using Hadoop 2.10.1 are written on
GCP to compute the following using the sample HVAC data. Ran the
programs via Hadoop 2.10.1 pseudo-distributed mode on an GCP instance. No “add-on” used to
Hadoop (such as Hive). The great majority of the data processing is performed within Hadoop.
