# Author = Sahil Bharaj

import netaddr
import csv

def convert_to_cidr(subnet):
    '''
    This function is required to convert netmask to CIDR format.
    '''
    try:
        network = netaddr.IPNetwork(subnet)
        return str(network)
    except netaddr.core.AddrFormatError:
        return subnet

def combine_subnets(id, subnets):
    '''
    This function is required to combine the subnets and also keep the invalid IP address.
    '''
    valid_networks = []
    invalid_entries = []

    for subnet in subnets:
        try:
            network = netaddr.IPNetwork(convert_to_cidr(subnet))
            valid_networks.append(network)
        except netaddr.core.AddrFormatError:
            invalid_entries.append(subnet)
    aggregated = []

    aggregated = netaddr.cidr_merge(valid_networks)

    combined_subnets = ";".join(str(net) for net in aggregated) + ";" + ";".join(invalid_entries)
    combined_subnets = combined_subnets.strip(";") 

    return f"{id},{combined_subnets}"

def process_input(line):
    '''
    This function is required to process the data and segregate ID and the subnets.
    '''
    parts = line.split(":")
    id = parts[0]
    subnets = parts[1].split(",")

    return combine_subnets(id, subnets)

def process_csv(input_file, output_file):
    '''
    This function is required to open input file to clean the data 
    and provide end result to the output file in csv format.
    '''
    results = []
    
    with open(input_file, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            input_str = ', '.join(row)
            cleaned_string = input_str.replace(", ,", "")

            result = process_input(cleaned_string)
            if result:
                results.append(result.split(','))
            
    print(result)
    with open(output_file, mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        for result in results:
            csv_writer.writerow(result)

input_csv = "coalesce_input.csv"
output_csv = "coalesce_output.csv"
process_csv(input_csv, output_csv)
print(f"Output written to {output_csv}")