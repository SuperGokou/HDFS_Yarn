# Hadoop Setup and Data Processing

## Overview

This project, completed by Ming Xia for CS 454 at Washington State University Vancouver under the instruction of Ben McCamish, involves setting up Hadoop on an Ubuntu operating system and utilizing it to process and reduce data. This README outlines the setup process and how to run the data processing tasks using Hadoop.

## Introduction

The goal of this project is to demonstrate the ability to install, configure, and utilize Hadoop for processing large datasets. The data processing involves mapping data entries to key-value pairs and reducing them to summarize information effectively.

## Installation and Setup

### Requirements

- Ubuntu OS (Version specifics recommended)
- Hadoop (Version 2.7.1 used in examples)
- Java (Required for running Hadoop)
- Python (For writing mapper and reducer scripts)
- VirtualBox and Cloudera (Optional, for a virtualized environment)

### Hadoop Installation

There are two main methods to install Hadoop for this project:

#### 1. Using Cloudera on VirtualBox (Subscription Required)

1. **Download and Install VirtualBox**: [Download here](https://www.virtualbox.org/wiki/Downloads)
2. **Install Cloudera**: Download from [Cloudera's site](https://www.cloudera.com/downloads.html) and set it up on VirtualBox.
   - Ensure virtualization is enabled in BIOS if you encounter any related errors.

#### 2. Local Installation Without Virtual Machine

1. **Download Hadoop**: [Apache Hadoop](http://hadoop.apache.org)
2. **Configure SSH**: Ensure you can SSH into your localhost without a password.
3. **Environment Setup**: Configure Hadoop and Java environment variables.
4. **Modify Hadoop Configuration Files**: Update settings in `core-site.xml`, `hdfs-site.xml`, `mapred-site.xml`, and `yarn-site.xml` as per your local setup requirements.

### Starting Hadoop Services

- Format HDFS using `bin/hdfs namenode -format`.
- Start DFS and Yarn services using the scripts found in `sbin` directory.

## Running the Application

### Data Processing Tasks


## Submission Details

- Submit a ZIP file containing all necessary code files, a detailed README, and output files via Canvas.

## Extra Credit Opportunities

- Implement additional features like support for handling more complex data types or improving the efficiency of data processing tasks.

## Licensing

This project is licensed under the MIT License - see the LICENSE file for details.


1. **Prepare Input Data**: Upload data to the Hadoop file system.
2. **Execute MapReduce Job**:
