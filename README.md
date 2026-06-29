# Worst HVAC Systems — Hadoop MapReduce on GCP

A big data analysis project using **Hadoop MapReduce** (Python) on **Google Cloud Platform** to identify underperforming HVAC systems across a campus of buildings.

## Problem Statement

Replacing HVAC systems is costly. To prioritize replacements, we analyze sensor data across all buildings to find:

1. **The 3 worst HVAC systems** — defined as the greatest sustained difference between desired temperature and actual temperature
2. **The 3 hottest buildings** during normal business hours (based on actual temperature readings)

## Architecture

```
HVAC Sensor Dataset  →  HDFS  →  Hadoop MapReduce (Python)  →  Ranked Results
```

Runs in **pseudo-distributed mode** on a single GCP VM — no Hive or other add-ons; all processing is done within Hadoop 2.10.1.

## Tech Stack

| Component | Technology |
|-----------|------------|
| Data processing | Hadoop 2.10.1 MapReduce |
| Language | Python (mapper + reducer scripts) |
| Cloud platform | Google Cloud Platform (GCP) |
| VM OS | Ubuntu 18.04 |

## Setup

### Part 1 — GCP Account
Create a free-tier GCP account at [cloud.google.com](https://cloud.google.com).

### Part 2 — Create VM
Provision an Ubuntu 18.04 VM instance from GCP Compute Engine.

### Part 3 — Install Hadoop
```bash
# Install Java
sudo apt-get install openjdk-8-jdk

# Download and configure Hadoop 2.10.1
wget https://downloads.apache.org/hadoop/common/hadoop-2.10.1/hadoop-2.10.1.tar.gz
tar -xzf hadoop-2.10.1.tar.gz
# ... configure core-site.xml, hdfs-site.xml, mapred-site.xml
```

### Part 4 — Start Hadoop
```bash
hdfs namenode -format
start-dfs.sh
start-mapred.sh
```

### Part 5 — Run Analysis
```bash
# Upload dataset to HDFS
hdfs dfs -put hvac_data.csv /input/

# Run MapReduce job (worst HVAC systems)
hadoop jar hadoop-streaming.jar \
  -mapper mapper_hvac.py \
  -reducer reducer_hvac.py \
  -input /input/hvac_data.csv \
  -output /output/worst_hvac

# Run MapReduce job (hottest buildings)
hadoop jar hadoop-streaming.jar \
  -mapper mapper_buildings.py \
  -reducer reducer_buildings.py \
  -input /input/hvac_data.csv \
  -output /output/hottest_buildings
```

## Metrics

- **Worst HVAC**: ranked by `|desired_temp - actual_temp|` averaged across all readings
- **Hottest buildings**: ranked by average `actual_temp` during business hours (9am–5pm)
