from flask import Flask, jsonify, request, send_file
from qr_code import qrcode_generator

app =  Flask( __name__ )
# app.config['TIMEOUT'] = 10

@app.route('/')
def hello_word():
    return jsonify({'message': 'Hello world!'})

@app.route('/qrcode', methods = ['POST', 'GET'])
def generate_qrcode():
    if request.method == 'POST':
        req =  request.get_json()
        print(req)
        # list of required fields
        required = ['data']
        # Checking if required fields are present in the request
        if all(field in req for field in required):
            print ("Request seems good") 
        else:
            print ("Not good") 
            return jsonify({'message': "Mandatory parameter is missing. {}".format(required)}) 

        img = qrcode_generator.create_qrcode(req['data'],\
                                            #  req.get("path", None),\
                                             box_size= req.get('box_size', 10),\
                                             border= req.get('border', 1),\
                                             base64encode= req.get('base64', False),)
        print(type(img))
        if req.get('base64', False):
            return img
        elif not req.get("path", False):
            return send_file(img, mimetype='image/png')
        else:
            return jsonify({'message': "Image saved at {}".format(req.get("path", False))})
        
    else:
        return jsonify({'message': '''Use a POST method with the following structure:
{
    "data": "<URL>",
    "path": "<path/to/folder/filename>.png", (optional)
    "box_size": <image size> (int) (optional),  
    "border": <image border>   (int) (optional),
    "base64: Bool - indicates if a base64code will be returned
}'''})

if __name__ == '__main__':
    print("MYAPPS is running!")
    app.run(host='0.0.0.0', port=5000)
    print("MYAPPS is running!?")