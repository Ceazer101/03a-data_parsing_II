import csv
import json
import yaml
import xml.etree.ElementTree as ET


# Function to read and parse text files
def parse_text(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        data = [line.strip().split(', ') for line in lines]
        return data

# Function to read and parse XML files
def parse_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    for child in root:
        category = child.tag
        data[category] = [sub.text for sub in child]
    return data

# Function to read and parse YAML files
def parse_yaml(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Function to read and parse JSON files
def parse_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Function to read and parse CSV files
def parse_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


# Test parsing for Set 1
print("Set 2:")
print("Text:")
print(parse_text("../dataFiles/set2/intro.txt"))
print("\nXML:")
print(parse_xml("../dataFiles/set2/skill.xml"))
print("\nYAML:")
print(parse_yaml("../dataFiles/set2/gear.yaml"))
print("\nJSON:")
print(parse_json("../dataFiles/set2/char.json"))
print("\nCSV:")
print(parse_csv("../dataFiles/set2/class.csv"))