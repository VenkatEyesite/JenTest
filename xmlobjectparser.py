import os
import argparse
from xml.dom.minidom import parse
from xml.dom import minidom
import os.path
parser=argparse.ArgumentParser()
parser.add_argument('-f','--path',type=str,required=False,default='val/')
args=parser.parse_args()

for filename in os.listdir(args.apth):
    tag = parse(args.path + filename)

    root = minidom.Document()
    xml = root.createElement('annotation')
    root.appendChild(xml)

    xml.appendChild(tag.getElementsByTagName('filename')[0])
    xml.appendChild(tag.getElementsByTagName('size')[0])

    for objectTag in tag.getElementsByTagName('object'):
        if objectTag.getElementsByTagName('name')[0].childNodes[0].nodeValue == "n09399592": #give the object name here
            objectTag.getElementsByTagName('name')[0].childNodes[0].nodeValue = 'head'
            xml.appendChild(objectTag)
        elif objectTag.getElementsByTagName('name')[0].childNodes[0].nodeValue == "hand": #give the object name here
            objectTag.getElementsByTagName('name')[0].childNodes[0].nodeValue = 'hand'
            xml.appendChild(objectTag)

    if len(root.getElementsByTagName('object')) > 0:
        if os.path.exists('PHead_Annotations') is False:
            os.makedirs('PHead_Annotations')
        with open('PHead_Annotations/' + (os.path.splitext(filename)[0] + '.xml'), 'w') as f:
            f.write(root.toprettyxml(indent="\t"))
