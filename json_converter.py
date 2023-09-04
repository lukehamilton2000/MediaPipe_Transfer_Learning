import json

def convert_to_coco_json(data):
  """Converts the given data into COCO JSON format.

  Args:
    data: The data to convert.

  Returns:
    A COCO JSON object.
  """

  coco_json = {
      "info": {
          "description": "A dataset of flower images.",
          "url": "https://example.com/flower_dataset/",
          "version": "1.0",
          "year": 2023,
          "contributor": "Bard",
          "licenses": [
              {
                  "id": 1,
                  "name": "Attribution-NonCommercial-NoDerivs 4.0 International",
                  "url": "https://creativecommons.org/licenses/by-nc-nd/4.0/"
              }
          ]
      },
      "images": [],
      "annotations": []
  }

  for image_data in data:
    image = {
        "id": image_data["image_id"],
        "file_name": image_data["file_name"],
        "width": image_data["width"],
        "height": image_data["height"]
    }
    coco_json["images"].append(image)

  for annotation_data in data:
    annotation = {
        "id": annotation_data["annotation_id"],
        "image_id": annotation_data["image_id"],
        "category_id": 1,
        "iscrowd": 0,
        "bbox": annotation_data["bbox"],
        "area": annotation_data["area"]
    }
    coco_json["annotations"].append(annotation)

  return coco_json


if __name__ == "__main__":
  data = [
    filename,file_size,file_attributes,region_count,region_id,region_shape_attributes,region_attributes
    image1.jpg,93782,"{}",3,0,"{""name"":""rect"",""x"":480,""y"":11,""width"":481,""height"":422}","{""name"":""flower""}"
    image1.jpg,93782,"{}",3,1,"{""name"":""rect"",""x"":262,""y"":507,""width"":305,""height"":207}","{""name"":""flower""}"
    image1.jpg,93782,"{}",3,2,"{""name"":""rect"",""x"":620,""y"":440,""width"":242,""height"":274}","{""name"":""flower""}"
    image2.jpg,60260,"{}",4,0,"{""name"":""rect"",""x"":278,""y"":599,""width"":277,""height"":207}","{""name"":""flower""}"
    image2.jpg,60260,"{}",4,1,"{""name"":""rect"",""x"":342,""y"":327,""width"":227,""height"":248}","{""name"":""flower""}"
    image2.jpg,60260,"{}",4,2,"{""name"":""rect"",""x"":134,""y"":282,""width"":192,""height"":290}","{""name"":""flower""}"
    image2.jpg,60260,"{}",4,3,"{""name"":""rect"",""x"":279,""y"":144,""width"":156,""height"":210}","{""name"":""flower""}"
    image3.png,238633,"{}",2,0,"{""name"":""rect"",""x"":94,""y"":79,""width"":289,""height"":193}","{""name"":""flower""}"
    image3.png,238633,"{}",2,1,"{""name"":""rect"",""x"":91,""y"":35,""width"":98,""height"":129}","{""name"":""flower""}"
    image4.jpg,7834,"{}",1,0,"{""name"":""rect"",""x"":77,""y"":17,""width"":131,""height"":148}","{""name"":""flower""}"
    image5.jpg,142500,"{}",2,0,"{""name"":""rect"",""x"":261,""y"":48,""width"":239,""height"":260}","{""name"":""flower""}"
    image5.jpg,142500,"{}",2,1,"{""name"":""rect"",""x"":716,""y"":45,""width"":68,""height"":226}","{""name"":""flower""}"
    image6.jpg,213054,"{}",4,0,"{""name"":""rect"",""x"":762,""y"":386,""width"":286,""height"":341}","{""name"":""flower""}"
    image6.jpg,213054,"{}",4,1,"{""name"":""rect"",""x"":705,""y"":770,""width"":291,""height"":349}","{""name"":""flower""}"
    image6.jpg,213054,"{}",4,2,"{""name"":""rect"",""x"":622,""y"":1181,""width"":336,""height"":379}","{""name"":""flower""}"
    image6.jpg,213054,"{}",4,3,"{""name"":""rect"",""x"":1754,""y"":405,""width"":173,""height"":166}","{""name"":""flower""}"
    image7.jpg,176024,"{}",2,0,"{""name"":""rect"",""x"":562,""y"":6,""width"":263,""height"":289}","{""name"":""flower""}"
    image7.jpg,176024,"{}",2,1,"{""name"":""rect"",""x"":400,""y"":261,""width"":407,""height"":461}","{""name"":""flower""}"
    image8.jpg,62461,"{}",2,0,"{""name"":""rect"",""x"":164,""y"":24,""width"":85,""height"":88}","{""name"":""flower""}"
    image8.jpg,62461,"{}",2,1,"{""name"":""rect"",""x"":184,""y"":94,""width"":124,""height"":89}","{""name"":""flower""}"
    image9.jpg,148478,"{}",3,0,"{""name"":""rect"",""x"":291,""y"":84,""width"":361,""height"":382}","{""name"":""flower""}"
    image9.jpg,148478,"{}",3,1,"{""name"":""rect"",""x"":832,""y"":387,""width"":149,""height"":199}","{""name"":""flower""}"
    image9.jpg,148478,"{}",3,2,"{""name"":""rect"",""x"":972,""y"":4,""width"":290,""height"":233}","{""name"":""flower""}"
    image10.jpg,74383,"{}",6,0,"{""name"":""rect"",""x"":56,""y"":315,""width"":102,""height"":121}","{""name"":""flower""}"
    image10.jpg,74383,"{}",6,1,"{""name"":""rect"",""x"":194,""y"":388,""width"":39,""height"":63}","{""name"":""flower""}"
    image10.jpg,74383,"{}",6,2,"{""name"":""rect"",""x"":342,""y"":379,""width"":32,""height"":78}","{""name"":""flower""}"
    image10.jpg,74383,"{}",6,3,"{""name"":""rect"",""x"":726,""y"":317,""width"":105,""height"":153}","{""name"":""flower""}"
    image10.jpg,74383,"{}",6,4,"{""name"":""rect"",""x"":645,""y"":482,""width"":51,""height"":44}","{""name"":""flower""}"
    image10.jpg,74383,"{}",6,5,"{""name"":""rect"",""x"":502,""y"":133,""width"":48,""height"":98}","{""name"":""flower""}"
    image11.jpg,100705,"{}",6,0,"{""name"":""rect"",""x"":71,""y"":36,""width"":185,""height"":136}","{""name"":""flower""}"
    image11.jpg,100705,"{}",6,1,"{""name"":""rect"",""x"":286,""y"":2,""width"":181,""height"":82}","{""name"":""flower""}"
    image11.jpg,100705,"{}",6,2,"{""name"":""rect"",""x"":476,""y"":7,""width"":168,""height"":119}","{""name"":""flower""}"
    image11.jpg,100705,"{}",6,3,"{""name"":""rect"",""x"":516,""y"":136,""width"":169,""height"":89}","{""name"":""flower""}"
    image11.jpg,100705,"{}",6,4,"{""name"":""rect"",""x"":609,""y"":194,""width"":137,""height"":153}","{""name"":""flower""}"
    image11.jpg,100705,"{}",6,5,"{""name"":""rect"",""x"":243,""y"":27,""width"":153,""height"":251}","{""name"":""flower""}"
    image12.jpg,178377,"{}",2,0,"{""name"":""rect"",""x"":142,""y"":161,""width"":549,""height"":608}","{""name"":""flower""}"
    image12.jpg,178377,"{}",2,1,"{""name"":""rect"",""x"":691,""y"":399,""width"":407,""height"":457}","{""name"":""flower""}"
    image13.jpg,90917,"{}",2,0,"{""name"":""rect"",""x"":228,""y"":13,""width"":586,""height"":584}","{""name"":""flower""}"
    image13.jpg,90917,"{}",2,1,"{""name"":""rect"",""x"":745,""y"":382,""width"":273,""height"":377}","{""name"":""flower""}"
    image14.jpg,123640,"{}",2,0,"{""name"":""rect"",""x"":129,""y"":236,""width"":227,""height"":171}","{""name"":""flower""}"
    image14.jpg,123640,"{}",2,1,"{""name"":""rect"",""x"":435,""y"":140,""width"":115,""height"":171}","{""name"":""flower""}"
    image15.jpg,38559,"{}",1,0,"{""name"":""rect"",""x"":100,""y"":72,""width"":320,""height"":311}","{""name"":""flower""}"
    image16.jpg,49053,"{}",3,0,"{""name"":""rect"",""x"":243,""y"":81,""width"":168,""height"":162}","{""name"":""flower""}"
    image16.jpg,49053,"{}",3,1,"{""name"":""rect"",""x"":106,""y"":182,""width"":117,""height"":181}","{""name"":""flower""}"
    image16.jpg,49053,"{}",3,2,"{""name"":""rect"",""x"":183,""y"":74,""width"":67,""height"":108}","{""name"":""flower""}"
    image17.jpg,36353,"{}",7,0,"{""name"":""rect"",""x"":144,""y"":418,""width"":226,""height"":169}","{""name"":""flower""}"
    image17.jpg,36353,"{}",7,1,"{""name"":""rect"",""x"":657,""y"":441,""width"":165,""height"":181}","{""name"":""flower""}"
    image17.jpg,36353,"{}",7,2,"{""name"":""rect"",""x"":389,""y"":579,""width"":169,""height"":169}","{""name"":""flower""}"
    image17.jpg,36353,"{}",7,3,"{""name"":""rect"",""x"":166,""y"":672,""width"":163,""height"":103}","{""name"":""flower""}"
    image17.jpg,36353,"{}",7,4,"{""name"":""rect"",""x"":4,""y"":687,""width"":81,""height"":78}","{""name"":""flower""}"
    image17.jpg,36353,"{}",7,5,"{""name"":""rect"",""x"":385,""y"":493,""width"":111,""height"":80}","{""name"":""flower""}"
    image17.jpg,36353,"{}",7,6,"{""name"":""rect"",""x"":492,""y"":415,""width"":160,""height"":167}","{""name"":""flower""}"
    image18.jpg,89232,"{}",3,0,"{""name"":""rect"",""x"":827,""y"":81,""width"":404,""height"":390}","{""name"":""flower""}"
    image18.jpg,89232,"{}",3,1,"{""name"":""rect"",""x"":554,""y"":392,""width"":357,""height"":197}","{""name"":""flower""}"
    image18.jpg,89232,"{}",3,2,"{""name"":""rect"",""x"":633,""y"":4,""width"":390,""height"":63}","{""name"":""flower""}"
    image19.jpg,218447,"{}",3,0,"{""name"":""rect"",""x"":746,""y"":188,""width"":168,""height"":88}","{""name"":""flower""}"
    image19.jpg,218447,"{}",3,1,"{""name"":""rect"",""x"":768,""y"":399,""width"":155,""height"":194}","{""name"":""flower""}"
    image19.jpg,218447,"{}",3,2,"{""name"":""rect"",""x"":642,""y"":312,""width"":122,""height"":173}","{""name"":""flower""}"
    image20.jpg,76184,"{}",4,0,"{""name"":""rect"",""x"":174,""y"":89,""width"":120,""height"":187}","{""name"":""flower""}"
    image20.jpg,76184,"{}",4,1,"{""name"":""rect"",""x"":241,""y"":178,""width"":239,""height"":207}","{""name"":""flower""}"
    image20.jpg,76184,"{}",4,2,"{""name"":""rect"",""x"":484,""y"":168,""width"":186,""height"":198}","{""name"":""flower""}"
    image20.jpg,76184,"{}",4,3,"{""name"":""rect"",""x"":429,""y"":360,""width"":135,""height"":99}","{""name"":""flower""}"
    image21.jpg,177968,"{}",15,0,"{""name"":""rect"",""x"":553,""y"":121,""width"":90,""height"":73}","{""name"":""flower""}"
    image21.jpg,177968,"{}",15,1,"{""name"":""rect"",""x"":283,""y"":649,""width"":80,""height"":64}","{""name"":""flower""}"
    image21.jpg,177968,"{}",15,2,"{""name"":""rect"",""x"":437,""y"":713,""width"":63,""height"":42}","{""name"":""flower""}"
    image21.jpg,177968,"{}",15,3,"{""name"":""rect"",""x"":710,""y"":463,""width"":102,""height"":99}","{""name"":""flower""}"
    image21.jpg,177968,"{}",15,4,"{""name"":""rect"",""x"":897,""y"":555,""width"":78,""height"":79}","{""name"":""flower""}"
    image21.jpg,177968,"{}",15,5,"{""name"":""rect"",""x"":753,""y"":660,""width"":49,""height"":50}","{""name"":""flower""}"
    image21.jpg,177968,"{}",15,6,"{""name"":""rect"",""x"":742,""y"":829,""width"":61,""height"":70}","{""name"":""flower""}"
    image21.jpg,177968,"{}",15,7,"{""name"":""rect"",""x"":792,""y"":934,""width"":98,""height"":40}","{""name"":""flower""}"
    image21.jpg,177968,"{}",15,8,"{""name"":""rect"",""x"":853,""y"":846,""width"":38,""height"":37}","{""name"":""flower""}"
    image21.jpg,177968,"{}",15,9,"{""name"":""rect"",""x"":817,""y"":753,""width"":79,""height"":72}","{""name"":""flower""}"
    image21.jpg,177968,"{}",15,10,"{""name"":""rect"",""x"":852,""y"":630,""width"":61,""height"":61}","{""name"":""flower""}"
    image21.jpg,177968,"{}",15,11,"{""name"":""rect"",""x"":604,""y"":271,""width"":48,""height"":60}","{""name"":""flower""}"
    image21.jpg,177968,"{}",15,12,"{""name"":""rect"",""x"":485,""y"":194,""width"":65,""height"":59}","{""name"":""flower""}"
    image21.jpg,177968,"{}",15,13,"{""name"":""rect"",""x"":1092,""y"":315,""width"":20,""height"":43}","{""name"":""flower""}"
    image21.jpg,177968,"{}",15,14,"{""name"":""rect"",""x"":1022,""y"":296,""width"":43,""height"":40}","{""name"":""flower""}"
    image22.jpg,10220,"{}",10,0,"{""name"":""rect"",""x"":20,""y"":134,""width"":47,""height"":33}","{""name"":""flower""}"
    image22.jpg,10220,"{}",10,1,"{""name"":""rect"",""x"":82,""y"":112,""width"":32,""height"":29}","{""name"":""flower""}"
    image22.jpg,10220,"{}",10,2,"{""name"":""rect"",""x"":34,""y"":16,""width"":52,""height"":47}","{""name"":""flower""}"
    image22.jpg,10220,"{}",10,3,"{""name"":""rect"",""x"":52,""y"":92,""width"":24,""height"":34}","{""name"":""flower""}"
    image22.jpg,10220,"{}",10,4,"{""name"":""rect"",""x"":17,""y"":81,""width"":21,""height"":35}","{""name"":""flower""}"
    image22.jpg,10220,"{}",10,5,"{""name"":""rect"",""x"":130,""y"":4,""width"":45,""height"":49}","{""name"":""flower""}"
    image22.jpg,10220,"{}",10,6,"{""name"":""rect"",""x"":106,""y"":66,""width"":43,""height"":40}","{""name"":""flower""}"
    image22.jpg,10220,"{}",10,7,"{""name"":""rect"",""x"":157,""y"":34,""width"":54,""height"":36}","{""name"":""flower""}"
    image22.jpg,10220,"{}",10,8,"{""name"":""rect"",""x"":147,""y"":80,""width"":29,""height"":39}","{""name"":""flower""}"
    image22.jpg,10220,"{}",10,9,"{""name"":""rect"",""x"":184,""y"":73,""width"":55,""height"":48}","{""name"":""flower""}"
    image23.jpg,64239,"{}",8,0,"{""name"":""rect"",""x"":120,""y"":131,""width"":78,""height"":57}","{""name"":""flower""}"
    image23.jpg,64239,"{}",8,1,"{""name"":""rect"",""x"":214,""y"":35,""width"":69,""height"":81}","{""name"":""flower""}"
    image23.jpg,64239,"{}",8,2,"{""name"":""rect"",""x"":479,""y"":25,""width"":90,""height"":117}","{""name"":""flower""}"
    image23.jpg,64239,"{}",8,3,"{""name"":""rect"",""x"":226,""y"":127,""width"":46,""height"":69}","{""name"":""flower""}"
    image23.jpg,64239,"{}",8,4,"{""name"":""rect"",""x"":278,""y"":127,""width"":51,""height"":83}","{""name"":""flower""}"
    image23.jpg,64239,"{}",8,5,"{""name"":""rect"",""x"":361,""y"":41,""width"":80,""height"":113}","{""name"":""flower""}"
    image23.jpg,64239,"{}",8,6,"{""name"":""rect"",""x"":449,""y"":102,""width"":41,""height"":71}","{""name"":""flower""}"
    image23.jpg,64239,"{}",8,7,"{""name"":""rect"",""x"":294,""y"":10,""width"":73,""height"":76}","{""name"":""flower""}"
    image24.jpg,73449,"{}",4,0,"{""name"":""rect"",""x"":134,""y"":35,""width"":178,""height"":199}","{""name"":""flower""}"
    image24.jpg,73449,"{}",4,1,"{""name"":""rect"",""x"":371,""y"":98,""width"":139,""height"":138}","{""name"":""flower""}"
    image24.jpg,73449,"{}",4,2,"{""name"":""rect"",""x"":404,""y"":272,""width"":142,""height"":164}","{""name"":""flower""}"
    image24.jpg,73449,"{}",4,3,"{""name"":""rect"",""x"":223,""y"":205,""width"":206,""height"":139}","{""name"":""flower""}"
    image25.png,362044,"{}",1,0,"{""name"":""rect"",""x"":199,""y"":54,""width"":294,""height"":286}","{""name"":""flower""}"
    image26.jpg,69491,"{}",4,0,"{""name"":""rect"",""x"":323,""y"":295,""width"":168,""height"":187}","{""name"":""flower""}"
    image26.jpg,69491,"{}",4,1,"{""name"":""rect"",""x"":500,""y"":422,""width"":166,""height"":126}","{""name"":""flower""}"
    image26.jpg,69491,"{}",4,2,"{""name"":""rect"",""x"":189,""y"":97,""width"":179,""height"":152}","{""name"":""flower""}"
    image26.jpg,69491,"{}",4,3,"{""name"":""rect"",""x"":107,""y"":243,""width"":153,""height"":109}","{""name"":""flower""}"
    image27.jpg,68119,"{}",3,0,"{""name"":""rect"",""x"":283,""y"":210,""width"":198,""height"":137}","{""name"":""flower""}"
    image27.jpg,68119,"{}",3,1,"{""name"":""rect"",""x"":307,""y"":6,""width"":162,""height"":187}","{""name"":""flower""}"
    image27.jpg,68119,"{}",3,2,"{""name"":""rect"",""x"":557,""y"":85,""width"":166,""height"":192}","{""name"":""flower""}"
    image28.jpg,57231,"{}",3,0,"{""name"":""rect"",""x"":467,""y"":453,""width"":143,""height"":236}","{""name"":""flower""}"
    image28.jpg,57231,"{}",3,1,"{""name"":""rect"",""x"":238,""y"":489,""width"":123,""height"":157}","{""name"":""flower""}"
    image28.jpg,57231,"{}",3,2,"{""name"":""rect"",""x"":373,""y"":341,""width"":102,""height"":41}","{""name"":""flower""}"
    image29.jpg,680425,"{}",1,0,"{""name"":""rect"",""x"":356,""y"":185,""width"":278,""height"":262}","{""name"":""flower""}"
    image30.jpg,1317132,"{}",1,0,"{""name"":""rect"",""x"":284,""y"":66,""width"":1985,""height"":2197}","{""name"":""flower""}"
    image31.jpg,91878,"{}",3,0,"{""name"":""rect"",""x"":484,""y"":371,""width"":132,""height"":166}","{""name"":""flower""}"
    image31.jpg,91878,"{}",3,1,"{""name"":""rect"",""x"":537,""y"":225,""width"":138,""height"":154}","{""name"":""flower""}"
    image31.jpg,91878,"{}",3,2,"{""name"":""rect"",""x"":628,""y"":390,""width"":173,""height"":164}","{""name"":""flower""}"
    image32.jpg,73320,"{}",8,0,"{""name"":""rect"",""x"":576,""y"":515,""width"":99,""height"":141}","{""name"":""flower""}"
    image32.jpg,73320,"{}",8,1,"{""name"":""rect"",""x"":419,""y"":357,""width"":171,""height"":205}","{""name"":""flower""}"
    image32.jpg,73320,"{}",8,2,"{""name"":""rect"",""x"":690,""y"":334,""width"":122,""height"":125}","{""name"":""flower""}"
    image32.jpg,73320,"{}",8,3,"{""name"":""rect"",""x"":144,""y"":123,""width"":133,""height"":121}","{""name"":""flower""}"
    image32.jpg,73320,"{}",8,4,"{""name"":""rect"",""x"":320,""y"":118,""width"":151,""height"":172}","{""name"":""flower""}"
    image32.jpg,73320,"{}",8,5,"{""name"":""rect"",""x"":422,""y"":17,""width"":233,""height"":139}","{""name"":""flower""}"
    image32.jpg,73320,"{}",8,6,"{""name"":""rect"",""x"":640,""y"":97,""width"":133,""height"":152}","{""name"":""flower""}"
    image32.jpg,73320,"{}",8,7,"{""name"":""rect"",""x"":580,""y"":231,""width"":140,""height"":100}","{""name"":""flower""}"
    image33.jpg,9787,"{}",2,0,"{""name"":""rect"",""x"":58,""y"":51,""width"":98,""height"":78}","{""name"":""flower""}"
    image33.jpg,9787,"{}",2,1,"{""name"":""rect"",""x"":176,""y"":73,""width"":57,""height"":52}","{""name"":""flower""}"
    image34.jpg,10639,"{}",1,0,"{""name"":""rect"",""x"":94,""y"":12,""width"":105,""height"":100}","{""name"":""flower""}"
    image35.jpg,20878,"{}",3,0,"{""name"":""rect"",""x"":28,""y"":44,""width"":89,""height"":106}","{""name"":""flower""}"
    image35.jpg,20878,"{}",3,1,"{""name"":""rect"",""x"":125,""y"":42,""width"":122,""height"":129}","{""name"":""flower""}"
    image35.jpg,20878,"{}",3,2,"{""name"":""rect"",""x"":260,""y"":171,""width"":72,""height"":98}","{""name"":""flower""}"
    image36.jpg,131676,"{}",3,0,"{""name"":""rect"",""x"":40,""y"":33,""width"":313,""height"":184}","{""name"":""flower""}"
    image36.jpg,131676,"{}",3,1,"{""name"":""rect"",""x"":175,""y"":215,""width"":228,""height"":158}","{""name"":""flower""}"
    image36.jpg,131676,"{}",3,2,"{""name"":""rect"",""x"":349,""y"":15,""width"":254,""height"":248}","{""name"":""flower""}"
    image37.jpg,619474,"{}",4,0,"{""name"":""rect"",""x"":558,""y"":173,""width"":170,""height"":145}","{""name"":""flower""}"
    image37.jpg,619474,"{}",4,1,"{""name"":""rect"",""x"":567,""y"":520,""width"":81,""height"":115}","{""name"":""flower""}"
    image37.jpg,619474,"{}",4,2,"{""name"":""rect"",""x"":678,""y"":543,""width"":96,""height"":106}","{""name"":""flower""}"
    image37.jpg,619474,"{}",4,3,"{""name"":""rect"",""x"":615,""y"":431,""width"":66,""height"":52}","{""name"":""flower""}"
    image38.jpg,8879,"{}",2,0,"{""name"":""rect"",""x"":72,""y"":17,""width"":77,""height"":92}","{""name"":""flower""}"
    image38.jpg,8879,"{}",2,1,"{""name"":""rect"",""x"":95,""y"":80,""width"":122,""height"":113}","{""name"":""flower""}"
    image39.jpg,98170,"{}",2,0,"{""name"":""rect"",""x"":267,""y"":102,""width"":238,""height"":256}","{""name"":""flower""}"
    image39.jpg,98170,"{}",2,1,"{""name"":""rect"",""x"":805,""y"":345,""width"":95,""height"":117}","{""name"":""flower""}"
    image40.jpg,70755,"{}",3,0,"{""name"":""rect"",""x"":445,""y"":60,""width"":103,""height"":158}","{""name"":""flower""}"
    image40.jpg,70755,"{}",3,1,"{""name"":""rect"",""x"":574,""y"":99,""width"":38,""height"":76}","{""name"":""flower""}"
    image40.jpg,70755,"{}",3,2,"{""name"":""rect"",""x"":334,""y"":5,""width"":73,""height"":108}","{""name"":""flower""}"
  ]

  coco_json = convert_to_coco_json(data)

  print(json.dumps(coco_json))
