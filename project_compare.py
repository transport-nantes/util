#!/usr/bin/python3

"""Project visualiser/comparator.

Read a JSON config file with project data and provide a visualisation
of the data.

The JSON config file should be an array with objects having the
following keys:

    name        The project name
    revenue     Estimated project revenue
    public      Estimated number of people affected by the project

Missing keys have default values (0 or empty) and should elicit warnings.

"""

import argparse
import matplotlib.pyplot as plt
import json
import tabulate

def viz_revenue_public(data):
    """Visualise by expected revenue and public affected.
    """
    names = [item["name"] for item in data]
    revenue = [item["revenue"] for item in data]
    public = [item["public"] for item in data]
    plt.scatter(revenue, public, s=60)
    for index in range(len(names)):
        plt.text(revenue[index] + 20, public[index] + 100, names[index], fontsize=20)
    plt.xlabel("Revenu", fontsize=20)
    plt.ylabel("Public", fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()

def emit_table(data):
    """Print a table summarising JSON data.
    """
    columns = [{"projet": item["name"], "revenu": item["revenue"], "public": item["public"]}
                for item in data]
    print(tabulate.tabulate(columns, headers="keys", tablefmt="fancy_grid"))

def main():
    """Do what we do."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, required=True,
                        help='Filename containing project config as JSON')
    parser.add_argument('--visu', type=str, required=True,
                        help='Visualisation type')
    args = parser.parse_args()
    with open(args.config, 'r') as fp_in:
        data = json.load(fp_in)
        if ('revenue-public' == args.visu):
            viz_revenue_public(data)
        elif 'table' == args.visu:
            emit_table(data)

if __name__ == '__main__':
    main()
