# IPv4 Address Aggregator

This project contains a Python script and Docker setup to aggregate IPv4 subnets into the least number of subnets possible without losing any data. The input and output are in CSV format.

## Project Structure

- `Final_ipv4_addr_aggr.py`: A standalone Python script that aggregates IPv4 subnets and also segragates the IDs as well.
- `Dockerfile`: A Dockerfile that sets up a Python environment with the required packages.
- `tufin-docker-run.sh`: A bash script to build the Docker image and run the container to process the input data.

## Final_ipv4_addr_aggr.py
This script reads a CSV file containing lines of IPv4 subnets and aggregates them. The output is another CSV file with the aggregated subnets.

### Example
Input: `123:10.10.10.0/24,10.10.11.0/24,10.10.12.0/24`
Output: `123,10.10.10.0/23;10.10.12.0/24`

## Dockerfile
The Dockerfile sets up a minimal Python environment to run the script. It installs the necessary Python packages.

-To build the Docker image, run:
`docker build -t tufin-app .`

## tufin-docker-run.sh
This bash script builds the Docker image and runs a container to process the input CSV file, writing the output to the current working directory.

-Usage
Place your input CSV file (coalesce_input.csv) in the current working directory.
Run the script:
`./tufin-docker-run.sh`

This `README.md` file covers the key points of this project, providing clear instructions on how to use the Python script, Dockerfile, and bash script, as well as explaining the purpose and usage of each component.
