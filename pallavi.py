def extract_rsid(gvf_file, input_file, output_file):
    
    rsid_dict = {}

    with open(gvf_file, 'r') as gvf:
        for line in gvf:
            if not line.startswith('#'):  
                parts = line.strip().split('\t')
                chromosome = parts[0]
                position = int(parts[3])
                rsid = None

                attributes = parts[8].split(';')
                for attr in attributes:
                    if attr.startswith('Dbxref=EVA_4:rs'):
                        rsid = attr.split(':')[-1]

                if chromosome not in rsid_dict:
                    rsid_dict[chromosome] = {}
                rsid_dict[chromosome][position] = rsid

    with open(input_file, 'r') as input_data, open(output_file, 'w') as output:
        for line in input_data:
            chromosome, position_str = line.strip().split()
            position = int(position_str)

            rsid = rsid_dict.get(chromosome, {}).get(position, "Not Found")

            output.write(f"{chromosome}\t{position}\t{rsid}\n")

gvf_file = "capra.gvf"
input_file = "capra.txt"
output_file = "capra_result.txt"

extract_rsid(gvf_file, input_file, output_file)
