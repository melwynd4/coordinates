#!/home/mdsouza/anaconda3/bin/python
'''
Solves the problem of coordinates closest to the input coordinates
'''
import json
from math import sqrt
import click

def read_conf(file_name):
    '''
    Read the coordinates file
    '''
    with open(file_name) as infile:
            conf = json.load(infile)
    return conf

def new_coordinates(point, coord_file):
    '''
    Generate new coordinates based on the position of the point
    '''
    conf = read_conf(coord_file)
    for i in conf:
        #distance from input point
        x = float(point['x']) - float(i['value'].split(',')[0])
        y = float(point['y']) - float(i['value'].split(',')[1])
        #Find z = sqrt(x*x + y*y)
        #for each of the coordinates
        #then sort them in a list
        i['distance'] = sqrt(x*x + y*y)
        
    #sort based on distance
    conf_n = sorted(conf, key=lambda k: k['distance'])
    #remove distance
    for i in conf_n:
        i.pop('distance')
    #return
    return conf_n



@click.command()
@click.option('--x', default=6, help='target x coordinates')
@click.option('--y', default=33, help='target y coordinates')
@click.option('--coordinatesfile', default='coordinates.json', help='input coordinates file.')
@click.option('--outputfile', default='new_coordinates_x_6_y_33.json', help='output coordinates file.')
def process_cmdline(x, y, coordinatesfile, outputfile):
    try:
        args = [x, y, coordinatesfile, outputfile]
        conf_n = new_coordinates({'x':x, 'y':y}, coordinatesfile)
        with open(outputfile, 'w') as fp:
            json.dump(conf_n, fp)
    except:
        logging.exception('main:Exception')

if __name__ == '__main__':
    process_cmdline()
