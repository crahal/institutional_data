"""
#!/usr/bin/env python3

Two every so slightly modified functions created
by the amazing Gabriele Simeone  (github.com/gsime)
whilst working at Transparency International, and
this file is provided with full attribution.

@TODO: multiprocessing functionality
"""


def parse_officer(line):
    """
    Summary: Parse a line of officer data from the FTP
    Inputs: line of raw ftp data
    Outputs: a dictionary of data parsed from the line
    """
    results = dict()
    results['appointed_to_company_number'] = line[0:8]
    results['record_type'] = line[8]
    results['appointment_date_origin_code'] = line[9:10]
    results['officer_role_code'] = line[10:12]
    results['pnr'] = line[12:24]
    results['is_company'] = line[24] == 'Y'
    results['filler_a'] = line[25:32]
    results['start_date_text'] = line[32:40]
    results['end_date_text'] = line[40:48]
    results['service_address_post_code'] = line[48:56]
    results['partial_dob'] = line[56:64]
    results['full_dob'] = line[64:72]
    results['unwanted_variable_data_length'] = line[72:76]
    variable_data = line[76:].rstrip(' \n')
    vardata = variable_data.split('<')
    vardata_components = (
        'title',
        'name',
        'surname',
        'honours',
        'service_address_care_of',
        'service_address_po_box',
        'service_address_line_1',
        'service_address_line_2',
        'service_address_post_town',
        'service_address_county',
        'service_address_country',
        'occupation',
        'nationality',
        'ura_country',
        'filler_b',)
    for component, datapoint in zip(vardata_components, vardata):
        results[component] = datapoint
    return results


def parse_company(line):
    """
    Summary: Parse a line of officer data from the FTP
    Inputs: line of raw ftp data
    Outputs: a dictionary of data parsed from the line
    """
    results = dict()
    results['company_number'] = line[0:8]
    results['record_type'] = line[8]
    results['company_status_code'] = line[9]
    results['is_company'] = line[24] == 'Y'
    results['filler'] = line[10:32]
    results['number_of_officers'] = line[32:36]
    results['unwanted_company_name_length'] = line[36:40]
    results['company_name'] = line[40:].strip('< \n')
    return results
