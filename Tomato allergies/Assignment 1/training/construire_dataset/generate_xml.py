#coding=utf-8
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
from xml.dom import minidom
from PIL import Image
import json

def creat_xml(key = "",list = []):
    labels_tomate = ["939030726152341c154ba28629341da6_lab", "9f2c42629209f86b2d5fbe152eb54803_lab",        # labels des tomates
                     "4e884654d97603dedb7e3bd8991335d0_lab", "f3c12eecb7abc706b032ad9a387e6f01_lab",
                     "e306505b150e000f5e1b4f377ad688a0_lab"]

    output_path = "annotations/" + key.split(".")[0]+".xml"
    image_path = "tomate_images_set/" + key      #image path
    root = ET.Element("annotation")     #root node
    imname = ET.SubElement(root, "folder")      #child node
    imname.text = "images"      #node content
    filename = ET.SubElement(root, "filename")      #editer source
    filename.text = key
    path = ET.SubElement(root, "path")      #editer le chemin d'image
    path.text = image_path
    source = ET.SubElement(root, "source")      #editer source
    source.text = "Unknown"
    size_image = ET.SubElement(root, "size")
    im = Image.open(image_path)
    width, height = im.size
    image_width = ET.SubElement(size_image, "width")
    image_width.text = str(width)
    image_height = ET.SubElement(size_image, "height")
    image_height.text = str(height)
    image_depth = ET.SubElement(size_image, "depth")
    image_depth.text = str(3)
    segmented = ET.SubElement(size_image, "segmented")
    segmented.text = str(0)

    for sous_dict in list:
        if sous_dict["id"] in labels_tomate:
            object = ET.SubElement(root, "object")
            obj_name = ET.SubElement(object, "name")
            obj_name.text = "tomate"
            obj_pose = ET.SubElement(object, "pose")
            obj_pose.text = "unspecified"
            obj_truncated = ET.SubElement(object, "truncated")
            obj_truncated.text = str(0)
            difficulty = ET.SubElement(object, "difficult")
            difficulty.text = str(0)
            bounding_box = ET.SubElement(object, "bndbox")

            xmin = sous_dict["box"][0]
            ymin = sous_dict["box"][1]
            xmax = sous_dict["box"][2] + xmin
            ymax = sous_dict["box"][3] + ymin

            bnd_xmin = ET.SubElement(bounding_box, "xmin")
            bnd_xmin.text = str(xmin)
            bnd_ymin = ET.SubElement(bounding_box, "ymin")
            bnd_ymin.text = str(ymin)
            bnd_xmax = ET.SubElement(bounding_box, "xmax")
            bnd_xmax.text = str(xmax)
            bnd_ymax = ET.SubElement(bounding_box, "ymax")
            bnd_ymax.text = str(ymax)

    xml = minidom.parseString(ET.tostring(root, 'utf-8'))
    pretty_xml_as_string = xml.toprettyxml()
    with open(output_path, 'wb') as f:
        f.write(pretty_xml_as_string.encode('utf-8'))


if __name__=="__main__":
    with open("tomate_image.json", 'r') as load_f:
        load_dict = json.load(load_f)
        for k in load_dict:  # iteration des keys
            creat_xml(k, load_dict[k])